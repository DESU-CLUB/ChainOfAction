import re
import time

import openai

class ActionAgent:
    def __init__(
            self,
            model_name = 'gpt-3.5-turbo',
            temperature = 0,
            ckpt_dir = "ckpt",
            resume = False,
            chat_log=  True,
            execution_error = True
    ):
        self.ckpt_dir = ckpt_dir
        self.chat_log=  chat_log
        self.execution_error = execution_error
