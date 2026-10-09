import time
import base64
import io

import streamlit as st
from streamlit_local_storage import LocalStorage


RESUME_KEY = "resume_analyzer_resume"
RESUME_NAME_KEY = "resume_analyzer_resume_name"
JOB_KEY = "resume_analyzer_job"


class SavedResume(io.BytesIO):
    """File-like object restored from browser storage."""

    def __init__(self, data, name):
        super().__init__(data)
        self.name = name
        self.type = "application/pdf"


def get_storage():
    """Create the browser storage helper."""
    return LocalStorage()


def save_resume(storage, resume):
    """Save the PDF and filename before rerunning the app."""
    if not resume:
        return

    data = base64.b64encode(resume.getvalue()).decode("utf-8")

    storage.setItem(
        RESUME_KEY,
        data,
        key="save_resume_data",
    )
    storage.setItem(
        RESUME_NAME_KEY,
        resume.name,
        key="save_resume_name",
    )

    # Give the browser time to finish saving before rerunning.
    time.sleep(1.5)


def load_resume(storage):
    """Restore the PDF from browser storage."""
    data = storage.getItem(RESUME_KEY)
    name = storage.getItem(RESUME_NAME_KEY)

    if not data or not name:
        return None

    try:
        return SavedResume(base64.b64decode(data), name)
    except (ValueError, TypeError):
        return None


def save_job_description(storage, description):
    """Save the job description, including an empty value."""
    storage.setItem(
        JOB_KEY,
        description,
        key="save_job_description",
    )


def load_job_description(storage):
    """Restore the saved job description."""
    return storage.getItem(JOB_KEY) or ""


def clear_api_key():
    """Remove the API key from session state."""
    st.session_state.pop("gemini_api_key", None)


def clear_saved_resume(storage):
    """Remove the saved resume safely."""
    storage.eraseItem(
        RESUME_KEY,
        key="erase_resume_data",
    )
    storage.eraseItem(
        RESUME_NAME_KEY,
        key="erase_resume_name",
    )


def clear_saved_job_description(storage):
    """Remove the saved job description safely."""
    storage.eraseItem(
        JOB_KEY,
        key="erase_job_description",
    )


def clear_all_saved_inputs(storage):
    """Remove all saved form inputs safely."""
    clear_saved_resume(storage)
    clear_saved_job_description(storage)