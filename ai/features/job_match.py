from ai.providers.base import AIProvider
from ai.response_validator import validate_job_match


def analyze_job_match(
    provider: AIProvider,
    resume_text,
    job_description,
):
    """Analyze a resume against a job description."""

    prompt = f"""
Analyze this resume against the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return ONLY valid JSON.
Do not use markdown.
Do not add ```json or any explanation.

Use exactly this structure:

{{
    "match_score": 0,
    "matching_skills": [],
    "missing_skills": [],
    "suggestions": [],
    "summary": ""
}}

Rules:
- match_score must be a number from 0 to 100.
- matching_skills must be an array of strings.
- missing_skills must be an array of strings.
- suggestions must be an array of strings.
- summary must be a short string.
"""

    result = provider.generate_json(prompt)

    return validate_job_match(result)