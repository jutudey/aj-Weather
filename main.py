import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the next days")
place = st.text_input("Place: ")
days = st.slider('Forecast days: ', min_value=1, max_value=5,
                 help="Select the number of days you want included in the forecast")
option = st.selectbox('Select data to view:', ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} in {place}")

# dates = ['2024-10-09', '2024-10-10', '2024-10-11']
# temperatures = [10, 11, 15]
# figure = px.line(x=dates, y=temperatures, labels={'x': "Date", "y":"Temperature in C"})

data = get_data(place, days,option)


st.plotly_chart(figure)
