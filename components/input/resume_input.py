import streamlit as st


def get_resume():
    """Display resume upload and return the uploaded file."""
    st.markdown("### 📄 Your Resume")

    st.caption(
        "Upload a PDF resume to compare against the job description."
    )

    return st.file_uploader(
        "Upload your resume",
        type=["pdf"],
        help="Upload a text-based PDF resume.",
        label_visibility="collapsed",
    )