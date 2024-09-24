import streamlit as st
from click import option

st.title("Weather Forecast for the next days")
place = st.text_input("Place: ")
days = st.slider('Forecast days: ', min_value=1, max_value=5,
                 help="Select the number of days you want included in the forecast")
option = st.selectbox('Select data to view:', ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} in {place}")

print()