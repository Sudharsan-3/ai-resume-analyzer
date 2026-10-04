from errors.ai_errors import ProviderError


JOB_MATCH_FIELDS = {
    "match_score",
    "matching_skills",
    "missing_skills",
    "suggestions",
    "summary",
}

RESUME_QUALITY_FIELDS = {
    "quality_score",
    "strengths",
    "weaknesses",
    "improvements",
    "summary",
}


def validate_job_match(result):
    """Validate a job match analysis response."""

    _validate_fields(result, JOB_MATCH_FIELDS)

    if not isinstance(result["match_score"], (int, float)):
        raise ProviderError(
            "🤖 The AI returned an invalid match score."
        )

    if not 0 <= result["match_score"] <= 100:
        raise ProviderError(
            "🤖 The AI returned an invalid match score."
        )

    _validate_lists(
        result,
        ["matching_skills", "missing_skills", "suggestions"],
    )

    _validate_summary(result)

    return result


def validate_resume_quality(result):
    """Validate a resume quality analysis response."""

    _validate_fields(result, RESUME_QUALITY_FIELDS)

    if not isinstance(result["quality_score"], (int, float)):
        raise ProviderError(
            "🤖 The AI returned an invalid quality score."
        )

    if not 0 <= result["quality_score"] <= 100:
        raise ProviderError(
            "🤖 The AI returned an invalid quality score."
        )

    _validate_lists(
        result,
        ["strengths", "weaknesses", "improvements"],
    )

    _validate_summary(result)

    return result


def _validate_fields(result, required_fields):
    if not isinstance(result, dict):
        raise ProviderError(
            "🤖 The AI returned an unexpected response."
        )

    if not required_fields.issubset(result.keys()):
        raise ProviderError(
            "🤖 The AI response is missing required information."
        )


def _validate_lists(result, fields):
    for field in fields:
        if not isinstance(result[field], list):
            raise ProviderError(
                "🤖 The AI returned invalid analysis data."
            )


def _validate_summary(result):
    if not isinstance(result["summary"], str):
        raise ProviderError(
            "🤖 The AI returned an invalid summary."
        )