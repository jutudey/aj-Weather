import streamlit as st
import plotly.express as px
from backend import get_data

# add GUI elements
st.title("Weather Forecast for the next days")
place = st.text_input("Name of city you want the weather forcast for: ")
days = st.slider('Forecast days: ', min_value=1, max_value=5,
                 help="Select the number of days you want included in the forecast")
option = st.radio('Select data to view:', ("Temperature", "Weather Conditions"))

if place:
    st.subheader(f"{option} for the next {days} in {place}")

    # fetch data via API
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [dict["main"]['temp'] for dict in filtered_data]
        date = [dict['dt_txt'] for dict in filtered_data]
        # create temperature plot
        figure = px.line(x=date, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Weather Conditions":
        sky_conditions = [dict["weather"][0]['main'] for dict in filtered_data]
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": 'images/snow.png'}
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)
