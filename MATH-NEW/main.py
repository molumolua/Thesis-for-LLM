# main.py

import os
import json
import random
from tqdm import tqdm
from data_loader import load_problems
from openai_access import call_chatgpt,get_oai_completion
from config import OUTPUT_PATH

def save_answer(category, file_name, answer):
    category_output_path = os.path.join(OUTPUT_PATH, category)
    os.makedirs(category_output_path, exist_ok=True)
    answer_file_path = os.path.join(category_output_path, file_name)
    with open(answer_file_path, 'w', encoding='utf-8') as f:
        json.dump({'answer': answer}, f, ensure_ascii=False, indent=4)


random.seed(2025)
problems = load_problems()
random.shuffle(problems)
problems = problems[:1]
print(problems)
print(f"Total problems to process: {len(problems)}")
    
for idx, problem in tqdm(enumerate(problems, 1)):
    print(f"Processing {idx}/{len(problems)}: {problem['file_name']} in {problem['category']}")
    answer = get_oai_completion(problem['problem'],"gpt-4")
    if answer:
        save_answer(problem['category'], problem['file_name'], answer)
        print(f"Answer saved for {problem['file_name']}")
    else:
        print(f"Failed to get answer for {problem['file_name']}")

