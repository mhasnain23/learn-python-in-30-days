import re
import json


class FlashcardGenerator:
    def __init__(self, text):
        self.text = text
        self.flashcards = []

    def generate_flashcards(self, max_cards=5):
        # Naive method: extract definitions and convert to Q/A
        pattern = r"([A-Z][^.?:!]+?)\s+(is|are|was|means|refers to)\s+([^.:!?]+)"
        matches = re.findall(pattern, self.text)

        for match in matches[:max_cards]:
            term = match[0].strip()
            definition = match[2].strip()
            question = f"What is {term}?"
            answer = definition
            self.flashcards.append({"question": question, "answer": answer})

        return self.flashcards

    def export_to_json(self, path="flashcards.json"):
        with open(path, "w") as f:
            json.dump(self.flashcards, f, indent=4)
