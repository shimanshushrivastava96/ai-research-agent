import os
import gradio as gr

from agents.planner_agent import create_research_plan
from agents.search_agent import search_web
from agents.summarize_agent import summarize_research
from agents.citation_agent import format_citations
from utils.pdf_export import export_pdf
from utils.vector_store import save_research

os.makedirs("reports", exist_ok=True)


def run_research(topic, depth):
    status = "Creating research plan...\n"

    status += "Searching web sources...\n"

    results = search_web(topic, depth)

    combined_content = ""

    for item in results:
        combined_content += item["content"] + "\n\n"

    status += "Generating AI report...\n"

    report = summarize_research(topic, combined_content, depth)

    citations = format_citations(results)

    final_report = f"# AI Research Report\n\n{report}\n\n{citations}"

    save_research(topic, final_report)

    safe_name = topic.replace(" ", "_")
    pdf_path = f"reports/{safe_name}.pdf"

    export_pdf(pdf_path, final_report)

    status += "Research completed successfully"

    return status, final_report, pdf_path


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# AI Research Agent")
    gr.Markdown("Multi-Agent AI Research System using Gemini")

    topic = gr.Textbox(
        label="Research Topic",
        placeholder="Enter your topic here"
    )

    depth = gr.Dropdown(
        choices=["basic", "advanced"],
        value="basic",
        label="Research Depth"
    )

    run_btn = gr.Button("Start Research")

    status_output = gr.Textbox(label="System Status")

    report_output = gr.Markdown(label="Research Report")

    pdf_output = gr.File(label="Download PDF")

    run_btn.click(
        fn=run_research,
        inputs=[topic, depth],
        outputs=[status_output, report_output, pdf_output]
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
