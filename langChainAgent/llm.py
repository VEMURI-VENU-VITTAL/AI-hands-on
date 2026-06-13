from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM
from msgFormatter import addSystemMsg


MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto")

system_prompt = """
You are an agent.

Available tools:

calculator(expression)
get_time()

Rules:

If a calculation is required output should be like:

{"action":"calculator","expression":"25*18"}

If time is required output should be like:

{"action":"get_time"}

When answering finally, means we got all necessary results:

{"action":"final_answer","response":"..."} 

Output ONLY valid JSON that requires.
You MUST output exactly ONE and only ONE JSON object.
Never output more than one JSON object.
Never concatenate JSON objects.
Never include > or any other characters outside the JSON.
Do not add explanations.
Do not add markdown.
Do not add notes.
"""

def generate(state):
    messages = state["messages"]
    
    if(len(messages)==1):
        state = addSystemMsg(state, system_prompt)

    prompt = tokenizer.apply_chat_template(
        state["messages"],
        tokenize=False,
        add_generation_prompt=True
    )

    print("-----------------------------llm input: \n", prompt)

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
    ).to(model.device)

    outputs = model.generate(
        **inputs, 
        max_new_tokens = 200,
        temperature = 0.7,
        do_sample=True
    )

    generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]

    response = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    )

    return response
