from ai.features.job_match import analyze_job_match
from ai.features.resume_quality import analyze_resume_quality


def analyze_resume(
    provider,
    resume_text,
    job_description,
):
    """Run all resume analyses using the selected AI provider."""

    job_match = analyze_job_match(
        provider,
        resume_text,
        job_description,
    )

    resume_quality = analyze_resume_quality(
        provider,
        resume_text,
    )

    return {
    **job_match,
    "resume_quality": resume_quality,
}