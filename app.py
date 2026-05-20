import streamlit as st
import requests

st.set_page_config(page_title="AI Deployment Copilot", layout="wide")

st.title("AI Deployment Copilot")
st.write("Turn a business problem into a GenAI system design blueprint.")

business_problem = st.text_area(
    "Business Problem",
    "Build a customer support assistant that answers questions from policy PDFs and ticket history"
)

industry = st.text_input("Industry", "Energy")
expected_users = st.number_input("Expected Users", min_value=1, value=5000)
latency_requirement = st.selectbox("Latency Requirement", ["low", "medium", "high"])

data_sources_text = st.text_input(
    "Data Sources",
    "Policy PDFs, CRM tickets, Knowledge base articles"
)

if st.button("Generate Architecture Blueprint"):
    payload = {
        "business_problem": business_problem,
        "industry": industry,
        "expected_users": expected_users,
        "latency_requirement": latency_requirement,
        "data_sources": [x.strip() for x in data_sources_text.split(",")]
    }

    with st.spinner("Generating blueprint..."):
        response = requests.post(
            "http://127.0.0.1:8000/generate-blueprint",
            json=payload
        )

    if response.status_code == 200:
        data = response.json()

        st.success("Blueprint generated successfully")

        st.subheader("Problem Summary")
        st.write(data.get("problem_summary"))

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Recommended Architecture")
            st.json(data.get("recommended_architecture"))

            st.subheader("RAG Pipeline")
            st.json(data.get("rag_pipeline"))

        with col2:
            st.subheader("API Integrations")
            st.json(data.get("api_integrations"))

            st.subheader("Workflow Orchestration")
            st.json(data.get("workflow_orchestration"))

        st.subheader("Deployment Plan")
        st.json(data.get("deployment_plan"))

        st.subheader("Cost Estimate")
        st.json(data.get("cost_estimate"))

        st.subheader("Risk Evaluation")
        st.json(data.get("risk_evaluation"))

    else:
        st.error("Something went wrong.")
        st.write(response.text)