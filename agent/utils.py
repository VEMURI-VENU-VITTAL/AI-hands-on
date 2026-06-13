import json
import re
from tools import TOOLS
from memory import ConversationMemory



def parseJson(response):
    matches = re.findall(r"\{[\s\S]*?\}", response)
    if not matches:
        return None
    try:
        return json.loads(matches[-1])
    except:
        return None
    
def actionCaller(action, expression, memory:ConversationMemory):
    toolResponse = None
    if(action is None):
        return 
    if(action=="calculator"):
        if expression is None:
            memory.add_observation(action, "Expression missing")
    if expression is None:
        toolResponse = TOOLS[action]() 
    else:
        toolResponse = TOOLS[action](expression)
    
    memory.add_observation(action, expression)
    memory.add_tool(toolResponse)