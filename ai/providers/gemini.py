import json

from google import genai
from google.genai import errors, types
from google.genai._gaos.lib.compat_errors import (
    AuthenticationError,
    InternalServerError,
)

from ai.providers.base import AIProvider
from ai.response_schema import RESPONSE_SCHEMA
from errors.ai_errors import (
    InvalidAPIKeyError,
    ProviderError,
    RateLimitError,
)


MODEL_NAME = "gemini-3.8-flash"


class GeminiProvider(AIProvider):
    """Gemini implementation of the AI provider."""

    def __init__(self, api_key):
        self.client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(
                timeout=30000,
                retry_options=types.HttpRetryOptions(
                    attempts=1,
                    http_status_codes=[],
                ),
            ),
        )

    def generate_json(self, prompt):
        """Send a prompt to Gemini and return parsed JSON."""

        try:
            response = self.client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                        response_schema=RESPONSE_SCHEMA,
                    ),
)

            response_text = response.text.strip()

            try:
                return json.loads(response_text)

            except json.JSONDecodeError as error:
                raise ProviderError(
                    "🤖 The AI returned an invalid response."
                ) from error

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

            if status in (429, 503):
                raise RateLimitError(
                    "The AI service is currently busy or rate limited."
                ) from error

            raise ProviderError(
                "The AI provider could not process your request."
            ) from error

        except InternalServerError as error:
            raise ProviderError(
                "The AI provider is temporarily unavailable."
            ) from error

        except Exception as error:
            raise ProviderError(
                "The AI provider encountered an unexpected error."
            ) from error