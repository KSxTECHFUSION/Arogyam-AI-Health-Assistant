import requests

# Clean user question if needed
def refine_question(question: str) -> str:
    return question.strip()

# Generate AI-like response using DuckDuckGo Instant Answer API
def get_ai_response(question: str) -> str:
    refined_q = refine_question(question)

    # DuckDuckGo Instant Answer API URL
    url = "https://api.duckduckgo.com/"
    params = {
        "q": refined_q,
        "format": "json",
        "no_redirect": 1,
        "no_html": 1,
        "skip_disambig": 1
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        # Try to get direct answer
        if data.get("AbstractText"):
            return data["AbstractText"]
        elif data.get("Answer"):
            return data["Answer"]
        elif data.get("Definition"):
            return data["Definition"]
        else:
            return "I'm sorry, I don't have a perfect answer for that. Could you try asking differently?"
    except Exception:
        return "Oops! I'm having trouble finding an answer right now. Please try again later."