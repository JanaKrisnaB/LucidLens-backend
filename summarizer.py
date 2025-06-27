from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, count, max_length=None, min_length=None):
    if len(text.strip()) == 0:
        return "Input text is empty."
    if count < 10:
        return "Input text too short to summarize."

    if not max_length or not min_length:
        max_length = min(60, count)
        min_length = min(20, count // 2)
    max_length = max(max_length, min_length + 10)

    summary = summarizer_pipeline(text, max_length=max_length, min_length=min_length, do_sample=False)[0]["summary_text"]
    return summary
