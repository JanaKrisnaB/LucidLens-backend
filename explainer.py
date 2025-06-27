from transformers import pipeline

explainer_pipeline = pipeline("text2text-generation", model="t5-base")

def explain_text(text):
    prompt = f"simplify this so that it is easy to understand: {text}"
    output = explainer_pipeline(prompt, max_length=150, do_sample=False)
    return output[0]["generated_text"]
