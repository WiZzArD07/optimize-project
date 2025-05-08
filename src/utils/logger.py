# src/utils/logger.py

import os
import json
from datetime import datetime

def log_to_file(results, log_dir="logs", name_prefix="eval"):
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(log_dir, f"{name_prefix}_{timestamp}.json")

    with open(file_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"[Logger] Saved evaluation results to: {file_path}")

# Example:
# log_to_file(results)
