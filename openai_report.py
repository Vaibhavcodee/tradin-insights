import openai
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def get_openai_report(sector, market_data):
    prompt = (
        f"Generate a markdown report for trade opportunities in the {sector} sector in India.\n"
        f"Here is some recent market data/news:\n{market_data}\n"
        "The report should include:\n"
        "- Sector name\n"
        "- Key market trends\n"
        "- Trade opportunities\n"
        "- Risks\n"
        "- Recommendations\n"
        "Format the report in markdown."
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600
    )
    return response.choices[0].message.content