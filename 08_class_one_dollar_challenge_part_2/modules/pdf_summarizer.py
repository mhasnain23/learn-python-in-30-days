import fitz  # PyMuPDF
import os


class PDFSummarizer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = ""

    def extract_text(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("PDF file not found.")

        doc = fitz.open(self.file_path)
        extracted = []
        for page in doc:
            extracted.append(page.get_text())
        self.text = "\n".join(extracted)
        return self.text

    # This is the summary function for the PDFSummarizer class that uses the basic_summarize method to generate a summary of the extracted text. It takes an optional sentence_count parameter to specify the number of sentences to include in the summary.
    def basic_summarize(self, sentence_count=5):
        if not self.text:
            raise ValueError("No text to summarize.")

        sentences = self.text.split(". ")
        summary = ". ".join(sentences[:sentence_count])
        return summary.strip() + "."
