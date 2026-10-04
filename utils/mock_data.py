import json
from pathlib import Path


def load_sample_analysis():
    """Load sample analysis data for UI development."""
    file_path = Path("data/sample_analysis.json")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)