import streamlit as st


def get_job_description():
    """Display job description input and return its content."""
    st.subheader("📋 Job Description")

    return st.text_area(
        "Paste the job description here",
        height=250,
        placeholder=(
            "Example:\n"
            "We are looking for a React developer "
            "with experience in Node.js..."
        ),
    )