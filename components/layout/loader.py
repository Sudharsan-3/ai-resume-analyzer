
import streamlit as st


def show_loader(
    title="Loading",
    description="Please wait while we prepare everything.",
):
    """Display a reusable animated loader."""

    st.html(
        f"""
        <style>
        .app-loader {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 64px 16px;
        }}

        .app-loader-ring {{
            width: 48px;
            height: 48px;
            border: 4px solid #E0E7FF;
            border-top-color: #4F46E5;
            border-radius: 50%;
            animation: app-loader-spin 0.8s linear infinite;
            margin-bottom: 24px;
        }}

        .app-loader-title {{
            color: #0F172A;
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 8px;
        }}

        .app-loader-description {{
            color: #475569;
            font-size: 15px;
        }}

        @keyframes app-loader-spin {{
            to {{ transform: rotate(360deg); }}
        }}

        @media (prefers-reduced-motion: reduce) {{
            .app-loader-ring {{
                animation-duration: 2s;
            }}
        }}
        </style>

        <div class="app-loader">
            <div class="app-loader-ring"></div>
            <div class="app-loader-title">{title}</div>
            <div class="app-loader-description">{description}</div>
        </div>
        """
    )