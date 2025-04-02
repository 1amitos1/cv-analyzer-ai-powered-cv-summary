** AI-Powered CV Summary: **

**Brief Explanation
**

**AI-Powered CV Summary: 
**

main.py – Orchestrates CLI arguments, PDF parsing, section detection, summarization, and output.
cli_handler.py – Handles command-line arguments.
pdf_parser.py – Extracts text from the PDF.
section_detector.py – Identifies major CV sections (Education, Experience, Skills, etc.).
summarizer.py – Integrates with Gemini to generate concise summaries.
output_manager.py – Handles console printing and optional file output.


| **File Name**                                      | **Description**                                                                 |
|----------------------------------------------------|---------------------------------------------------------------------------------|
| [main.py](./main.py)                               | Entry point. Parses CLI args and orchestrates the entire CV analysis flow.      |
| [cli_handler.py](./src/cli_handler.py)             | Handles command-line arguments (PDF path, max words, focus) for the analyzer.   |
| [pdf_parser.py](./src/pdf_parser.py)               | Extracts text from PDF files using `PyPDF2`.                                    |
| [section_detector.py](./src/section_detector.py)   | Identifies major sections (Education, Experience, etc.) in the CV text.         |
| [summarizer.py](./src/summarizer.py)               | Interfaces with **Gemini** (Google Generative AI) for the AI-powered summary.   |
| [output_manager.py](./src/output_manager.py)       | Prints the summary to console or writes it to a text file.                      |
| [test_unit_summarizer.py](./tests/test_unit_summarizer.py) | Multiple test cases for Summarizer logic.                                    |
| [test_system_flow.py](./tests/test_system_flow.py) | End-to-end test verifying CLI → Summarizer → Output.      