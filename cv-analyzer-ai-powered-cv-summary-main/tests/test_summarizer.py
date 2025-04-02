# test_summarizer.py
import unittest
from unittest.mock import patch
import google.generativeai as palm

# Import the functions you're testing
from summarizer import configure_gemini, generate_summary

class TestSummarizer(unittest.TestCase):
    def setUp(self):
        """
        Called before every test method. We configure Gemini with a fake key 
        to avoid real API calls.
        """
        configure_gemini("FAKE_API_KEY")

    @patch('summarizer.palm.generate_text')
    def test_generate_summary_basic(self, mock_generate_text):
        """
        Test if 'generate_summary' returns the mocked LLM result properly.
        """
        # Mock the LLM response
        mock_generate_text.return_value.result = "Mock Summary Response"
        
        # The 'client' argument is None in this example, adjust as needed
        sections = {"AllText": "Sample CV text for testing."}
        summary = generate_summary(client=None, sections=sections, max_words=50)

        # Validate the summary
        self.assertIsNotNone(summary)
        self.assertIn("Mock Summary Response", summary)

        # Ensure the LLM method was called exactly once
        mock_generate_text.assert_called_once()

    @patch('summarizer.palm.generate_text')
    def test_generate_summary_word_limit(self, mock_generate_text):
        """
        Test if 'generate_summary' respects the max_words limit.
        """
        # Return a 60-word string
        mock_generate_text.return_value.result = "word " * 60
        
        sections = {"AllText": "Some CV text."}
        summary = generate_summary(client=None, sections=sections, max_words=10)

        # Check that the summary has been truncated to 10 words plus '...'
        self.assertTrue(summary.endswith("..."))
        self.assertLessEqual(len(summary.split()), 11)

if __name__ == '__main__':
    unittest.main()
