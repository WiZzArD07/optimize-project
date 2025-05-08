# LLM Jailbreak Prevention Project

This project is designed to optimize Large Language Models (LLMs) for reducing jailbreaks and enhancing safety. It includes fine-tuning, adversarial training, safety filtering, and evaluation.

## Project Structure
config/
├── config.json # Paths and configurations
├── training_config.json# Hyperparameters for training
data/
├── red_team_prompts.json # Adversarial prompts
├── synthetic_prompts.json # Synthetic prompts
├── safe_prompts.json # Safe prompts
src/
├── models/ # LLM model and safety classifier
├── eval/ # Evaluation metrics and pipelines
├── defense/ # Defense mechanisms like adversarial training and output filtering
├── utils/ # Helper functions and utilities
tests/ # Unit tests for all components
notebooks/ # Jupyter notebooks for exploration and evaluation


## Setup

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Prepare your data in the `data/` folder (e.g., red_team_prompts.json, safe_prompts.json, synthetic_prompts.json).

4. Run the training pipeline in `train.py`.

## Running the Training Pipeline

To start the training process, simply run:

```bash
python train.py
