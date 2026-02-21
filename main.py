from dotenv import load_dotenv
from datetime import datetime, date
import streamlit as st
import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")
base_url = os.getenv("URL").replace("DEMO_KEY", api_key)


def generate_pic(selected_date):
    params = {
        "api_key": api_key,
        "date": selected_date.strftime("%Y-%m-%d")
    }

    if selected_date > date.today():
        st.error("Even NASA can't see the future. Please select an earlier day.")
        return

    response = requests.get(base_url, params=params)
    print(response.status_code)

    if response.status_code == 200:
        data = response.json()

        st.header(data.get('title', 'Astronomy Picture'))
        img_url = data.get('hdurl', data.get('url'))

        if data.get("media_type") == "image":
            st.image(img_url)
        else:
            st.video(img_url)

        st.write(data.get('explanation'))

    else:
        st.error(f"Error {response.status_code}: Could not fetch data.")


st.subheader('Picture of the day')
user_date = st.date_input(label="🚀🧑‍🚀")

if user_date:
    generate_pic(user_date)
