# evaluator.py
# This file evaluates common production risks for GenAI systems.

def evaluate_risks(latency_requirement: str = "medium"):
    # If the user needs very low latency, risk becomes higher
    latency_risk = "Medium"

    if latency_requirement.lower() == "low":
        latency_risk = "High"
    elif latency_requirement.lower() == "high":
        latency_risk = "Low"

    return {
        "hallucination_risk": {
            "level": "Medium",
            "why_it_matters": "LLMs may generate answers not supported by source documents.",
            "mitigation": [
                "Use retrieval-augmented generation",
                "Add source citations",
                "Apply confidence thresholds",
                "Route uncertain answers to human review"
            ]
        },
        "latency_risk": {
            "level": latency_risk,
            "why_it_matters": "RAG and LLM calls can slow down real-time applications.",
            "mitigation": [
                "Cache frequent queries",
                "Use smaller models for simple tasks",
                "Stream responses",
                "Optimize retrieval top-k"
            ]
        },
        "scalability_risk": {
            "level": "Medium",
            "why_it_matters": "Higher user volume can increase cost, API load, and response delays.",
            "mitigation": [
                "Use autoscaling backend services",
                "Separate ingestion and query workloads",
                "Use managed vector storage",
                "Add queue-based processing for large files"
            ]
        }
    }