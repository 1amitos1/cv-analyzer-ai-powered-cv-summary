from google import genai as palm


def configure_gemini(api_key: str):
    """
    Configures the Gemini (Google Generative AI) environment with the API key.
    """
    client = palm.Client(api_key=api_key)
    return client



def generate_summary(client, sections: dict, max_words: int = 100, focus: str = None) -> str:
    """
    Generates a concise summary by calling the Gemini LLM.
    Args:
        sections: Dict of section data.
        max_words: Maximum word count for final summary.
        focus: Optional focus area (e.g. 'leadership').
    """
    cv_content = sections.get("AllText", "")
    prompt = (
        f"Summarize the following CV content in under {max_words} words.\n"
        "Focus on key skills, experience, and education.\n\n"
        f"{cv_content}\n"
    )
    if focus:
        prompt += f"\nEmphasize {focus}.\n"

        
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[prompt] ,
    )

    if not response:
        return "No summary available."

    summarized_text = response.text

    # Enforce max words if needed
    words = summarized_text.split()
    if len(words) > max_words:
        summarized_text = " ".join(words[:max_words]) + "..."

    return summarized_text
