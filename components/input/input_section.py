import streamlit as st


def show_input_header():
    """Display the analysis input section."""
    st.markdown(
        """
        <div class="section-heading">
            <div class="section-title">Prepare your analysis</div>
            <div class="section-subtitle">
                Add your resume and the job description
                you want to compare.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )