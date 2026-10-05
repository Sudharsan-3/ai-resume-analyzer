from ai.features.job_match import get_job_match_instructions
from ai.features.resume_quality import get_resume_quality_instructions
from ai.response_validator import (
    validate_job_match,
    validate_resume_quality,
)


def analyze_resume(
    provider,
    resume_text,
    job_description,
):
    """Run all resume analyses with one AI request."""

    prompt = f"""
Analyze this resume and job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Perform both analyses below.

{get_job_match_instructions()}

{get_resume_quality_instructions()}

Return ONLY valid JSON.
Do not use markdown.
Do not add ```json or any explanation.

Use exactly this structure:

{{
    "job_match": {{
        "match_score": 0,
        "matching_skills": [],
        "missing_skills": [],
        "suggestions": [],
        "summary": ""
    }},
    "resume_quality": {{
        "quality_score": 0,
        "strengths": [],
        "weaknesses": [],
        "improvements": [],
        "summary": ""
    }}
}}

Rules:
- All scores must be numbers from 0 to 100.
- All list fields must contain strings.
- All summaries must be short strings.
"""

    result = provider.generate_json(prompt)

    job_match = validate_job_match(result["job_match"])
    resume_quality = validate_resume_quality(
        result["resume_quality"]
    )

    return {
        **job_match,
        "resume_quality": resume_quality,
    }