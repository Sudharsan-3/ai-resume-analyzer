import json

import anthropic

from ai.providers.base import AIProvider
from errors.ai_errors import ProviderError


MODEL_NAME = "claude-sonnet-4-5"


class ClaudeProvider(AIProvider):
    """Claude implementation of the AI provider."""

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)

    def generate_json(self, prompt):
        """Generate a structured JSON response using Claude."""

        try:
            response = self.client.messages.create(
                model=MODEL_NAME,
                max_tokens=4096,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            text = response.content[0].text
            return json.loads(text)

        except anthropic.APIError as exc:
            raise ProviderError(
                "Claude API request failed."
            ) from exc

        except json.JSONDecodeError as exc:
            raise ProviderError(
                "Claude returned invalid JSON."
            ) from exc