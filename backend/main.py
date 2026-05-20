# main.py
# This is the entry point of our FastAPI app.
# It exposes APIs that users can call to generate GenAI architecture blueprints.

from fastapi import FastAPI
from dotenv import load_dotenv

from schemas import ProjectRequest
from planner import generate_blueprint
from cost_estimator import estimate_cost
from evaluator import evaluate_risks

# Loads environment variables from .env file if present
load_dotenv()

# Creates the FastAPI application
app = FastAPI(
    title="AI Deployment Copilot",
    description="Converts business problems into deployable GenAI architecture blueprints.",
    version="1.0.0"
)


@app.get("/")
def home():
    # Simple health check route
    return {
        "message": "AI Deployment Copilot is running.",
        "docs": "/docs"
    }


@app.post("/generate-blueprint")
def generate_architecture(request: ProjectRequest):
    # Step 1: Generate GenAI architecture blueprint
    blueprint = generate_blueprint(request)

    # Step 2: Estimate rough monthly cost
    cost = estimate_cost(request.expected_users or 1000)

    # Step 3: Evaluate hallucination, latency, and scalability risks
    risks = evaluate_risks(request.latency_requirement or "medium")

    # Step 4: Combine everything into one response
    return {
        **blueprint,
        "cost_estimate": cost,
        "risk_evaluation": risks
    }