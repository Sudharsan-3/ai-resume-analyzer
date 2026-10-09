
import streamlit as st

from components.input.api_settings import get_api_settings
from components.input.job_input import get_job_description
from components.input.resume_input import get_resume
from components.layout.screen import set_screen
from utils.persistence import (
    clear_all_saved_inputs,
    clear_api_key,
    get_storage,
    load_job_description,
    load_resume,
    save_job_description,
    save_resume,
)


@st.dialog("Clear all inputs?")
def confirm_clear_all_dialog():
    st.write(
        "This removes your saved resume, job description, "
        "API key, and previous analysis."
    )

    yes_col, cancel_col = st.columns(2)

    with yes_col:
        if st.button(
            "Yes, clear all",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.perform_clear_all = True
            st.rerun()

    with cancel_col:
        if st.button("Cancel", use_container_width=True):
            st.rerun()

def show_setup():
    """Display the resume analysis setup page."""

    st.html("""
    <style>
    /* Give the page enough room at the top */
    .block-container {
    padding-top: 0.5rem !important;
    padding-bottom: 0.75rem !important;
}

    /* Keep vertical spacing compact */
    div[data-testid="stVerticalBlock"] {
        gap: 0.55rem;
    }

    /* Back button position and appearance */
    .st-key-back_home {
    margin: 0 !important;
    padding: 0 !important;
}

    .st-key-back_home button {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: flex-start !important;

    color: #2563EB !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;

    padding: 3rem 0 0 0 !important;
    min-height: 36px !important;

    font-size: 15px !important;
    font-weight: 600 !important;
}

    .st-key-back_home button:hover {
    color: #1D4ED8 !important;
    background: transparent !important;
}

    /* Page heading */
    .setup-heading {
        color: #0F172A;
        font-size: 30px;
        font-weight: 800;
        letter-spacing: -0.8px;
        margin: 0;
    }

    .setup-subtitle {
        color: #475569;
        font-size: 14px;
        margin-bottom: 8px;
    }

    /* Input cards */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-color: #E2E8F0;
        border-radius: 12px;
        background: #FFFFFF;
    }

    .stTextInput input,
    .stTextArea textarea {
        border-radius: 9px;
        border-color: #E2E8F0;
    }

    /* Buttons */
    .stButton button {
        min-height: 44px;
        border-radius: 10px;
        font-weight: 600;
    }

    /* Resume uploader */
    [data-testid="stFileUploaderDropzone"] {
        padding: 0.35rem 0.5rem !important;
    }

    /* Clear All hover */
    .st-key-clear_all_button button {
        color: #475569;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
    }

    .st-key-clear_all_button button:hover {
        color: #DC2626 !important;
        background: #FEF2F2 !important;
        border-color: #DC2626 !important;
    }
    </style>
    """)

    # Back button comes before the heading.
    if st.button("← Back", key="back_home", type="tertiary"):
        set_screen("welcome")

    st.html("""
    <div class="setup-heading">Prepare your analysis</div>
    <div class="setup-subtitle">
        Add your job details and resume to get personalized AI feedback.
    </div>
    """)

    

    storage = get_storage()

    # Clear data before loading or displaying the form.
    if st.session_state.pop("perform_clear_all", False):
        clear_all_saved_inputs(storage)
        clear_api_key()

        st.session_state["job_description"] = ""
        st.session_state["saved_resume"] = None
        st.session_state["resume_upload_version"] = (
            st.session_state.get("resume_upload_version", 0) + 1
        )

        for key in list(st.session_state.keys()):
            if key.startswith("resume_upload_"):
                st.session_state.pop(key, None)

        for key in (
            "analysis_result",
            "analysis_data",
            "analysis_status",
        ):
            st.session_state.pop(key, None)

        st.session_state["show_validation"] = False

    if "saved_resume" not in st.session_state:
        st.session_state.saved_resume = load_resume(storage)

    if "job_description" not in st.session_state:
        st.session_state.job_description = load_job_description(storage)

    show_validation = st.session_state.get("show_validation", False)

    def field_title(title, missing):
        required = (
            ' <span style="color:#DC2626;font-size:12px">'
            '• Required</span>'
            if show_validation and missing
            else ""
        )
        st.markdown(
            f"### {title}{required}",
            unsafe_allow_html=True,
        )

    api_missing = not st.session_state.get("gemini_api_key", "").strip()

    with st.container(border=True):
        field_title("🔑 AI Provider & API Key", api_missing)
        st.caption("Choose your AI model and enter your API key.")
        get_api_settings()

    left_col, right_col = st.columns(2, gap="small")

    with left_col:
        with st.container(border=True):
            job_missing = not st.session_state["job_description"].strip()
            field_title("📝 Job Description", job_missing)
            st.caption("Paste the job description you're targeting.")
            job_description = get_job_description()

    with right_col:
        with st.container(border=True):
            resume_missing = not st.session_state.saved_resume
            field_title("📄 Your Resume", resume_missing)
            st.caption("Upload a PDF resume.")
            resume = get_resume(st.session_state.saved_resume, storage)

    # Save the selected PDF, then replace the uploader with the saved row.
    if resume and resume is not st.session_state.saved_resume:
        save_resume(storage, resume)
        st.session_state.saved_resume = resume
        st.rerun()

    # Save empty descriptions too, so old descriptions do not return.
    save_job_description(storage, job_description)

    if show_validation:
        red_css = ""

        if not st.session_state.get("gemini_api_key", "").strip():
            red_css += """
            .st-key-gemini_api_key input {
                border: 1px solid #DC2626 !important;
                box-shadow: 0 0 0 1px #DC2626 !important;
            }
            """

        if not job_description.strip():
            red_css += """
            .st-key-job_description textarea {
                border: 1px solid #DC2626 !important;
                box-shadow: 0 0 0 1px #DC2626 !important;
            }
            """

        if not resume:
            red_css += """
            [class*="st-key-resume_upload_"]
            [data-testid="stFileUploaderDropzone"] {
                border: 1px solid #DC2626 !important;
                border-radius: 10px;
            }
            """

        if red_css:
            st.html(f"<style>{red_css}</style>")

    clear_col, analyze_col = st.columns(2, gap="small")

    with clear_col:
        if st.button(
            "Clear All",
            key="clear_all_button",
            use_container_width=True,
        ):
            confirm_clear_all_dialog()

    with analyze_col:
        analyze_clicked = st.button(
            "✨ Analyze Resume →",
            key="analyze_button",
            type="primary",
            use_container_width=True,
        )

    if analyze_clicked:
        st.session_state.show_validation = True

        api_key = st.session_state.get("gemini_api_key", "")
        missing_api = not api_key.strip()
        missing_resume = not resume
        missing_job = not job_description.strip()

        if missing_api or missing_resume or missing_job:
            st.rerun()
        else:
            st.session_state.analysis_data = {
                "provider_name": "gemini",
                "api_key": api_key,
                "resume": resume,
                "job_description": job_description,
            }
            st.session_state.analysis_status = "pending"
            st.session_state.pop("analysis_result", None)
            st.session_state.show_validation = False

            clear_api_key()
            set_screen("analyzing")