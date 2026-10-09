
import streamlit as st


def get_api_settings():
    """Display AI provider settings."""

    provider_name = st.selectbox(
        "AI Model",
        ["gemini"],
        format_func=lambda value: "Google Gemini",
        key="ai_provider",
    )

    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        placeholder="Paste your Gemini API key",
        key="gemini_api_key",
        help="Your API key is used to request your resume analysis.",
    )

    return provider_name, api_key