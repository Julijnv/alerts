import requests
from config.settings import GOOGLE_API_KEY, SEARCH_ENGINE_ID, SEARCH_QUERY

def perform_google_search():
    """
    Executes a search query using the Google Custom Search API.

    Returns:
        list: A list of URLs from the search results, or an empty list if the search fails.
    """
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": SEARCH_QUERY,
        "cx": SEARCH_ENGINE_ID,
        "key": GOOGLE_API_KEY,
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return [item["link"] for item in data.get("items", [])]
        else:
            print(f"Google Search API error: {response.status_code}")
            return []
    except Exception as e:
        print(f"Exception occurred during Google search: {e}")
        return []
