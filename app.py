import streamlit as st

from utils.pdf_reader import extract_text


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
)

st.title("🤖 AI Resume Analyzer")
st.write("Upload your resume to extract and analyze its content.")

resume = st.file_uploader(
    "Upload your resume",
    type=["pdf"],
)

if resume:
    resume_text = extract_text(resume)

    if resume_text:
        st.success("Resume uploaded successfully!")

        with st.expander("View extracted text"):
            st.text(resume_text)
    else:
        st.error("Could not extract text from this PDF.")