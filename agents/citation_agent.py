def format_citations(results):
    citations = "\n\n## Sources\n"

    for idx, item in enumerate(results, start=1):
        citations += f"{idx}. {item['title']}\n{item['url']}\n\n"

    return citations
