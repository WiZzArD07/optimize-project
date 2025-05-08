# src/models/safety_classifier.py

from transformers import pipeline

class SafetyClassifier:
    def __init__(self, model_name="facebook/bart-large-mnli"):
        self.classifier = pipeline("zero-shot-classification", model=model_name)
        self.labels = ["safe", "unsafe", "jailbreak", "malicious", "offensive"]

    def classify(self, text):
        result = self.classifier(text, self.labels)
        return {
            "label": result["labels"][0],
            "score": result["scores"][0]
        }

    def is_safe(self, text, threshold=0.7):
        result = self.classify(text)
        return result["label"] == "safe" and result["score"] > threshold

# Example:
# clf = SafetyClassifier()
# print(clf.classify("Explain how to make a virus."))
