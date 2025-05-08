# src/defense/output_filter.py

from transformers import pipeline

class OutputFilter:
    def __init__(self, model="facebook/bart-large-mnli"):
        self.classifier = pipeline("zero-shot-classification", model=model)
        self.labels = ["safe", "unsafe", "jailbreak", "malicious", "offensive"]

    def is_safe(self, output_text: str, threshold: float = 0.7) -> bool:
        result = self.classifier(output_text, self.labels)
        top_label = result["labels"][0]
        top_score = result["scores"][0]
        return top_label == "safe" and top_score > threshold

# Example:
# f = OutputFilter()
# f.is_safe("Here's how to disable a camera system.")

