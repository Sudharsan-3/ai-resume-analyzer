from abc import ABC, abstractmethod


class AIProvider(ABC):
    """Base interface for AI providers."""

    @abstractmethod
    def generate_json(self, prompt):
        """Generate a JSON response from a prompt."""
        raise NotImplementedError