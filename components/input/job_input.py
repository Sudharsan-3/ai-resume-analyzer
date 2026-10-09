
import streamlit as st


def get_job_description():
    """Collect the target job description."""

    return st.text_area(
        "Paste the job description",
        placeholder=(
            "Paste the job description here...\n\n"
            "Include responsibilities, required skills, "
            "qualifications, and experience."
        ),
        height=220,
        key="job_description",
    )