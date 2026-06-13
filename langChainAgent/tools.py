def calculator(expression: str):
    return eval(expression)

def get_time(expression=None):
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")


TOOLS_DIR = {
    "calculator":calculator,
    "get_time":get_time
}