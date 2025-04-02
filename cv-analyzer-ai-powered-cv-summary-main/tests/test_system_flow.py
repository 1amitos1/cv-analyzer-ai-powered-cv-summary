import unittest
import subprocess
import os

class TestSystemFlow(unittest.TestCase):

    def test_full_flow(self):
        # Path to a sample CV PDF in your tests/resources/
        sample_pdf = r'./cv_pdf/CV_Patrick_Gomes_de_Oliveira.pdf'

        cmd = [
            "python", "main.py",
            "--pdf", sample_pdf,
            "--max-words", "100"
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # CLI should exit normally
        self.assertEqual(result.returncode, 0, f"Failed with stderr: {result.stderr}")

        # Check if summary text was printed
        self.assertIn("AI-Powered CV SUMMARY", result.stdout)

if __name__ == "__main__":
    unittest.main()
