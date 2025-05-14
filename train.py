
 # train.py

import json
from src.defense.input_preprocessor import InputPreprocessor
from src.defense.adversarial_training import run_adversarial_training
from src.utils.data_loader import load_json_prompts

def main():
    # Load configuration files
    with open("config/config.json", "r") as f:
        config = json.load(f)
    with open("config/training_config.json", "r") as f:
        training_config = json.load(f)

    # Instantiate the preprocessor
    preprocessor = InputPreprocessor()

    # Load raw prompts
    raw_red_prompts  = load_json_prompts(config["data_paths"]["red_team"], "red")
    raw_safe_prompts = load_json_prompts(config["data_paths"]["safe"],      "safe")

    # Sanitize and filter out any blocked prompts
    def sanitize_batch(prompts):
        cleaned = []
        for p in prompts:
            sanitized = preprocessor.sanitize_prompt(p)
            # If it's been blocked, skip
            if sanitized.startswith("[BLOCKED PROMPT"):
                continue
            cleaned.append(sanitized)
        return cleaned

    red_team_prompts = sanitize_batch(raw_red_prompts)
