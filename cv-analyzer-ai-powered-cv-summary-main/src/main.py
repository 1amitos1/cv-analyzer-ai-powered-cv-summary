import os
from cli_handler import parse_args
from pdf_parser import parse_pdf
from section_detector import detect_sections
from summarizer import configure_gemini, generate_summary
from output_manager import display_summary

from google import genai as palm


def main():
    args = parse_args()
    #args.pdf="/Users/amit/Desktop/code_main/CV_Analyze/CV_Patrick_Gomes_de_Oliveira.pdf" 
    #args.focus = "leadership"
    #args.max_words=100
    # Configure Gemini with environment variable or fallback
    
    GEMINI_API_KEY= ''


    #api_key = os.getenv("GEMINI_API_KEY", "YOUR_DEFAULT_API_KEY")
    client = configure_gemini(GEMINI_API_KEY)

    # Extract text
    cv_text = parse_pdf(args.pdf)

    # Detect sections
    sections = detect_sections(cv_text)

    # Summarize
    summary = generate_summary(
        sections=sections,
        max_words=args.max_words,
        client = client,
        focus=args.focus
        
    )

    # Output
    display_summary(summary)
    # Optionally, 
    write_summary_to_file(summary)

if __name__ == "__main__":
    main()
