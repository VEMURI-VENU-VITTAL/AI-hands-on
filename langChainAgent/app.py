from nodes import graph
from msgFormatter import addUserMsg
from memory import state

app = graph.compile()

state = addUserMsg(state, "what is 25*8 and what time it is?")

result = app.invoke(state)

print(result["messages"])