
def addUserMsg(state, msg):
    state["messages"].append({
        "role":"user", "content":msg
    }) 

    return state

def addSystemMsg(state, msg):
    state["messages"].insert(0,{
        "role":"system", "content":msg
    })

    return state

def addAgentMsg(state, msg):
    state["messages"].append({
        "role":"assistant", "content":msg
    })

    return state

def addObservation(state, msg):
    state["messages"].append({
        "role":"assistant", "content":msg
    })

    return state