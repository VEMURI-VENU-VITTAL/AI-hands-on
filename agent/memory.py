class ConversationMemory:
    def __init__(self):
        self.messages = []

    def add_user(self, text):
        self.messages.append({
            "role":"user",
            "content":text
        })
    
    def add_assistant(self, text):
        self.messages.append({
            "role":"assistant",
            "content": text
        })
    
    def add_observation(self, action, expression):
        self.messages.append({
            "assistant": {"action":action, "expression": expression},
        })

    def add_tool(self, response):
        self.messages.append({
            "Tool": response
        })   

    def get_messages(self):
        return self.messages
