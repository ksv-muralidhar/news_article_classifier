import os


def get_api_url():
    api_url = os.getenv("API_URL")
    if api_url is None:
        api_url = "http://localhost:5001"
    return api_url
