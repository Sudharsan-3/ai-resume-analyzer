import streamlit as st
from components.screens.setup import show_setup
from ai.providers.factory import get_provider
from components.analysis.analysis_result import show_analysis
from components.input.api_settings import get_api_settings
from components.input.job_input import get_job_description
from components.input.resume_input import get_resume
from components.layout.header import show_header
from components.layout.screen import get_screen, set_screen
from components.screens.welcome import show_welcome
from components.layout.loader import show_loader
from components.usage.usage import record_analysis, show_usage
from errors.ai_errors import AIError
from errors.messages import get_error_message
from services.ai_analysis import analyze_resume
from utils.pdf_reader import extract_text

from components.styles.styles import apply_styles


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
)



apply_styles()

if st.query_params.get("home") == "1":
    st.session_state.screen = "welcome"
    del st.query_params["home"]

screen = get_screen()

show_header()


if screen == "welcome":
    show_welcome()

elif screen == "setup":
    show_setup()

elif screen == "analyzing":
    show_loader(
    title="Analyzing your resume",
    description=(
        "Comparing your experience with the job description."
    ),
)

    data = st.session_state.analysis_data
    resume_text = extract_text(data["resume"])

    if not resume_text:
        st.error("Could not extract text from this PDF.")
        if st.button("← Back"):
            set_screen("setup")
    else:
        try:
            provider = get_provider(
                data["provider_name"],
                data["api_key"],
            )

            result = analyze_resume(
                provider,
                resume_text,
                data["job_description"],
            )

            record_analysis()
            st.session_state.analysis_result = result
            set_screen("job_match")

        except AIError as error:
            st.error(get_error_message(error))

            if st.button("← Back to Setup"):
                set_screen("setup")


elif screen == "job_match":
    show_analysis(st.session_state.analysis_result)