BASE_CSS = """
@import url(
    'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700'
    '&family=Space+Grotesk:wght@500;600;700&display=swap'
);

.stApp {
    background: #f8fafc;
}

#MainMenu,
[data-testid="stToolbar"],
footer {
    visibility: hidden;
}

.main .block-container {
    max-width: 1180px;
    padding-top: 88px;
    padding-bottom: 2rem;
}
"""