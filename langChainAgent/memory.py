from typing import TypedDict, List
state = {
    "messages":[]
}
class AgentState(TypedDict):
    messages: List[dict]
