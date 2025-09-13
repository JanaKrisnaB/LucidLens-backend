import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def summarize_text(text, count, max_length=None, min_length=None):
    if len(text.strip()) == 0:
        return "Input text is empty."
    if count < 10:
        return "Input text too short to summarize."

    # You can guide Gemini with a summarization prompt
    prompt = f"""
    Summarize the following text in a clear and concise way.
    Text: {text}
    """

    response = model.generate_content(prompt)

    return response.text.strip()
