memory = {}
def calculator(a,b,op):
    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return a/b

def save_name(name):
    memory["name"] = name

def get_name():
    return memory.get("name", "Unknown")

def get_time():
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")

#registry
TOOLS = {
    "calculator":calculator,
    "save_name":save_name,
    "get_name":get_name,
    "get_time":get_time
}
