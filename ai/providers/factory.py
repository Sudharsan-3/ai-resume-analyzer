from ai.providers.base import AIProvider
from ai.providers.gemini import GeminiProvider
from ai.providers.registry import SUPPORTED_PROVIDERS


def get_provider(provider_name: str, api_key: str) -> AIProvider:
    """Create the selected AI provider."""

    if provider_name == "gemini":
        return GeminiProvider(api_key)

    if provider_name not in SUPPORTED_PROVIDERS:
        raise ValueError(
            f"Unsupported AI provider: {provider_name}"
        )

    raise NotImplementedError(
        f"{SUPPORTED_PROVIDERS[provider_name]} provider is not available yet."
    )