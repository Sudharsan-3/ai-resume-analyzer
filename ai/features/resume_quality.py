from ai.providers.base import AIProvider
from ai.response_validator import validate_resume_quality


def analyze_resume_quality(
    provider: AIProvider,
    resume_text,
):
    """Analyze the overall quality of a resume."""

    prompt = f"""
Analyze the quality of this resume.

RESUME:
{resume_text}

Evaluate the resume based only on the information provided.

Return ONLY valid JSON.
Do not use markdown.
Do not add ```json or any explanation.

Use exactly this structure:

{{
    "quality_score": 0,
    "strengths": [],
    "weaknesses": [],
    "improvements": [],
    "summary": ""
}}

Rules:
- quality_score must be a number from 0 to 100.
- strengths must be an array of strings.
- weaknesses must be an array of strings.
- improvements must be an array of strings.
- summary must be a short string.
- Do not invent experience, skills, education, or achievements.
"""

    result = provider.generate_json(prompt)

    return validate_resume_quality(result)