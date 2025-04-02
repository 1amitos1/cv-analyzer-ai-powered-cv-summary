## Phase 3: Design

In this phase, we refine our architecture through a **Class-Responsibility-Collaborator (CRC)** outline and simple design diagrams. The goal is to ensure each component is well-defined and easy to maintain before coding.

---

### 1. High-Level Design Approach

We follow **XP’s principle of simple design**:
- **Keep classes small** and focused on a single responsibility.
- **Minimize dependencies** between classes.
- **Favor clarity** over premature optimization.

---

### 2. CRC Cards

Below is a CRC (Class-Responsibility-Collaborator) description for our key classes. These classes are tentatively located in the `src/` folder (or as makes sense in your project structure).

| **Class**        | **Responsibilities**                                                                                                                                                              | **Collaborators**                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| `CLIHandler`     | - Parse command-line arguments (PDF path, max words, focus)<br>- Validate user input (e.g., check if file exists)<br>- Initiate main application flow                                                                   | - `PDFParser`<br>- `Summarizer`                            |
| `PDFParser`      | - Extract text from the given PDF<br>- Preprocess text (basic cleaning, splitting)                                                                                                                                     | - `CLIHandler`<br>- `Summarizer`                           |
| `Summarizer`     | - Interface with **Gemini** (google-generativeai library)<br>- Construct prompt based on user focus and max-words<br>- Return generated summary text                                                                    | - `CLIHandler`<br>- `PDFParser` (for raw CV text)          |
| `SectionDetector`| - Identify major sections in the raw PDF text (Education, Experience, Skills, etc.)<br>- Provide structured data (e.g., dictionary of section_name → text_content)                                                     | - `PDFParser`<br>- `Summarizer` (can refine prompts or pass structured data) |
| `OutputManager`  | - Print final summary to terminal<br>- (Optional) Write summary to a text file if the user desires                                                                                                                     | - `Summarizer`<br>- `CLIHandler`                           |

---

### 3. Sequence Diagram 

A rough outline of how the system components interact:

1. **User** runs `python main.py --pdf resume.pdf --max-words 100`.
2. **CLIHandler**:
   1. Parses args (pdf path, max_words).
   2. Calls **PDFParser** to extract text.
3. **PDFParser**:
   1. Reads and cleans PDF text.
   2. Passes raw text to **SectionDetector**.
4. **SectionDetector**:
   1. Identifies sections (Education, Experience, etc.).
   2. Returns structured text segments back to CLIHandler (or directly to Summarizer).
5. **CLIHandler** calls **Summarizer**, passing:
   - Extracted text or structured sections.
   - Max words, any focus keyword.
6. **Summarizer**:
   1. Sends prompt to Gemini LLM API.
   2. Receives summary text.
   3. Returns summary to CLIHandler.
7. **CLIHandler** calls **OutputManager** to display the summary.
8. **OutputManager**:
   1. Prints summary to console.
   2. (Optional) Writes summary to a file if desired.

**sequenceDiagram:
**

-participant U as User

-participant CLI as CLIHandler

-participant PDF as PDFParser

-participant SD as SectionDetector

-participant SUM as Summarizer

-participant OM as OutputManager
```

Sequence Diagram (ASCII Representation)

 User                       CLIHandler                 PDFParser                  SectionDetector             Summarizer                OutputManager
  | (1) python main.py        |                           |                           |                           |                            |
  | --pdf resume.pdf          |                           |                           |                           |                            |
  | --max-words 100           |                           |                           |                           |                            |
  |-------------------------->|                           |                           |                           |                            |
  |                           | (2) Parse CLI arguments    |                           |                           |                            |
  |                           |--------------------------->|                           |                           |                            |
  |                           |                           | (3) Read & clean PDF      |                           |                            |
  |                           |                           |-------------------------->|                           |                            |
  |                           |                           |                           | (4) Identify sections     |                            |
  |                           |                           |                           |-------------------------->|                            |
  |                           |                           |                           |                           | (5) Send prompt to Gemini  |
  |                           |                           |                           |                           |--------------------------->|
  |                           |                           |                           |                           | (6) Receive summary text   |
  |                           |                           |                           |                           |<---------------------------|
  |                           | (7) Return summary         |                           |                           |                            |
  |                           |<---------------------------|                           |                           |                            |
  |                           |                           |                           |                           | (8) Summarizer → CLIHandler|
  |                           |                           |                           |                           |--------------------------->|
  |                           |                           |                           |                           | (9) Pass summary to Output |
  |                           |------------------------------------------------------->|                            |
  |                           |                           |                           |                           |                            |
  |                           |                           |                           |                           | (10) Print summary         |
  |                           |                           |                           |                           | (Optional: write to file) |
  |                           |                           |                           |                           |                            |
  |                           |----------------------------> [End of flow]           |                           |                            |
  | (Done)                    |                           |                           |                           |                            |






---
```

### 4. Design Considerations

1. **Error Handling**  
   - The `CLIHandler` must catch invalid arguments (e.g., missing PDF) and provide clear error messages.  
   - The `PDFParser` should handle unreadable or corrupt PDFs gracefully, possibly returning partial text or a structured error.

2. **Extensibility**  
   - `SectionDetector` could be enhanced with more complex NLP or pattern recognition.  
   - `Summarizer` logic can add advanced prompt engineering or fallback strategies if Gemini is unreachable.

3. **Testing**  
   - Each class should have unit tests (e.g., `test_pdf_parser.py`, `test_summarizer.py`).  
   - System-level tests ensure the end-to-end flow works as expected.

---

### 5. LLM Interactions

All design-related conversations with the LLM are recorded in:
- [Phase 3 LLM Chat Transcript](./chats/phase3_llm_chat.txt)

---

