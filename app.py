import streamlit as st

from ai.providers.factory import get_provider

from components.input.api_settings import get_api_settings
from components.input.job_input import get_job_description
from components.input.input_section import show_input_header
from components.input.resume_input import get_resume

from components.analysis.analysis_result import show_analysis

from components.layout.header import show_header

from components.usage.usage import record_analysis, show_usage

from components.styles.styles import apply_styles

from errors.ai_errors import AIError
from errors.messages import get_error_message
from services.ai_analysis import analyze_resume

from utils.pdf_reader import extract_text
from utils.mock_data import load_sample_analysis

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
)

apply_styles()

show_header()

show_input_header()

show_usage()

settings_col, resume_col = st.columns(2)

with settings_col:
    provider_name, api_key = get_api_settings()

with resume_col:
    resume = get_resume()

job_description = get_job_description()

if st.button("🧪 Preview Analysis UI"):
            result = load_sample_analysis()
            show_analysis(result)

if st.button("🚀 Analyze Resume"):
    if not api_key:
        st.warning("Please enter your API key.")
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
                    provider = get_provider(provider_name, api_key)

                    result = analyze_resume(
                        provider,
                        resume_text,
                        job_description,
                    )

                    record_analysis()
                    show_analysis(result)

                except AIError as error:
                    st.error(get_error_message(error))
        