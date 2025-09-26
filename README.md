# Trade Opportunities API

A FastAPI service that analyzes market data and provides trade opportunity insights for specific sectors in India.

## Features
- Single endpoint: `/analyze/{sector}`
- Returns a structured markdown report with current market news
- Real news headlines via NewsAPI.org
- Basic authentication (username: `user`, password: `pass`)
- Rate limiting (5 requests per user/session)
- Input validation and error handling

## Setup Instructions

1. **Clone the repository**
2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
3. **Add your NewsAPI.org API key**
   - The API key is set in `.env` as `NEWSAPI_KEY`.
4. **(Optional) Add your OpenAI API key**
   - To enable AI-generated markdown reports, set your OpenAI API key in `.env` as `OPENAI_API_KEY`.
   - If you do not provide an OpenAI API key or your quota is exceeded, the report will only show news data.
4. **Run the server**:
   ```sh
   uvicorn main:app --reload
   ```
5. **Access the API**:
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive docs.
   - Use `/analyze/{sector}` endpoint (e.g., `/analyze/finance`).
   - Authenticate with username `user` and password `pass`.

## Example Request
```
curl -u user:pass "http://127.0.0.1:8000/analyze/finance"
```

## Response Format
Returns a markdown report with:
- Sector name
- Top 5 recent news headlines

## Security
- Basic authentication
- Rate limiting
- Input validation





## To Do / Extensions
- Switch to JWT authentication for stronger security
- Improve error handling and logging

## License
MIT
