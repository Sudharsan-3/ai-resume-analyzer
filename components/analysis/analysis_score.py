import streamlit as st


def show_score(result):
    """Display the resume match score."""

    score = result["match_score"]
    matching = len(result["matching_skills"])
    missing = len(result["missing_skills"])

    if score >= 80:
        status = "Strong match"
    elif score >= 60:
        status = "Good match"
    else:
        status = "Needs improvement"

    left, right = st.columns([1.5, 1])

    with left:
        st.markdown(
            f"""
            <div class="score-main">
                <div class="score-label">RESUME MATCH</div>
                <div class="score-value">{score}%</div>
                <div class="score-status">{status}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        stat_col1, stat_col2 = st.columns(2)

        with stat_col1:
            st.metric("Matched", matching)

        with stat_col2:
            st.metric("To Consider", missing)

    st.progress(score / 100)