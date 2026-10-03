import streamlit as st

from components.job_input import get_job_description
from utils.pdf_reader import extract_text


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
)

st.title("🤖 AI Resume Analyzer")
st.write("Compare your resume with a job description using AI.")


resume = st.file_uploader(
    "Upload your resume",
    type=["pdf"],
)

job_description = get_job_description()


if resume and job_description:
    resume_text = extract_text(resume)

    if resume_text:
        st.success("Resume and job description are ready!")

        with st.expander("View extracted resume text"):
            st.text(resume_text)
    else:
        st.error("Could not extract text from this PDF.")