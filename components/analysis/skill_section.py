import streamlit as st


def show_skill_section(title, skills, icon):
    """Display skills as modern tags."""

    st.markdown(
        f"""
        <div class="skill-section">
            <div class="skill-section-title">
                <span class="skill-icon">{icon}</span>
                {title}
            </div>
            <div class="skill-section-count">
                {len(skills)} skills identified
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not skills:
        st.markdown(
            """
            <div class="analysis-card skill-card empty-skills">
                No skills identified.
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    tags = "".join(
        f'<span class="skill-tag">{skill}</span>'
        for skill in skills
    )

    st.markdown(
        f"""
        <div class="analysis-card skill-card">
            <div class="skill-tags">
                {tags}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )