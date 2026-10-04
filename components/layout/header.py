import streamlit as st


def show_header():
    """Display the application header."""
    st.markdown(
        """
        <div class="app-header">
            <div class="header-icon">🤖</div>
            <div>
                <div class="header-title">
                    AI Resume Analyzer
                </div>
                <div class="header-subtitle">
                    Understand how your resume aligns with a job.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )