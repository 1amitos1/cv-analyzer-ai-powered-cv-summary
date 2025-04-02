def detect_sections(cv_text: str) -> dict:
    """
    Identifies sections (Education, Experience, Skills, etc.) from raw CV text.
    Returns a dict keyed by section name with text content.
    """
    sections = {
        "AllText": cv_text,
        "Education": "",
        "Experience": "",
        "Skills": ""
    }
    # Future: Add logic to parse out actual section content.
    return sections
