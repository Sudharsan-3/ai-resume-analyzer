HEADER_CSS = """
.app-header {
    position: fixed;
    top: 0;
    left: 0;

    width: 100vw;
    height: 68px;

    background: #ffffff;
    border-bottom: 1px solid #e2e8f0;

    display: flex;
    align-items: center;
    justify-content: space-between;

    cursor: pointer;    

    padding: 0 32px;
    box-sizing: border-box;

    z-index: 999999;
}

.header-brand {
    color: #0f172a;

    font-family: "Space Grotesk", sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    letter-spacing: -0.025em;
     text-decoration: none;
}
.header-brand:hover {
    color: #4F46E5;
}

.header-feedback {
    display: flex;
    align-items: center;
    gap: 7px;

    padding: 9px 16px;

    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;

    color: #475569;

    font-family: "Inter", sans-serif;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition:
        background 0.15s ease,
        color 0.15s ease,
        border-color 0.15s ease;
}

.header-feedback:hover {
    background: #f8fafc;
    color: #4f46e5;
    border-color: #c7d2fe;
}


/* Mobile menu is hidden on desktop */

.header-desktop-actions {
    margin-left: auto;
}

.header-menu-toggle,
.header-menu-button,
.header-mobile-menu {
    display: none;
}


/* Mobile slide-down menu */

@media (max-width: 600px) {
    .app-header {
        padding: 0 16px;
    }

    .header-brand {
        font-size: 1.05rem;
    }

    .header-desktop-actions {
        display: none;
    }

    .header-menu-toggle {
        display: block;
        position: absolute;
        width: 1px;
        height: 1px;
        opacity: 0;
    }

    .header-menu-button {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 42px;
        height: 42px;
        margin-left: auto;

        color: #0F172A;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        font-size: 1.3rem;
        cursor: pointer;

        transition:
            background 0.2s ease,
            border-color 0.2s ease;
    }

    .header-menu-button:hover {
        background: #EEF2FF;
        border-color: #C7D2FE;
    }

    .menu-close {
        display: none;
    }

    .header-menu-toggle:checked
    + .header-menu-button .menu-open {
        display: none;
    }

    .header-menu-toggle:checked
    + .header-menu-button .menu-close {
        display: inline;
    }

    /* Full-width panel sliding down over page content */

    .header-mobile-menu {
        display: block;
        position: fixed;
        top: 68px;
        left: 0;
        width: 100vw;
        box-sizing: border-box;

        padding: 16px 20px 20px;
        background: #FFFFFF;
        border-bottom: 1px solid #E2E8F0;
        border-radius: 0 0 16px 16px;
        box-shadow: 0 12px 28px rgb(15 23 42 / 10%);

        z-index: 999998;

        opacity: 0;
        visibility: hidden;
        pointer-events: none;
        transform: translateY(-16px);

        transition:
            transform 0.28s ease,
            opacity 0.22s ease,
            visibility 0.28s ease;
    }

    .header-menu-toggle:checked
    ~ .header-mobile-menu {
        opacity: 1;
        visibility: visible;
        pointer-events: auto;
        transform: translateY(0);
    }

    .header-mobile-feedback {
        display: flex;
        align-items: center;
        gap: 10px;

        width: 100%;
        box-sizing: border-box;
        padding: 15px 16px;

        color: #475569;
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 10px;

        font-family: "Inter", sans-serif;
        font-size: 0.95rem;
        font-weight: 600;
        cursor: pointer;

        transition:
            background 0.2s ease,
            color 0.2s ease,
            border-color 0.2s ease;
    }

    .header-mobile-feedback:hover {
        background: #EEF2FF;
        color: #4F46E5;
        border-color: #C7D2FE;
    }
}

@media (prefers-reduced-motion: reduce) {
    .header-mobile-menu,
    .header-menu-button,
    .header-mobile-feedback {
        transition: none;
    }
}

/* Back button only */

.st-key-header_action {
    position: fixed;
    top: 14px;
    right: 32px;

    z-index: 1000000;
}

.st-key-header_action button {
    min-height: 40px;

    padding: 8px 16px !important;

    background: #ffffff !important;
    color: #475569 !important;

    border: 1px solid #e2e8f0 !important;
    border-radius: 10px !important;

    font-family: "Inter", sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 600 !important;

    box-shadow: none !important;
}

.st-key-header_action button:hover {
    background: #f8fafc !important;
    color: #4f46e5 !important;
    border-color: #c7d2fe !important;
    box-shadow: none !important;
}
"""