# src/defense/output_filter.py
class OutputFilter:
    def __init__(self):
        self.blocklist = ["hack", "explosive", "kill", "bomb", "attack", "drugs", "malware"]

    def filter(self, text: str) -> str:
        for word in self.blocklist:
            if word in text.lower():
                return "[REDACTED: unsafe content]"
        return text


