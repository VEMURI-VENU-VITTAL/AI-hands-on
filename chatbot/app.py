from memory import ConversationMemory
from llm import generate

memory = ConversationMemory()

print("MyGpt Started")

while True:
    user_input = input("\nyou: ")

    if(user_input.lower()=="exit"):
        break

    memory.add_user(user_input)

    response = generate(memory.get_messages())

    print("\n Bot:", response)

    memory.add_assistant(response)