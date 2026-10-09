import streamlit as st
import time
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
from components.layout.transition_loader import show_transition_loader

from components.styles.styles import apply_styles


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
)



apply_styles()


screen = get_screen()

show_header()


if screen == "welcome":
    show_welcome()


elif screen == "setup":
    if st.session_state.get("setup_transition", False):
        show_transition_loader()

        time.sleep(2)

        st.session_state["setup_transition"] = False
        st.rerun()
    else:
        show_setup()

elif screen == "analyzing":
    status_now = st.session_state.get(
        "analysis_status", "pending"
    )
    data = st.session_state.get("analysis_data")

    if status_now == "running":
        st.session_state.analysis_status = "interrupted"
        st.warning(
            "The analysis may have been interrupted by a refresh. "
            "To avoid duplicate API requests, it will not restart automatically."
        )
        st.info(
            "If the result was not saved, return to Setup "
            "to start a new analysis."
        )

        if st.button("← Back to Setup"):
            set_screen("setup")

    elif status_now == "interrupted":
        st.warning(
            "This analysis was interrupted. Its result may not be available."
        )
        if st.button("← Back to Setup"):
            set_screen("setup")

    elif status_now == "complete":
        if "analysis_result" in st.session_state:
            set_screen("job_match")
        else:
            st.warning(
                "The completed result is unavailable in this session."
            )
            if st.button("← Back to Setup"):
                set_screen("setup")

    elif not data:
        # Session data was lost, so we cannot safely repeat the request.
        st.session_state.analysis_status = "interrupted"
        st.warning(
            "Your analysis session data is missing, possibly because "
            "the page was refreshed. The analysis cannot safely resume."
        )
        if st.button("← Back to Setup"):
            set_screen("setup")

    elif status_now == "pending":
        result = None
        error_message = None
        st.session_state.analysis_status = "running"

        st.markdown(
            '<div class="analysis-status-spacer"></div>',
            unsafe_allow_html=True,
        )

        with st.status(
            "Analyzing your resume...",
            expanded=True,
            state="running",
        ) as status:
            st.write("Reading your resume...")
            resume_text = extract_text(data["resume"])

            if not resume_text:
                error_message = "Could not extract text from this PDF."
            else:
                try:
                    st.write(
                        "Comparing your skills with the job description..."
                    )
                    provider = get_provider(
                        data["provider_name"],
                        data["api_key"],
                    )
                    result = analyze_resume(
                        provider,
                        resume_text,
                        data["job_description"],
                    )
                except AIError as error:
                    error_message = get_error_message(error)
                except Exception:
                    error_message = (
                        "The AI service is temporarily unavailable. "
                        "Please try again."
                    )

            if error_message:
                status.update(
                    label="Analysis could not be completed",
                    state="error",
                    expanded=False,
                )
            else:
                status.update(
                    label="Analysis completed!",
                    state="complete",
                    expanded=False,
                )

        if error_message:
            st.session_state.analysis_status = "failed"
            st.error(error_message)
            if st.button("← Back to Setup"):
                set_screen("setup")
        else:
            st.session_state.analysis_result = result
            st.session_state.analysis_status = "complete"
            record_analysis()
            set_screen("job_match")

    else:
        st.warning("Please start a new analysis from Setup.")
        if st.button("← Back to Setup"):
            set_screen("setup")

elif screen == "job_match":
    show_analysis(st.session_state.analysis_result)