from services.ai_analysis import analyze_resume


class FakeProvider:
    def __init__(self):
        self.call_count = 0

    def generate_json(self, prompt):
        self.call_count += 1

        return {
            "job_match": {
                "match_score": 85,
                "matching_skills": ["Python"],
                "missing_skills": ["Docker"],
                "suggestions": ["Add Docker experience."],
                "summary": "Strong match.",
            },
            "resume_quality": {
                "quality_score": 80,
                "strengths": ["Clear experience"],
                "weaknesses": ["Limited project detail"],
                "improvements": ["Add project metrics."],
                "summary": "Good resume quality.",
            },
        }


def test_analyze_resume_uses_one_ai_request():
    provider = FakeProvider()

    result = analyze_resume(
        provider,
        "Python developer with 3 years of experience.",
        "Looking for a Python developer.",
    )

    assert provider.call_count == 1
    assert result["match_score"] == 85
    assert result["resume_quality"]["quality_score"] == 80
