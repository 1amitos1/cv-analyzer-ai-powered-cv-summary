# src/pdf_parser.py
import PyPDF2

def parse_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file.
    Args:
        pdf_path (str): The file path to the PDF.
    Returns:
        A string containing all text extracted from the PDF.
    """
    text_chunks = []
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            # Extract text from each page
            page_text = page.extract_text() or ""
            text_chunks.append(page_text.strip())
    return "\n".join(text_chunks)
