from google import genai
from google.genai import errors, types
from google.genai._gaos.lib.compat_errors import AuthenticationError

from errors.ai_errors import (
    AIError,
    InvalidAPIKeyError,
    NetworkError,
    ProviderError,
    RateLimitError,
)


MODEL_NAME = "gemini-3.8-flash"


def analyze_resume(api_key, resume_text, job_description):
    """Analyze a resume against a job description."""

    try:
        client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(
        retry_options=types.HttpRetryOptions(
            attempts=1,
            http_status_codes=[],
        )
    ),
)

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

        interaction = client.interactions.create(
            model=MODEL_NAME,
            input=prompt,
        )
        return interaction.output_text.strip()
    except AuthenticationError as error:
        raise InvalidAPIKeyError(
            "The API key is invalid."
        ) from error

    except errors.ClientError as error:
        status = getattr(error, "status_code", None)

        if status in (400, 401, 403):
            raise InvalidAPIKeyError(
                "The API key is invalid or does not have access."
            ) from error

        if status == 429:
            raise RateLimitError(
                "The AI service is currently busy or rate limited."
            ) from error

        raise ProviderError(
            "The AI provider could not process your request."
        ) from error

    except errors.ServerError as error:
        raise ProviderError(
            "The AI provider is temporarily unavailable."
        ) from error

    except AIError:
        raise

    except Exception as error:
        print("ACTUAL ERROR:", type(error))
        print("ERROR DETAILS:", error)

        raise ProviderError(
            "🤖 The AI service returned an unexpected error."
        ) from error