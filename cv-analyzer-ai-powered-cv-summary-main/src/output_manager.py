def display_summary(summary: str):
    """
    Prints the summary to the console.
    """
    print("\n=== AI-Powered CV SUMMARY ===\n")
    print(summary)

def write_summary_to_file(summary: str, filename: str = "summary.txt"):
    """
    Writes the summary to a text file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(summary)
