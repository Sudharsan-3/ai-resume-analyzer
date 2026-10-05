import streamlit as st

from ai.providers.registry import SUPPORTED_PROVIDERS


def get_api_settings():
    """Get the selected AI provider and its API key."""

    st.markdown("### 🔑 AI Settings")

    provider_name = st.selectbox(
        "AI Provider",
        options=list(SUPPORTED_PROVIDERS.keys()),
        format_func=lambda name: SUPPORTED_PROVIDERS[name],
    )

    st.caption(
        "Enter your API key to run the analysis."
    )

    api_key = st.text_input(
        f"{SUPPORTED_PROVIDERS[provider_name]} API Key",
        type="password",
        placeholder="Enter your API key",
        help="Your key is used only for this session.",
    )

    return provider_name, api_key