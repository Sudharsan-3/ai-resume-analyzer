from ai.providers.base import AIProvider
from ai.providers.gemini import GeminiProvider


def get_provider(provider_name: str, api_key: str) -> AIProvider:
    """Create the selected AI provider."""

    if provider_name == "gemini":
        return GeminiProvider(api_key)

    raise ValueError(
        f"Unsupported AI provider: {provider_name}"
    )