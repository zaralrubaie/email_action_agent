import os
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def generate_action_plan(tasks: list) -> dict:
    prompt = f"""
    Based on these tasks:

    {tasks}

    Create a clear step-by-step action plan.
    Return ONLY valid JSON with:
    - priority
    - steps (list of strings)
    """

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return {"priority": "Medium", "steps": []}
