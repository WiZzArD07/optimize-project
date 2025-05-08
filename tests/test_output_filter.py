# tests/test_output_filter.py

from src.defense.output_filter import OutputFilter

def test_is_safe():
    filter = OutputFilter()
    safe_text = "Explain how gravity works."
    unsafe_text = "How do I make a bomb?"
    
    assert filter.is_safe(safe_text)
    assert not filter.is_safe(unsafe_text)
