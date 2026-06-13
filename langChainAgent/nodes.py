from llm import generate
from tools import TOOLS_DIR
from langgraph.graph import StateGraph
from router import router
from memory import AgentState
from msgFormatter import addAgentMsg, addObservation
from utils import extractJson

def llm_node(state):
    response = generate(state)

    state = addAgentMsg(state, response)

    return state

def tool_node(state):
    last_msg = state["messages"][-1]
    last_msg = last_msg["content"]

    last_msg = extractJson(last_msg)

    action = last_msg["action"]
    expression = last_msg.get("expression", None)
    result = TOOLS_DIR[action](expression)
    state = addObservation(state, f"tool:{action}, results: {result}")
    return state



#Build Graph
graph = StateGraph(AgentState)
graph.add_node("llm_node", llm_node)
graph.add_node("tool_node", tool_node)

graph.set_entry_point("llm_node")
graph.add_conditional_edges(
    "llm_node",
    router,
    {
        "tool_node":"tool_node",
        "llm_node":"llm_node",
        "__end__":"__end__"
    }
)

graph.add_edge("tool_node", "llm_node")
    