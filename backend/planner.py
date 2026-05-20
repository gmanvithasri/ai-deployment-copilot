# planner.py
# This file generates the GenAI architecture blueprint using Gemini.
# If Gemini fails, it returns a fallback blueprint so the demo still works.

import os
import json
import google.generativeai as genai


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_blueprint(request):
    prompt = f"""
You are an AI solution architect.

Create a practical GenAI system design for this business problem.

Business problem: {request.business_problem}
Industry: {request.industry}
Data sources: {request.data_sources}

Return only valid JSON with these exact keys:
problem_summary,
recommended_architecture,
rag_pipeline,
api_integrations,
workflow_orchestration,
deployment_plan.
"""

    try:
        response = model.generate_content(prompt)
        content = response.text.strip()

        content = content.replace("```json", "").replace("```", "").strip()

        return json.loads(content)

    except Exception:
        return {
            "problem_summary": request.business_problem,
            "recommended_architecture": {
                "frontend": "Simple web interface or Swagger UI",
                "backend": "FastAPI service",
                "llm_layer": "Gemini API for architecture generation",
                "retrieval_layer": "Vector database for semantic search",
                "monitoring": "Track latency, cost, and response quality"
            },
            "rag_pipeline": {
                "ingestion": "Load documents from provided data sources",
                "chunking": "Split documents into smaller semantic chunks",
                "embedding": "Create embeddings for document chunks",
                "retrieval": "Retrieve relevant chunks based on user query",
                "generation": "Generate grounded answer using retrieved context"
            },
            "api_integrations": [
                "Gemini API",
                "Vector database API",
                "CRM or ticketing API",
                "Document storage API"
            ],
            "workflow_orchestration": [
                "Receive business problem",
                "Identify data sources",
                "Design retrieval pipeline",
                "Generate architecture blueprint",
                "Estimate cost and risk",
                "Return deployment plan"
            ],
            "deployment_plan": {
                "local_demo": "Run with FastAPI and Swagger UI",
                "cloud_hosting": "Deploy backend on Render",
                "future_scale": "Add authentication, vector database, monitoring, and CI/CD"
            }
        }