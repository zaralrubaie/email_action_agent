import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def extract_tasks(email_text: str) -> list:
    prompt = f"""
    Extract all actionable tasks from this email.
    Return ONLY valid JSON list of objects with:
    - task
    - deadline (null if not mentioned)
    - priority (High/Medium/Low)

    Email:
    {email_text}
    """

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return []
