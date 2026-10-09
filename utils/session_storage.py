import base64
import streamlit as st


def save_setup_data(resume, job_description):
    """Save resume and job description for the current browser session."""

    if resume:
        resume_data = base64.b64encode(
            resume.getvalue()
        ).decode("utf-8")

        st.session_state.saved_resume = {
            "name": resume.name,
            "data": resume_data,
        }

    st.session_state.saved_job_description = job_description


def load_setup_data():
    """Return previously saved setup data."""

    return (
        st.session_state.get("saved_resume"),
        st.session_state.get(
            "saved_job_description",
            "",
        ),
    )


def clear_api_key():
    """Remove the API key without removing setup data."""

    st.session_state.pop("gemini_api_key", None)