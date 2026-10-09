
import streamlit as st


def show_transition_loader():
    """Show a full-screen loader during page navigation."""
    st.html("""
    <style>
    .transition-loader {
        position: fixed;
        inset: 0;
        z-index: 999999;
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: #F8FAFC;
        color: #0F172A;
        text-align: center;
    }

    .transition-spinner {
        width: 46px;
        height: 46px;
        border: 4px solid #E0E7FF;
        border-top-color: #4F46E5;
        border-radius: 50%;
        animation: transition-spin 0.8s linear infinite;
    }

    .transition-loader h3 {
        margin: 22px 0 6px;
        font-size: 20px;
        font-weight: 700;
    }

    .transition-loader p {
        margin: 0;
        color: #64748B;
        font-size: 14px;
    }

    @keyframes transition-spin {
        to { transform: rotate(360deg); }
    }
    </style>

    <div class="transition-loader">
        <div class="transition-spinner"></div>
        <h3>Preparing your workspace</h3>
        <p>Getting everything ready for your analysis...</p>
    </div>
    """)