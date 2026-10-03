from pypdf import PdfReader


def extract_text(file):
    """Extract text from an uploaded PDF file."""
    reader = PdfReader(file)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages).strip()