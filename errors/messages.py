from errors.ai_errors import (
    InvalidAPIKeyError,
    NetworkError,
    ProviderError,
    RateLimitError,
)


ERROR_MESSAGES = {
    InvalidAPIKeyError: (
        "🔑 Your API key appears to be invalid. "
        "Please check it and try again."
    ),
    RateLimitError: (
        "🚦 The AI service is currently busy. "
        "Please wait a moment and try again."
    ),
    ProviderError: (
        "🤖 The AI service is temporarily unavailable. "
        "Please try again shortly."
    ),
    NetworkError: (
        "🌐 We couldn't connect to the AI service. "
        "Please check your internet connection."
    ),
}


def get_error_message(error):
    """Return a friendly message for an application error."""
    for error_type, message in ERROR_MESSAGES.items():
        if isinstance(error, error_type):
            return message

    return "⚠️ Something went wrong. Please try again."