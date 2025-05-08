# tests/test_base_model.py

from src.models.base_model import BaseLLM

def test_generate():
    model = BaseLLM("gpt2")
    prompt = "What is the capital of France?"
    response = model.generate(prompt)
    
    assert response
    assert "Paris" in response  # since it's the expected output
