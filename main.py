from functions import get_picture_details
from datetime import date as dt_date
import streamlit as st

st.set_page_config(page_title="Nasa Picture of the Day", page_icon="🚀")
st.title("Nasa Picture of the Day 🧑‍🚀🚀")

selected_date = st.date_input("Select a date! 🕰️", max_value=dt_date.today())

formatted_date = selected_date.strftime("%Y-%m-%d")
image_details = get_picture_details(formatted_date)

if image_details:
    if image_details["media_type"] == "image":
        st.image(image_details["url"])
        st.subheader(image_details["author"])
        st.text(image_details["explanation"])
    else:
        st.text("Sorry this page is dedicated only for pictures...")

else:
    st.info("Ooops... No data found for this date. Please try another one")
