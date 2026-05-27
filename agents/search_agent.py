from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def search_web(query, depth="basic"):
    response = client.search(
        query=query,
        search_depth=depth,
        max_results=5
    )

    results = []

    for item in response["results"]:
        results.append({
            "title": item.get("title"),
            "content": item.get("content"),
            "url": item.get("url")
        })

    return results
