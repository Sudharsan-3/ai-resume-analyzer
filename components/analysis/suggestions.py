import streamlit as st


def show_suggestions(suggestions):
    """Display resume improvement suggestions."""

    st.markdown(
        """
        <div class="suggestion-heading">
            <div>
                <div class="suggestion-title">
                    💡 Resume Improvements
                </div>
                <div class="suggestion-subtitle">
                    Practical changes that could strengthen your resume.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for index, suggestion in enumerate(suggestions, start=1):
        st.markdown(
            f"""
            <div class="suggestion-card">
                <div class="suggestion-number">
                    {index:02d}
                </div>
                <div class="suggestion-content">
                    <div class="suggestion-label">
                        Improvement {index}
                    </div>
                    <div class="suggestion-text">
                        {suggestion}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )