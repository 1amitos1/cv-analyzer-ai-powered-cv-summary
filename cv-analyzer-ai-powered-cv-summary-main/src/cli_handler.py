import argparse

def parse_args():
    """
    Parses command-line arguments for CV Analyzer.
    Returns:
        argparse.Namespace with pdf, max_words, focus, etc.
    """
    parser = argparse.ArgumentParser(
        description="Analyze a PDF CV and generate an AI-powered summary."
    )
    parser.add_argument("--pdf", required=True, help="Path to the PDF file.")
    parser.add_argument("--max-words", type=int, default=100, help="Max words in the summary.")

    parser.add_argument("--focus", type=str, default=None,
                        help="Optional focus area for the summary.")
    return parser.parse_args()


