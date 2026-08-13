from functions import get_picture_details
from dotenv import load_dotenv
from datetime import date as dt_date
import streamlit as st

st.set_page_config(page_title="Nasa Picture of the Day", page_icon="🚀")
st.title("NASA Picture Of The Day")

selected_date = st.date_input(label = "Please select a date! 🕰️", max_value=dt_date.today())
formatted_date = selected_date.strftime("%Y-%m-%d")

picture_details = get_picture_details(date=formatted_date)

if picture_details['media_type'] != "image":
    st.text("Sorry this website is for pictures only")

else:
    st.image(picture_details["url"])
    st.header(picture_details['title'])
    st.markdown(picture_details['copyright'])
    st.text(picture_details['explanation'])

