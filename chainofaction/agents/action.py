import re
import time
import chainofaction.utils as U
from langchain.chat_models import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage

import openai

class ActionAgent:
    def __init__(
            self,
            model_name = 'gpt-3.5-turbo',
            temperature = 0,
            request_timeout = 120,
            ckpt_dir = "ckpt",
            resume = False,
            chat_log=  True,
            execution_error = True,
        
    ):
        self.ckpt_dir = ckpt_dir
        self.chat_log=  chat_log
        self.execution_error = execution_error
        U.f_mk_dir(f"{self.ckpt_dir}/actions")
        if resume:
            print(f"\033[32mLoading Action Agent from {ckpt_dir}/action\033[0m")
            self.memory = U.load_json(f"{self.ckpt_dir}/actions/memory.json")

        else:
            self.memory = {}
            self.llm = ChatOpenAI(model_name=model_name, temperature=temperature, request_timeout = request_timeout)


    def render_system_message(self, skills = []):
        system_template = load_prompt("action_message")
        base_skills = []
        if not self.llm.model_name == "gpt-3.5-turbo":
            base_skills+=[]
            #Add new skills if weaker model
        
        programs = '\n\n'.join(load_control_primitives_contexts(base_skills)+skills)

        response_format = load_prompt("action_response format")
        system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
        system_message = system_message_prompt.format(
            programs = programs, response_format=  response_format
        )
        assert isinstance(system_message, SystemMessage)
        return system_message
    
    def render_human_message(self, *, events, code = "", task ="", context = "", critique = ""):
        chat_messages= []
        error_messages = []
        damage_messages = []
        assert events[-1][0] == "observe", "Last event must be an observation"
        for i, (event_type, event) in enumerate(events):
            if event_type == "onChat":
                    chat_messages.append(event["onChat"])
            elif event_type == "onError":
                error_messages.append(event["onError"])

            elif event_type == 'observe':
                #Add stuff here based on what we're looking at to 
                #Decompose code
                assert i == len(events) -1
            

            observation = ""

            if code:
                observation += f"Code from the last round: \n{code}\n\n"
            else:
                observation += f"Code from the last round: No code in the first round "

            if self.execution_error:
                if error_messages:
                    error ="\n".join(error_messages)
                    onservation = f"Execution Error:\n{error}\n\n"

            if self.chat_log:
                if chat_messages:
                    chat_log = "\n".join(chat_messages)
                    observation +=f"Chat log: {chat_log}\n\n"
                else:
                    observation = f"Chat log: None\n\n"

            observation += f"Task {task}\n\n"

            if context:
                observation += f"Context: {context}\n\n"
            else:
                observation += f"Context: None\n\n"

            if critique:
                observation ++f"Critique: {critique}\n\n"
            else:
                observation +=f"Critique: None\n\n"

            return HumanMessage(content = observation)


    def process_ai_message(self, message):
            assert isinstance(message, AIMessage)

            retry = 3
            error = None
            while retry > 0:
                try:                
                    code_pattern = re.compile(r"```(?:python|py)(.*?)```", re.DOTALL)
                    code = "\n".join(code_pattern.findall(message.content))
                    functions = []
                    assert len(list(code))) >0, "NO functions found"
                except:
                    pass
        
