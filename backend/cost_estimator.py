# cost_estimator.py
# This file gives a lightweight estimated monthly cost range.
# It is not exact pricing. It is meant for system planning and demo purposes.

def estimate_cost(expected_users: int = 1000):
    # Simple assumption: each user sends around 30 queries per month
    monthly_queries = expected_users * 30

    if monthly_queries < 50000:
        tier = "Low"
        estimate = "$50 - $200/month"
    elif monthly_queries < 500000:
        tier = "Medium"
        estimate = "$300 - $1,500/month"
    else:
        tier = "High"
        estimate = "$2,000+/month"

    return {
        "usage_tier": tier,
        "estimated_monthly_queries": monthly_queries,
        "estimated_monthly_cost": estimate,
        "cost_drivers": [
            "LLM token usage",
            "Embedding generation",
            "Vector database storage",
            "API calls",
            "Monitoring and logging"
        ]
    }