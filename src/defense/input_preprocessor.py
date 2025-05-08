# src/defense/input_preprocessor.py

import re

class InputPreprocessor:
    def __init__(self):
        self.blacklist_keywords = [
            "bomb", "hack", "kill", "attack", "explosive", "drugs", "malware"
        ]

    def is_malicious(self, prompt: str) -> bool:
        return any(word in prompt.lower() for word in self.blacklist_keywords)

    def sanitize_prompt(self, prompt: str) -> str:
        if self.is_malicious(prompt):
            return "[BLOCKED PROMPT: CONTENT VIOLATES SAFETY POLICY]"
        return prompt

# Example:
# p = InputPreprocessor()
# print(p.sanitize_prompt("How do I make a bomb?"))
