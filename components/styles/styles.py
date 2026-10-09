
import streamlit as st

from components.styles.base import BASE_CSS
from components.styles.header import HEADER_CSS
from components.styles.results import RESULTS_CSS


def apply_styles():
    """Apply the application's global styles."""

    st.markdown(
        f"<style>{BASE_CSS}{HEADER_CSS}{RESULTS_CSS}</style>",
        unsafe_allow_html=True,
    )