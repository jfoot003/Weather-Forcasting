import streamlit as st
import pandas as pd
import requests


# Function to fetch weather data
def get_weather_data(city_name):
    api_key = '79e62f2d0518c73492fd68d8cde6ee68'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()


# Streamlit app
st.title('Weather Forecast App')

# Input for city name
city = st.text_input('Enter city name:')

if city:
    data = get_weather_data(city)
    if data:
        st.write(f"Temperature: {data['main']['temp']}°C")
        st.write(f"Weather: {data['weather'][0]['description']}")
        st.write(f"Humidity: {data['main']['humidity']}%")
        st.write(f"Wind Speed: {data['wind']['speed']} m/s")

        # Line chart for temperature
        temp_data = pd.DataFrame({'Temperature': [data['main']['temp']]}, index=[city])
        st.line_chart(temp_data)

        # Map for location
        map_data = pd.DataFrame({'lat': [data['coord']['lat']], 'lon': [data['coord']['lon']]})
        st.map(map_data)

        # Show raw data
        if st.checkbox('Show raw data'):
            st.write(data)
    else:
        st.error('City not found!')
