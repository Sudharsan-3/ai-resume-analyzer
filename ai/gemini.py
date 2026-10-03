from google import genai
from google import genai
from google.genai import errors
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
        
        client = genai.Client(api_key=api_key)

        prompt = f"""
Analyze this resume against the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return these sections:

MATCH SCORE:
Give a percentage from 0-100.

MATCHING SKILLS:
List skills found in both.

MISSING SKILLS:
List important requirements missing from the resume.

SUGGESTIONS:
Give practical resume improvement suggestions.

SUMMARY:
Give a short overall analysis.
"""

        interaction = client.interactions.create(
            model=MODEL_NAME,
            input=prompt,
        )

        return interaction.output_text
    
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
    # except Exception as error:
    #     raise NetworkError(
    #         "We could not connect to the AI service."
    #     ) from error