import streamlit as st


def get_api_key():
    """Get the user's Gemini API key."""
    st.markdown("### 🔑 AI Settings")

    st.caption(
        "Enter your Gemini API key to run the analysis."
    )

    return st.text_input(
        "Gemini API Key",
        type="password",
        placeholder="Enter your Gemini API key",
        help="Your key is used only for this session.",
        label_visibility="collapsed",
    )