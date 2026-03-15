from dotenv import load_dotenv
import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")
api_url = os.getenv("API_URL").replace("DEMO_KEY", api_key)


def get_picture_details(date=None):
    if date:
        response = requests.get(f"{api_url}&date={date}")
    else:
        response = requests.get(api_url)

    data = response.json()

    print(data)

    return {
        "explanation": data.get("explanation"),
        "url": data.get("hdurl"),
        "author": data.get("copyright"),
        "media_type": data.get("media_type")
    }


if __name__ == '__main__':
    print(f"API URL: {api_url}")
    print(get_picture_details())
