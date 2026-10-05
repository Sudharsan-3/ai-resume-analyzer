SUPPORTED_PROVIDERS = {
    "gemini": "Gemini",
    "claude": "Claude",
    "openai": "OpenAI",
}


def get_provider_names():
    """Return the available AI provider names."""
    return list(SUPPORTED_PROVIDERS.keys())


def get_provider_label(provider_name):
    """Return the display label for a provider."""
    return SUPPORTED_PROVIDERS.get(provider_name)