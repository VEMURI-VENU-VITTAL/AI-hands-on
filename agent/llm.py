from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM


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

When answering finally:

{"action":"final_answer","response":"..."} 

Output ONLY valid JSON.
Do not add explanations.
Do not add markdown.
Do not add notes.
"""

def generate(messages):
    if(len(messages)==1):
        prompt = system_prompt+prompt

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
    ).to(model.device)

    outputs = model.generate(
        **inputs, 
        max_new_tokens = 200,
        temperature = 0.4,
        do_sample=True
    )

    generated_tokens = outputs[0][inputs[0].shape[1]:]

    response = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    )

    return response
