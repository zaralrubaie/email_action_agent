import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def summarize_email(email_text: str) -> str:
    prompt = f"""
    Summarize the following email in 3–4 sentences.
    Focus on the main request, deadlines, offers, and important context.

    Email:
    {email_text}
    """

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
