from chainofaction.agents import load_prompt
from chainofaction.utils.json_utils import fix_and_parse_json
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

class CriticAgent:
    def __init__(
            self,
            model_name = "gpt-3.5-turbo",
            temperature = 0,
            request_timeout = 120,
            mode = "auto"):
        self.lm = ChatOpenAI( 
            model_name = model_name,
            temperature = temperature,
            request_timeout = request_timeout,
        )
        assert mode in ["auto", "manual"]
        self.mode = mode

    def render_system_message(self):
        system_message = SystemMessage(content = load_prompt("critic"))
        return system_message
    

    def render_human_message(self, *, events, task, context):
        assert events[-1][0] == "observe", "Last event must be an observation"
        testcases_passed = events[-1][1]['testcases']
        testcase_failed = events[-1][1]['testcase_failed']
        code_outcome = events[-1][1]['interpreted'] #Check if code can run
        skills_used = events[-1][1]['skills']


        for i, (event_type, event) in enumerate(events):
            if event_type == 'onError':
                print(f"\033[31mCritic Agent: Error occurs {event['onError']}\033[0m")
                return None
            
        observation = ""

        observation +=f"Testcases passed: {testcases_passed}\n\n"
        if testcase_failed != None:
            observation+=f"Specific testcase failed on: {testcase_failed}\n\n"
        else:
            observation += f"All test cases passed\n\n"
        if code_outcome == True:
            observation +=f"Code can run:\n\n"
        else:
            observation+= f"Code cannot run {code_outcome}:\n\n"

        observation += f"Skills used: {skills_used}\n\n"
                
        print(f"\033[31m****Critic Agent human message****\n{observation}\033[0m")
        return HumanMessage(content = observation)
    
    def human_check_task_success(self):
        confirmed = False
        success = False
        critique = ''
        while not confirmed:
            success = input("Success? (y/n)")
            success = success.lower() == "y"
            critique = input("Enter your critique")
            confirmed = input("Confirm? (y/n)") in ["y",""]

        return success, critique
    

    def ai_check_task_success(self, messages, max_retries = 5):
        if max_retries == 0:
            print(
            "\033[31mFailed to parse Critic Agent response. Consider updating your prompt.\033[0m"
            )
            return False, ""
        
        if messages[1] is None:
            return False, ""
        
        critic = self.llm(messages).content
        print(f"\033[31m****Critic Agent ai message****\n{critic}\033[0m")
        try:
            response = fix_and_parse_json(critic)
            assert response["success"] in [True, False]
            if "critique" not in response:
                response['critique'] = ""
            return response["success"], response["critique"]
        except Exception as e:
            print(f"\033[31mError parsing critic response: {e} Trying again!\033[0m")
            return self.ai_check_task_success(
                messages= messages,
                max_retries = max
            )
        