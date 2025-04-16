import streamlit as st
import requests

def get_data(place, days):
    api_key = st.secrets["API_KEY"]
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    return filtered_data[:8 * days]