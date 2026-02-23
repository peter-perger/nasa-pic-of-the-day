from dotenv import load_dotenv
import streamlit as st
from datetime import date
import requests
import os

load_dotenv()

api_key = os.getenv("API_KEY")
url = os.getenv("URL").replace("DEMO_KEY", api_key)


def generate_pic(user_date, url):
    params = {
        "api_key": api_key,
        "date": user_date
    }

    if user_date > date.today():
        st.error("Even NASA can't see the future. PLease select an earlier date")
        return

    respone = requests.get(url, params=params)

    if respone.status_code == 200:
        image_url = respone.json()["hdurl"]
        text_section = respone.json()["explanation"]
        author = respone.json()["copyright"]

        st.image(image_url)
        st.title(author)
        st.text(text_section)

    else:
        st.error("Server errror, please come back later ❌❌")

    print(date.today())


user_date = st.date_input(label="Select a date! 🚀🧑‍🚀")
generate_pic(user_date=user_date, url=url)
