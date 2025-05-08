# tests/test_data_loader.py

import pytest
from src.utils.data_loader import load_json_prompts, load_all_prompts

def test_load_json_prompts():
    data = load_json_prompts("data/red_team_prompts.json", "red")
    assert len(data) > 0
    assert all('prompt' in entry for entry in data)
    assert all('type' in entry for entry in data)

def test_load_all_prompts():
    data = load_all_prompts([
        ("data/red_team_prompts.json", "red"),
        ("data/synthetic_prompts.json", "synthetic"),
        ("data/safe_prompts.json", "safe")
    ])
    assert len(data) > 0
    assert any(entry['type'] == 'red' for entry in data)
    assert any(entry['type'] == 'synthetic' for entry in data)
    assert any(entry['type'] == 'safe' for entry in data)
