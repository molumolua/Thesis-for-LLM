# data_loader.py

import os
import json
from config import TRAINING_DATA_PATH

def load_problems():
    problems = []
    for category in os.listdir(TRAINING_DATA_PATH):
        category_path = os.path.join(TRAINING_DATA_PATH, category)
        if os.path.isdir(category_path):
            for file_name in os.listdir(category_path):
                if file_name.endswith('.json'):
                    file_path = os.path.join(category_path, file_name)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        problems.append({
                            'category': category,
                            'file_name': file_name,
                            'problem': data.get('problem'),
                            'level': data.get('level'),
                            'type': data.get('type'),
                            'solution': data.get('solution')
                        })
    return problems
