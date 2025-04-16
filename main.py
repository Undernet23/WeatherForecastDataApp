import streamlit as st
import plotly.express as px
from backend import get_data
import datetime

# Add title, text input, slide, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))

st.subheader(f"{option} for the next {days} days in {place}")
if place:
    try:
        # Get temperature/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] - 273.15 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.bar(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature, C"})
            st.plotly_chart(figure)

        images = {
            "clear": "images/clear.png",
            "clouds": "images/clouds.png",
            "rain": "images/rain.png",
            "snow": "images/snow.png",
        }

        dates = [dict["dt_txt"] for dict in filtered_data]
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]

        # Optional debug
        # st.write("Sky conditions:", sky_conditions)

        for i in range(0, len(sky_conditions), 5):
            cols = st.columns(5)
            for col, date, condition in zip(cols, dates[i:i + 5], sky_conditions[i:i + 5]):
                image_src = images.get(condition.lower(), "images/clear.png")
                col.image(image_src, caption=date, width=100)


    except KeyError:
        st.warning(":orange[Please enter an existing place]", icon="⚠️")