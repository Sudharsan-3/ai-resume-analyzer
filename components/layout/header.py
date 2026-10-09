
import streamlit as st


def show_header(show_back=False):
    """Display the application header."""

    st.html(
        """
        <div class="app-header">
            <a href="?screen=welcome" class="header-brand">
                AI Resume Analyzer
            </a>

            <div class="header-desktop-actions">
                <div class="header-feedback">
                    <span>💬</span>
                    Feedback
                </div>
            </div>

            <input
                type="checkbox"
                id="header-menu-toggle"
                class="header-menu-toggle"
                aria-label="Toggle menu"
            >

            <label
                for="header-menu-toggle"
                class="header-menu-button"
                aria-label="Toggle menu"
            >
                <span class="menu-open">☰</span>
                <span class="menu-close">✕</span>
            </label>

            <div class="header-mobile-menu">
                <div class="header-mobile-feedback">
                    💬 Feedback
                </div>
            </div>
        </div>
        """
    )