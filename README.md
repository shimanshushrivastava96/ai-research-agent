---
title: AI Research Agent
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "5.34.2"
app_file: app.py
pinned: false
---

# AI Research Agent

AI-powered multi-agent research assistant using:
- Google Gemini
- Tavily Search
- ChromaDB
- Gradio

## Features

- Autonomous web research
- AI summarization
- Source citations
- PDF export
- Vector memory
- Multi-agent workflow

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Environment Variables


```env
GEMINI_API_KEY=your_key
TAVILY_API_KEY=your_key
```

## Deployment

Deploy on Hugging Face Spaces using Gradio SDK.


## Architecture

                +-------------------+
                |    User Query     |
                +-------------------+
                          |
                          v
                +-------------------+
                |  Planner Agent    |
                | Creates Research  |
                | Plan & Subtopics  |
                +-------------------+
                          |
                          v
                +-------------------+
                |  Research Agent   |
                | Fetches Real-Time |
                | Web Information   |
                +-------------------+
                          |
                          v
                +-------------------+
                |    Tavily API     |
                | Web Search Engine |
                +-------------------+
                          |
                          v
                +-------------------+
                |     ChromaDB      |
                | Vector Memory DB  |
                +-------------------+
                          |
                          v
                +-------------------+
                | Summarizer Agent  |
                | Generates Final   |
                | Research Report   |
                +-------------------+
                          |
                          v
                +-------------------+
                |   PDF Generator   |
                | Export Research   |
                | Report as PDF     |
                +-------------------+
                          |
                          v
                +-------------------+
                |    Gradio UI      |
                | User Interaction  |
                +-------------------+
```
