# src/utils/data_loader.py

import json
import os

def load_json_prompts(file_path, label_type=None):
    """
    Loads a JSON list of prompts and tags them with a type if given.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, 'r') as f:
        data = json.load(f)

    if label_type:
        for item in data:
            item['type'] = label_type

    return data

def load_all_prompts(dataset_paths):
    """
    Loads multiple prompt files and concatenates them into one list.
    """
    all_data = []
    for path, label in dataset_paths:
        all_data.extend(load_json_prompts(path, label))
    return all_data

# Example:
# prompts = load_all_prompts([
#     ("data/red_team_prompts.json", "red"),
#     ("data/synthetic_prompts.json", "synthetic"),
#     ("data/safe_prompts.json", "safe")
# ])
