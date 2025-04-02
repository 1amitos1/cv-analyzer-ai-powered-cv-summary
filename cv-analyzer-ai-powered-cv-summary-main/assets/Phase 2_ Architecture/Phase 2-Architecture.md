## Phase 2: Architecture

In this phase, we define how the system is structured and how the user interacts with it. We cover the **command-line interface**, **file system interactions**, **third-party libraries**, and **team responsibilities**. We also include references to the relevant LLM interaction logs.

---

### 1. Command-Line Interface Specification

| **CLI Option**           | **Description**                                                                        | **Example**                                       |
|--------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------|
| `--pdf <file_path>`      | **Required.** Path to the PDF CV you want to analyze.                                  | `python main.py --pdf my_resume.pdf`             |
| `--max-words <integer>`  | **Optional.** Caps the word count of the Gemini-generated summary (default 100 words). | `python main.py --pdf my_resume.pdf --max-words 80` |
| `--focus <keyword>`      | **Optional.** Guides Gemini to emphasize specific topics (e.g., “leadership”).         | `python main.py --pdf my_resume.pdf --focus leadership` |

**Flow**:
1. **Parse CLI arguments** (validate PDF path, set defaults if optional flags aren’t provided).
2. **Extract text** from the PDF.
3. **Identify sections** (heuristic or keyword-based).
4. **Send text to Gemini** (with optional focus, word-limit constraints).
5. **Print** summary to console (and optionally save to file).



![CV Analyzer Flowchart](image/CV_Analyzer_Flowchart_v1.png "Flowchart showing the overall CV Analyzer process")




---

### 2. File System Interactions

1. **Input**  
   - **PDF File**: Read from user-specified path (`--pdf`).
   - **Credentials**: Load Gemini API key from a **`.env`** file or environment variable to avoid hard-coding sensitive info.
   
2. **Output**  
   - **Terminal Output**: Print the CV summary directly to the command line.
   - **Optional Text File**: If specified in future enhancements, write the summary to something like `summary.txt`.

**Directory Structure (Proposed)**:
CV_Analyzer/ ├── main.py # Entry point for CLI ├── requirements.txt # Dependencies ├── README.md # Documentation ├── .env # Gemini API key (not committed) ├── src/ │ ├── pdf_parser.py # PDF parsing utilities │ ├── summarizer.py # Gemini LLM integration │ └── cli.py # Argument parsing └── chats/ └── phase2_llm_chat.txt # LLM logs for Architecture decisions




### 3. Third-Party Libraries

| **Library**            | **Purpose**                                  | **Notes**                                          |
|------------------------|----------------------------------------------|----------------------------------------------------|
| `PyPDF2` (or similar)  | Extract text from PDFs                      | Allows reading multi-page PDFs, though advanced formatting may require additional solutions. |
| `google-generativeai`  | Interface with Gemini LLM for text generation | Must securely configure API key.                   |
| `python-dotenv`        | Manage environment variables (.env)         | Helps load Gemini credentials at runtime.          |
| `argparse` or `click`  | Parse command-line arguments                | Provides user-friendly CLI.                        |

If additional Python libraries are needed for logging, error handling, or testing (e.g., `pytest`), they should be listed in `requirements.txt`.




---

### 4. Team Member Responsibilities

| **Member**   | **Main Responsibilities**                                      |
|--------------|----------------------------------------------------------------|
| Amit        | *CLI & Arg Parsing, Setting up environment*                    |
| Erez         | *PDF Parsing logic, PDF text extraction*                       |
| Amit        | *Gemini Summarization integration, Prompt engineering*         |
| Erez         | *Testing and QA (unit tests, system-level tests, CI/CD setup)* |



---

### 5. LLM Interactions

For detailed discussions and prompt engineering choices regarding this architecture:

- [Phase 2 LLM Chat Transcript](./chats/phase2_llm_chat.txt)




