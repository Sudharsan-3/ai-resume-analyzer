import streamlit as st


def get_job_description():
    """Display job description input and return its content."""
    st.markdown("### 📋 Job Description")

    st.caption(
        "Paste the job description you want to compare your resume against."
    )

    return st.text_area(
        "Paste the job description here",
        height=250,
        placeholder=(
            "Example:\n"
            "We are looking for a React developer "
            "with experience in Node.js..."
        ),
        label_visibility="collapsed",
    )