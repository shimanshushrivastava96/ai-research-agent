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

Rename `.env.example` to `.env`

```env
GEMINI_API_KEY=your_key
TAVILY_API_KEY=your_key
```

## Deployment

Deploy on Hugging Face Spaces using Gradio SDK.
