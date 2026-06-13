from tools import TOOLS
from tools import get_current_time, get_user_name, calculator
import re

def agent(query):
    query = query.lower()

    if query.startswith("my name is"):
        name = query.replace("my name is", "").strip()
        TOOLS["save_user_name"](name)
        return f"Nice to meet you {name}"
    if "name" in query:
        return TOOLS["get_user_name"]()
    if "time" in query:
        return TOOLS["get_current_time"]()
    match = re.search(r'(\d+)\s*([\+\-\*/])\s*(\d+)', query)

    if(match):
        a=int(match.group(1))
        op = match.group(2)
        b = int(match.group(3))

        return TOOLS["calculator"](a,b,op)
    return "I don't know."