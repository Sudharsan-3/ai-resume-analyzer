import streamlit as st

from errors.ai_errors import AIError
from errors.messages import get_error_message

from ai.gemini import analyze_resume
from components.api_settings import get_api_key
from components.job_input import get_job_description
from utils.pdf_reader import extract_text


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
)

st.title("🤖 AI Resume Analyzer")
st.write("Compare your resume with a job description using AI.")


api_key = get_api_key()

resume = st.file_uploader(
    "Upload your resume",
    type=["pdf"],
)

job_description = get_job_description()


if st.button("🚀 Analyze Resume"):
    if not api_key:
        st.warning("Please enter your Gemini API key.")
    elif not resume:
        st.warning("Please upload your resume.")
    elif not job_description.strip():
        st.warning("Please enter a job description.")
    else:
        resume_text = extract_text(resume)

        if not resume_text:
            st.error("Could not extract text from this PDF.")
        else:
            with st.spinner("🤖 AI is analyzing your resume..."):
                try:
                    result = analyze_resume(
                        api_key,
                        resume_text,
                        job_description,
                    )

                    st.subheader("📊 Analysis")
                    st.markdown(result)

                except AIError as error:
                    st.error(get_error_message(error))