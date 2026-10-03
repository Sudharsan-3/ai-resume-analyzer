import streamlit as st


def get_api_key():
    """Get the user's Gemini API key."""
    st.subheader("🔑 AI Settings")

    return st.text_input(
        "Gemini API Key",
        type="password",
        placeholder="Enter your Gemini API key",
        help="Your key is used only for this session.",
    )