from openai import OpenAI
import openai
import time
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)
def get_oai_completion(prompt,model):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        print(f"Error fetching answer: {e}")
        return None

def call_chatgpt(prompt,model):
    success = False
    re_try_count = 10
    ans = ''
    while not success and re_try_count >= 0:
        re_try_count -= 1
        try:
            ans = get_oai_completion(prompt,model)
            success = True
        except:
            time.sleep(5)
            print('retry for sample:', prompt)
    return ans