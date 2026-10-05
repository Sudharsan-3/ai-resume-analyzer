import streamlit as st


def show_resume_quality(result):
    """Display the resume quality analysis."""

    quality = result["resume_quality"]

    st.markdown(
        """
        <div class="results-section-label">
            Resume Quality
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.metric(
        "Quality Score",
        f'{quality["quality_score"]}%',
    )

    st.markdown("### Strengths")

    for strength in quality["strengths"]:
        st.markdown(f"- {strength}")

    st.markdown("### Weaknesses")

    for weakness in quality["weaknesses"]:
        st.markdown(f"- {weakness}")

    st.markdown("### Improvements")

    for improvement in quality["improvements"]:
        st.markdown(f"- {improvement}")

    st.markdown("### Summary")

    st.write(quality["summary"])