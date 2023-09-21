# Chain Of Action: Solving Problems With Stepwise Action
Wing@NUS CS6101 T2310 Project

## Abstract
We introduce a new prompting strategy, Chain of Action, which aims to decompose problems into a high level action plan and convert these steps into actions taken by an agentic LLM, learns to generate new skills via interacting with the environment, and refines the global action plan while iteratively correcting our solution for a single step.  Similar to the Voyager paper by Guanzhi et. al, we prompt the model to generate skills and store them in a database. However, we  We hypothesise that 1) the decomposition of complex problems into smaller skills will aid the model in solving more complex tasks, 2) the refining of the model's action plan on the fly will improve on previous prompting strategies like Skeleton of Thought, where the high level actions were not representative of the actual task at times, 3)  freeform thoughts and actions, unlike ReAct which has a structural constraint, will improve on GPT-4's ability to more accurately represent and solve coding-related questions. 

## Credits
- Code referenced from the Voyager paper, whose repo can be found [here](https://github.com/MineDojo/Voyager) 
