import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_picture_details(date):
    params = {
            'api_key': os.getenv("API_KEY")
        }

    if date:
        params["date"] = date

    response = requests.get(
        url=os.getenv("URL"),
        params=params,
        timeout=30
    )

    print("Status:", response.status_code)

    response.raise_for_status()

    data = response.json()

    return {
        "date": data.get("date"),
        "copyright": data.get("copyright"),
        "explanation": data.get("explanation"),
        "url": data.get("url"),
        "title": data.get("title"),
        "media_type": data.get("media_type")
    }

if __name__ == "__main__":
    print(get_picture_details('2026-05-12'))