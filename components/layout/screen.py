
import streamlit as st


SCREENS = {
    "welcome": "Welcome",
    "setup": "Setup",
    "analyzing": "Analyzing",
    "job_match": "Job Match",
    "resume_quality": "Resume Quality",
}


def get_screen():
    """Restore the current screen from the URL or session."""

    requested_screen = st.query_params.get("screen")

    if requested_screen in SCREENS:
        st.session_state.screen = requested_screen

    elif "screen" not in st.session_state:
        st.session_state.screen = "welcome"

    current_screen = st.session_state.screen
    st.query_params["screen"] = current_screen

    return current_screen


def set_screen(screen):
    """Update the current screen and its URL."""

    if screen not in SCREENS:
        raise ValueError(f"Unknown screen: {screen}")

    st.session_state.screen = screen
    st.query_params["screen"] = screen
    st.rerun()