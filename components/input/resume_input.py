
import streamlit as st

from utils.persistence import clear_saved_resume


def get_resume(saved_resume=None, storage=None):
    """Show the saved PDF or a fresh uploader."""

    if "resume_upload_version" not in st.session_state:
        st.session_state.resume_upload_version = 0

    if saved_resume:
        file_col, remove_col = st.columns([5, 1])

        with file_col:
            st.markdown("**Resume uploaded**")
            st.caption(saved_resume.name)

        with remove_col:
            if st.button(
                "✕",
                key="remove_saved_resume",
                help="Remove this resume",
                use_container_width=True,
            ):
                if storage:
                    clear_saved_resume(storage)

                st.session_state.saved_resume = None
                st.session_state.resume_upload_version += 1
                saved_resume = None

    if not saved_resume:
        upload_key = (
            f"resume_upload_{st.session_state.resume_upload_version}"
        )

        return st.file_uploader(
            "Upload your resume (PDF)",
            type=["pdf"],
            key=upload_key,
            help="Choose a PDF file containing your resume.",
        )

    return saved_resume