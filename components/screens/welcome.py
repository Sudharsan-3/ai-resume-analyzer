
import streamlit as st

from components.layout.screen import set_screen

from components.layout.transition_loader import show_transition_loader


def show_welcome():
    """Display the Welcome landing page."""

    st.html("""
    <style>
    .welcome-page {
        max-width: 1000px;
        margin: 20px auto 0;
        padding: 24px 12px 12px;
        color: #0F172A;
        animation: welcome-enter 0.55s ease-out both;
    }

    .welcome-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 14px;
        border: 1px solid #C7D2FE;
        border-radius: 999px;
        background: #EEF2FF;
        color: #4338CA;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1px;
    }

    .welcome-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #6366F1;
    }

    .welcome-title {
        max-width: 760px;
        margin: 28px 0 18px;
        font-size: clamp(38px, 6vw, 64px);
        line-height: 1.12;
        letter-spacing: -2px;
        font-weight: 800;
    }

    .welcome-title span {
        color: #4F46E5;
    }

    .welcome-subtitle {
        max-width: 650px;
        color: #475569;
        font-size: 18px;
        line-height: 1.8;
        margin-bottom: 12px;
    }

    .welcome-note {
        color: #64748B;
        font-size: 14px;
        margin-top: 8px;
    }

    .welcome-features {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 16px;
        margin-top: 48px;
    }

    .welcome-card {
        min-height: 155px;
        padding: 22px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 18px;
        transition: transform 0.2s ease,
                    border-color 0.2s ease,
                    box-shadow 0.2s ease;
    }

    .welcome-card:hover {
        transform: translateY(-4px);
        border-color: #C7D2FE;
        box-shadow: 0 12px 28px rgba(79, 70, 229, 0.08);
    }

    .welcome-icon {
        font-size: 25px;
        margin-bottom: 14px;
    }

    .welcome-card h3 {
        color: #0F172A;
        font-size: 16px;
        margin: 0 0 8px;
    }

    .welcome-card p {
        color: #64748B;
        font-size: 13px;
        line-height: 1.7;
        margin: 0;
    }

    @keyframes welcome-enter {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 640px) {
        .welcome-page {
            margin-top: 4px;
            padding-inline: 2px;
        }

        .welcome-title {
            letter-spacing: -1px;
        }

        .welcome-subtitle {
            font-size: 16px;
        }

        .welcome-features {
            grid-template-columns: 1fr;
            margin-top: 32px;
        }

        .welcome-card {
            min-height: auto;
        }
    }
    </style>

    <section class="welcome-page">
        <div class="welcome-badge">
            <span class="welcome-dot"></span>
            AI-POWERED RESUME ANALYSIS
        </div>

        <h1 class="welcome-title">
            Your next opportunity<br>
            starts with a <span>better resume.</span>
        </h1>

        <p class="welcome-subtitle">
            Understand your strengths, discover missing skills,
            and see how well your resume matches the job you want.
            Get practical feedback to help you move forward.
        </p>

        <p class="welcome-note">
             Clear insights. Actionable suggestions. Your next step.
        </p>

        <div class="welcome-features">
            <article class="welcome-card">
                <div class="welcome-icon">🎯</div>
                <h3>Job Match Score</h3>
                <p>Understand how closely your resume aligns with
                the job description.</p>
            </article>

            <article class="welcome-card">
                <div class="welcome-icon">🔍</div>
                <h3>Skills Gap Analysis</h3>
                <p>Identify matching skills and discover which
                important skills may be missing.</p>
            </article>

            <article class="welcome-card">
                <div class="welcome-icon">🚀</div>
                <h3>Actionable Feedback</h3>
                <p>Get practical suggestions to improve your resume
                for the opportunity you're targeting.</p>
            </article>
        </div>
    </section>
    """)

    _, center, _ = st.columns([1, 1.2, 1])

    with center:
        if st.button(
            "Start Your Analysis  →",
            key="start_button",
            use_container_width=True,
            type="primary",
        ):
            st.session_state["setup_transition"] = True
            set_screen("setup")

        st.html("""
    <style>
    .st-key-start_button {
        max-width: 340px;
        margin: 14px auto 0;
    }

    .st-key-start_button button {
        min-height: 52px;
        border-radius: 12px;
        font-weight: 700;
        transition: transform 0.2s ease;
    }

    .st-key-start_button button:hover {
        transform: translateY(-2px);
    }
    </style>
    """)