class AIError(Exception):
    """Base error for AI-related problems."""


class InvalidAPIKeyError(AIError):
    """Raised when the API key is invalid."""


class RateLimitError(AIError):
    """Raised when the AI provider is busy or rate limited."""


class ProviderError(AIError):
    """Raised when the AI provider is unavailable."""


class NetworkError(AIError):
    """Raised when the AI request cannot reach the provider."""