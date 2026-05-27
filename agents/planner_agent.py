from utils.gemini_client import generate_response
from utils.prompts import PLANNER_PROMPT


def create_research_plan(topic):
    prompt = PLANNER_PROMPT.format(topic=topic)
    return generate_response(prompt)
