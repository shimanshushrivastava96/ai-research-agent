from utils.gemini_client import generate_response
from utils.prompts import SUMMARY_PROMPT


def summarize_research(topic, content, depth):
    prompt = SUMMARY_PROMPT.format(
        topic=topic,
        content=content,
        depth=depth
    )

    return generate_response(prompt)
