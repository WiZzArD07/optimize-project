# src/eval/run_eval.py

import json
from ..models.base_model import BaseLLM
from ..models.safety_classifier import SafetyClassifier

from src.eval.metrics import (
    compute_jailbreak_rate,
    compute_false_positive_rate,
    compute_safety_accuracy
)


def load_prompts(filepath, label_type):
    with open(filepath, 'r') as f:
        data = json.load(f)
    for d in data:
        d['type'] = label_type
    return data


def evaluate_model(model, classifier, prompts):
    results = []
    for example in prompts:
        prompt = example['prompt']
        response = model.generate(prompt)
        is_safe = classifier.is_safe(response)
        results.append({
            'prompt': prompt,
            'response': response,
            'is_safe': is_safe,
            'type': example['type']
        })
    return results


def main():
    # Load model and classifier
    llm = BaseLLM()
    clf = SafetyClassifier()

    # Load all prompt types
    red = load_prompts("data/red_team_prompts.json", "red")
    syn = load_prompts("data/synthetic_prompts.json", "synthetic")
    safe = load_prompts("data/safe_prompts.json", "safe")

    all_prompts = red + syn + safe
    results = evaluate_model(llm, clf, all_prompts)

    # Metrics
    print("\n--- Evaluation Metrics ---")
    print(f"Jailbreak Rate: {compute_jailbreak_rate(results):.2%}")
    print(f"False Positive Rate: {compute_false_positive_rate(results):.2%}")
    print(f"Safety Accuracy: {compute_safety_accuracy(results):.2%}")


if __name__ == "__main__":
    main()
