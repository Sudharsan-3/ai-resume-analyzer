import streamlit as st


def record_analysis():
    """Record one AI analysis for this session."""
    if "analysis_count" not in st.session_state:
        st.session_state.analysis_count = 0

    st.session_state.analysis_count += 1


def show_usage():
    """Display current session usage."""
    count = st.session_state.get("analysis_count", 0)

    st.caption(f"📊 Session analyses: {count}")