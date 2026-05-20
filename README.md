# AI Deployment Copilot

AI Deployment Copilot is a GenAI system design tool that converts business problems into deployable AI architecture blueprints.

## Simple Explanation

You describe an AI app idea, and this tool creates a blueprint for how to build it.

For example, if the user says:

"I want a chatbot that answers questions from company policy documents."

The tool recommends:

- Architecture
- RAG pipeline
- API integrations
- Workflow steps
- Deployment plan
- Cost estimate
- Risk evaluation

## Tech Stack

- Python
- FastAPI
- OpenAI API
- Pydantic
- Uvicorn

## Features

- Converts business problems into GenAI architecture plans
- Generates RAG pipeline recommendations
- Suggests API integrations
- Provides deployment planning
- Estimates rough monthly cost
- Evaluates hallucination, latency, and scalability risks

## Run Locally

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload