RESULTS_CSS = """
/* Results page */
.results-header {
padding: 1.5rem 0;
margin-bottom: 1.25rem;
}

.results-eyebrow {
color: #2563eb;
font-size: 0.75rem;
font-weight: 700;
letter-spacing: 0.12em;
margin-bottom: 0.5rem;
}

.results-title {
color: #0f172a;
font-size: 2rem;
font-weight: 700;
line-height: 1.2;
}

.results-subtitle {
color: #64748b;
font-size: 1rem;
margin-top: 0.5rem;
}

.results-section-label {
color: #0f172a;
font-size: 1.25rem;
font-weight: 700;
margin: 1.5rem 0 0.75rem;
}

.score-main,
.analysis-card,
.summary-card,
.suggestion-card {
background: #ffffff;
border: 1px solid #e2e8f0;
border-radius: 14px;
padding: 1.25rem;
box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
}

.score-label {
color: #64748b;
font-size: 0.75rem;
font-weight: 700;
letter-spacing: 0.08em;
}

.score-value {
color: #2563eb;
font-size: 2.75rem;
font-weight: 700;
}

.score-status {
color: #475569;
font-weight: 600;
}

.skill-section {
margin-bottom: 0.75rem;
}

.skill-section-title {
color: #0f172a;
font-weight: 700;
font-size: 1rem;
}

.skill-icon {
color: #2563eb;
margin-right: 0.35rem;
}

.skill-section-count {
color: #64748b;
font-size: 0.8rem;
margin-top: 0.25rem;
}

.skill-tags {
display: flex;
flex-wrap: wrap;
gap: 0.5rem;
}

.skill-tag {
display: inline-block;
background: #eff6ff;
color: #1d4ed8;
border: 1px solid #dbeafe;
border-radius: 999px;
padding: 0.35rem 0.7rem;
font-size: 0.85rem;
overflow-wrap: anywhere;
}

.suggestion-heading,
.summary-heading {
margin: 1.5rem 0 0.75rem;
}

.suggestion-title,
.summary-title {
color: #0f172a;
font-size: 1.25rem;
font-weight: 700;
}

.suggestion-subtitle,
.summary-subtitle {
color: #64748b;
font-size: 0.9rem;
margin-top: 0.25rem;
}

.suggestion-card {
display: flex;
gap: 1rem;
margin-bottom: 0.75rem;
}

.suggestion-number {
color: #2563eb;
font-weight: 700;
font-size: 1.1rem;
}

.suggestion-label {
color: #0f172a;
font-weight: 700;
margin-bottom: 0.25rem;
}

.suggestion-text,
.summary-text {
color: #475569;
line-height: 1.65;
overflow-wrap: anywhere;
}

@media (max-width: 640px) {
.results-title {
font-size: 1.65rem;
}

```
.score-main,
.analysis-card,
.summary-card,
.suggestion-card {
    padding: 1rem;
}

.score-value {
    font-size: 2.2rem;
}
```

}

/* Keep analysis status below the fixed header */
.st-key-analysis_status {
    margin-top: 1rem;
}
.analysis-status-spacer {
    height: 3rem;
}
"""
