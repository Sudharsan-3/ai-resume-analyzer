import streamlit as st


def apply_styles():
    """Apply the application's visual styling."""
    st.markdown(
        """
        <style>
        /* Page */
        .stApp {
            background: #f8fafc;
        }

        .main .block-container {
            max-width: 1100px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        /* Header */
        .app-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 0.5rem 0 2rem;
        }

        .header-icon {
            width: 52px;
            height: 52px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 14px;
            background: #111827;
            font-size: 1.4rem;
        }

        .header-title {
            font-size: 1.8rem;
            font-weight: 700;
            color: #111827;
            line-height: 1.2;
        }

        .header-subtitle {
            margin-top: 0.3rem;
            color: #64748b;
            font-size: 0.95rem;
        }

        /* Section heading */
        .section-heading {
            margin: 0.5rem 0 1.5rem;
        }

        .section-title {
            font-size: 1.35rem;
            font-weight: 650;
            color: #111827;
        }

        .section-subtitle {
            margin-top: 0.3rem;
            color: #64748b;
            font-size: 0.9rem;
        }

                /* Results header */
        .results-header {
            padding: 1.5rem 0 1.25rem;
            border-bottom: 1px solid #e2e8f0;
            margin-bottom: 1.5rem;
        }

        .results-eyebrow {
            color: #64748b;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            margin-bottom: 0.35rem;
        }

        .results-title {
            color: #0f172a;
            font-size: 2rem;
            font-weight: 750;
            line-height: 1.15;
        }

        .results-subtitle {
            color: #64748b;
            font-size: 0.92rem;
            margin-top: 0.45rem;
            max-width: 620px;
        }

        .results-section-label {
            color: #0f172a;
            font-size: 1rem;
            font-weight: 650;
            margin: 1.5rem 0 1rem;
        }

        /* Analysis cards */
        
        .analysis-card {
            padding: 1.5rem;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            background: #ffffff;
            margin-bottom: 1rem;
            box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
        }

                /* Score */
        .score-main {
            padding: 0.5rem 0;
        }

        .score-label {
            color: #64748b;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.1em;
        }

        .score-value {
            color: #0f172a;
            font-size: 3.5rem;
            font-weight: 750;
            line-height: 1;
            margin: 0.4rem 0 0.35rem;
        }

        .score-status {
            color: #475569;
            font-size: 0.85rem;
            font-weight: 600;
        }

        [data-testid="stMetric"] {
            padding: 1rem;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            background: #ffffff;
        }

        [data-testid="stMetricLabel"] {
            color: #64748b;
        }

        [data-testid="stMetricValue"] {
            color: #0f172a;
        }

        .stProgress {
            margin-top: 0.75rem;
        }

        /* Skill tags */
        .skill-tag {
            display: inline-block;
            padding: 0.4rem 0.75rem;
            margin: 0.2rem;
            border-radius: 999px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            color: #334155;
            font-size: 0.85rem;
            font-weight: 500;
        }

        .skill-heading {
            margin-bottom: 0.75rem;
            font-size: 1.05rem;
            font-weight: 650;
            color: #111827;
        }

                /* Skills */
        .skill-section {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.7rem;
        }

        .skill-section-title {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: #0f172a;
            font-size: 1rem;
            font-weight: 650;
        }

        .skill-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 26px;
            height: 26px;
            border-radius: 8px;
            background: #f1f5f9;
            color: #334155;
            font-size: 0.85rem;
            font-weight: 700;
        }

        .skill-section-count {
            color: #94a3b8;
            font-size: 0.75rem;
        }

        .skill-card {
            min-height: 105px;
            padding: 1.25rem;
        }

        .skill-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.45rem;
        }

        .skill-tag {
            display: inline-flex;
            align-items: center;
            padding: 0.45rem 0.7rem;
            margin: 0;
            border-radius: 8px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            color: #334155;
            font-size: 0.82rem;
            font-weight: 500;
            transition: all 0.15s ease;
        }

        .skill-tag:hover {
            border-color: #cbd5e1;
            background: #f1f5f9;
        }

        .empty-skills {
            color: #94a3b8;
            font-size: 0.85rem;
        }

        /* Suggestions */
    
        .suggestion-heading {
            margin: 2rem 0 1rem;
        }

        .suggestion-title {
            color: #0f172a;
            font-size: 1.1rem;
            font-weight: 650;
        }

        .suggestion-subtitle {
            margin-top: 0.3rem;
            color: #64748b;
            font-size: 0.9rem;
        }

        .suggestion-card {
            display: flex;
            align-items: flex-start;
            gap: 1rem;
            padding: 1.1rem 1.2rem;
            margin-bottom: 0.7rem;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            background: #ffffff;
            box-shadow: 0 3px 10px rgba(15, 23, 42, 0.03);
        }

        .suggestion-number {
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 32px;
            height: 32px;
            border-radius: 9px;
            background: #f1f5f9;
            color: #475569;
            font-size: 0.72rem;
            font-weight: 700;
        }

        .suggestion-content {
            flex: 1;
        }

        .suggestion-label {
            margin-bottom: 0.25rem;
            color: #94a3b8;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        .suggestion-text {
            color: #334155;
            font-size: 0.9rem;
            line-height: 1.6;
        }

        /* Summary */
                /* Summary */
        .summary-heading {
            margin: 2rem 0 1rem;
        }

        .summary-title {
            color: #0f172a;
            font-size: 1.1rem;
            font-weight: 650;
        }

        .summary-subtitle {
            margin-top: 0.3rem;
            color: #64748b;
            font-size: 0.9rem;
        }

        .summary-card {
            padding: 1.4rem 1.5rem;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            background: #ffffff;
            box-shadow: 0 3px 10px rgba(15, 23, 42, 0.03);
        }

        .summary-text {
            color: #334155;
            font-size: 0.93rem;
            line-height: 1.75;
        }

        /* Buttons */
        .stButton > button {
            min-height: 44px;
            padding: 0.5rem 1.5rem;
            border-radius: 10px;
            border: 1px solid #111827;
            background: #111827;
            color: white !important;
            font-weight: 600;
            transition: all 0.2s ease;
        }

        .stButton > button p {
            color: white !important;
        }

        .stButton > button:hover {
            background: #1f2937;
            border-color: #1f2937;
        }

        .stButton > button:hover p {
            color: white !important;
        }

        /* File uploader */
        [data-testid="stFileUploader"] {
            border-radius: 12px;
        }

        /* Mobile */
        @media (max-width: 768px) {
            .main .block-container {
                padding: 1rem;
            }

            .header-title {
                font-size: 1.5rem;
            }

            .header-subtitle {
                font-size: 0.85rem;
            }

            .analysis-card {
                padding: 1.2rem;
            }

            .score-value {
                font-size: 2.5rem;
            }

            .score-card {
                align-items: flex-start;
                flex-direction: column;
                gap: 1.25rem;
            }

            .score-divider {
                width: 100%;
                height: 1px;
            }

            .score-stats {
                width: 100%;
                justify-content: space-between;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )