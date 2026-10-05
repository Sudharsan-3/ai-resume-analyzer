JOB_MATCH_SCHEMA = {
    "type": "object",
    "properties": {
        "match_score": {
            "type": "number",
        },
        "matching_skills": {
            "type": "array",
            "items": {"type": "string"},
        },
        "missing_skills": {
            "type": "array",
            "items": {"type": "string"},
        },
        "suggestions": {
            "type": "array",
            "items": {"type": "string"},
        },
        "summary": {
            "type": "string",
        },
    },
    "required": [
        "match_score",
        "matching_skills",
        "missing_skills",
        "suggestions",
        "summary",
    ],
}


RESUME_QUALITY_SCHEMA = {
    "type": "object",
    "properties": {
        "quality_score": {
            "type": "number",
        },
        "strengths": {
            "type": "array",
            "items": {"type": "string"},
        },
        "weaknesses": {
            "type": "array",
            "items": {"type": "string"},
        },
        "improvements": {
            "type": "array",
            "items": {"type": "string"},
        },
        "summary": {
            "type": "string",
        },
    },
    "required": [
        "quality_score",
        "strengths",
        "weaknesses",
        "improvements",
        "summary",
    ],
}


RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "job_match": JOB_MATCH_SCHEMA,
        "resume_quality": RESUME_QUALITY_SCHEMA,
    },
    "required": [
        "job_match",
        "resume_quality",
    ],
}