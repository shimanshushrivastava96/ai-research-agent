PLANNER_PROMPT = """
You are an AI research planner.
Break the user's topic into multiple research tasks.

Topic:
{topic}
"""

SUMMARY_PROMPT = """
Create a detailed research report.

Topic:
{topic}

Content:
{content}

Depth:
{depth}

Include:
- Introduction
- Key Findings
- Technical Insights
- Challenges
- Future Scope
- Conclusion
"""
