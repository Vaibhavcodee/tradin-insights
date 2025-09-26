
# news.py - Handles fetching news headlines for a sector using NewsAPI

import httpx
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

async def fetch_news(sector: str) -> str:
    """
    Fetch top 5 recent news headlines for the given sector in India.
    Returns a markdown list of headlines, or an error message if something goes wrong.
    """
    # Build the NewsAPI request URL
    url = (
        f"https://newsapi.org/v2/everything?q={sector}+india"
        f"&apiKey={NEWSAPI_KEY}&pageSize=5&sortBy=publishedAt&language=en"
    )
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=15)
            response.raise_for_status()
            data = response.json()
            articles = data.get("articles", [])
            if not articles:
                return "No recent news found."
            # Format headlines as markdown links
            headlines = [f"- [{article['title']}]({article['url']})" for article in articles]
            return "\n".join(headlines)
    except Exception as error:
        return f"Error fetching news: {error}"
