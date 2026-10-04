import streamlit as st

from components.analysis.analysis_score import show_score
from components.analysis.skill_section import show_skill_section
from components.analysis.suggestions import show_suggestions


def show_analysis(result):
    """Display the complete resume analysis."""

    st.markdown(
        """
        <div class="results-header">
            <div>
                <div class="results-eyebrow">ANALYSIS COMPLETE</div>
                <div class="results-title">Resume Analysis</div>
                <div class="results-subtitle">
                    See how closely your resume aligns with this role
                    and where you can improve.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    show_score(result)

    st.markdown(
        """
        <div class="results-section-label">
            Skills overview
        </div>
        """,
        unsafe_allow_html=True,
    )

    matching_col, missing_col = st.columns(2)

    with matching_col:
        show_skill_section(
            "Matching Skills",
            result["matching_skills"],
            "✓",
        )

    with missing_col:
        show_skill_section(
            "Skills to Consider",
            result["missing_skills"],
            "+",
        )

    show_suggestions(result["suggestions"])

    st.markdown(
        """
        <div class="summary-heading">
            <div class="summary-title">
                📝 Overall Summary
            </div>
            <div class="summary-subtitle">
                A quick overview of how your resume fits the role.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
    f"""
    <div class="summary-card">
        <div class="summary-text">
            {result["summary"]}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)