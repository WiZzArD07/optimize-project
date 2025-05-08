# src/utils/prompt_utils.py

def format_conversation(prompt, response):
    """
    Format a user-assistant conversation into a string.
    """
    return f"User: {prompt}\nAssistant: {response}"

def truncate_prompt(prompt, max_tokens=300):
    """
    Truncate prompt to a max token-like length (rough estimate by char count).
    """
    return prompt[:max_tokens * 4]  # rough estimate: 1 token ≈ 4 chars

# Example:
# print(format_conversation("Hi!", "Hello there!"))

