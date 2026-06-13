from llm import generate
from utils import parseJson
from utils import actionCaller
from memory import ConversationMemory

memory = ConversationMemory()

print("MyGpt Started")

while True:
    user_input = input("\nyou: ")
    if(user_input.lower()=="exit"):
        break
    memory.add_user(user_input)

    while True:
        action = None
        expression = None
        response = None
        
        response = generate(memory.get_messages())

        print("\n Bot:", response)

        jsonOutput = parseJson(response)
        print("json output: ", jsonOutput)
        if(jsonOutput is not None):
            action = jsonOutput.get("action", None)
            expression = jsonOutput.get("expression", None)
            response = jsonOutput.get("response", None)
        if(action=="final_answer"):
            print("response: ", response)
            break
        actionCaller(action, expression, memory)

    