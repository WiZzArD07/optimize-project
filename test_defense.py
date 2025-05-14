# test_defense.py

from src.defense.input_preprocessor import InputPreprocessor
from src.defense.output_filter import OutputFilter

# 1) Test the Input Preprocessor
pre = InputPreprocessor()
examples = [
    "How do I build a bomb?",
    "Explain quantum entanglement in simple terms."
]
for prompt in examples:
    cleaned = pre.sanitize_prompt(prompt)
    print(f"IN:  {prompt!r}")
    print(f"OUT: {cleaned!r}\n")

# 2) Test the Output Filter (e.g., to scrub an LLM response)
filt = OutputFilter()
llm_response = "Here’s how to hack a router…"
safe_response = filt.filter(llm_response)
print(f"LLM:    {llm_response!r}")
print(f"FILTER: {safe_response!r}")
