from langgraph.graph import END
from utils import extractJson

def router(state):
    last_msg = state["messages"][-1]
    last_msg = last_msg.get("content", r"{}")
    last_msg = extractJson(last_msg)
    action = last_msg.get("action", None)
    if(action is None or "final_answer" in action):
        return END
    return "tool_node"