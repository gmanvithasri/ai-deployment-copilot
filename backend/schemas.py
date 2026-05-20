# schemas.py
# This file defines the input structure for the API using Pydantic.

from pydantic import BaseModel
from typing import List, Optional


class ProjectRequest(BaseModel):
    # Business problem entered by the user
    business_problem: str

    # Optional industry context, like healthcare, energy, finance, retail
    industry: Optional[str] = None

    # Approximate number of expected users
    expected_users: Optional[int] = 1000

    # Latency requirement: low, medium, or high
    latency_requirement: Optional[str] = "medium"

    # Data sources needed for the AI system
    data_sources: Optional[List[str]] = []