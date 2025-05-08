

## `train.py`

# train.py

import json
from src.defense.adversarial_training import run_adversarial_training
from src.utils.data_loader import load_json_prompts

# Load configuration files
with open("config/config.json", "r") as f:
    config = json.load(f)
with open("config/training_config.json", "r") as f:
    training_config = json.load(f)

# Load prompts
red_team_prompts = load_json_prompts(config["data_paths"]["red_team"], "red")
safe_prompts = load_json_prompts(config["data_paths"]["safe"], "safe")

# Combine prompts
all_prompts = red_team_prompts + safe_prompts

# Fine-tune the model
run_adversarial_training(
    model_name=config["model_name"], 
    prompts=all_prompts, 
    output_dir=config["output_dir"]
)
