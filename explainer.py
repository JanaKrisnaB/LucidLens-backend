import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def explain_text(text):
    """
    Simplifies/explains the input text using Gemini.
    """
    if len(text.strip()) == 0:
        return "Input text is empty."

    # Build a clear instruction prompt for Gemini
    prompt = f"""
    Simplify the following text so that it is easy to understand:
    {text}
    """
    response = model.generate_content(prompt)
    return response.text.strip()
