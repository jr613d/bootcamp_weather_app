"""
Weather Report Streamlit App
-----------------------------
Day 2 challenge: takes the API call from Day 1 and wraps it in a simple
Streamlit app. Type a city name, click the button, and see the weather.

Run it with:
    streamlit run get_weather.py
"""

import os
import re

import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv

# Load OPENWEATHER_API_KEY from the local .env file (never commit this file/key)
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    Call the OpenWeatherMap API for the given city.

    Returns a dictionary with city_name, temp, humidity, and description
    if the call worked, or None if something went wrong (e.g. bad city name).
    """
    # Adding ",US" keeps results scoped to US cities, since many city names
    # (like "Springfield") repeat across different states/countries.
    params = {
        "q": f"{city},US",
        "appid": API_KEY,
        "units": "metric",  # metric units give temperature in Celsius
    }

    response = requests.get(BASE_URL, params=params)

    # If the API call didn't succeed (e.g. city not found), stop here
    if response.status_code != 200:
        return None

    data = response.json()

    # Pull out just the pieces of the response we actually need
    weather_info = {
        "city_name": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
    }
    return weather_info


def clean_up_description(description):
    """
    Make the description look nicer, e.g. turn "clear sky" into "Clear Sky".
    Uses a simple regex to capitalize the first letter of every word.
    """
    return re.sub(r"\b\w", lambda match: match.group().upper(), description)


def pick_emoji(description):
    """
    Pick a simple emoji based on keywords in the weather description.
    Just a fun visual touch - nothing fancy, just an if/elif chain.
    """
    description = description.lower()

    if "clear" in description:
        return "☀️"
    elif "cloud" in description:
        return "☁️"
    elif "rain" in description:
        return "🌧️"
    elif "snow" in description:
        return "❄️"
    elif "thunderstorm" in description:
        return "⛈️"
    elif "mist" in description or "fog" in description:
        return "🌫️"
    else:
        return "🌡️"


# ----------------------------------------------------------------
# Streamlit app starts here. Everything below this line runs every
# time the page loads or a widget (like the button) is interacted with.
# ----------------------------------------------------------------

st.title("🌎 Weather Report App")
st.write("Enter a US city name below to see the current weather.")

# A text box for the user to type a city name into
city = st.text_input("City name", placeholder="e.g. Raleigh")

# We use a button here instead of looking up the weather on every keystroke.
# Streamlit reruns the whole script whenever a widget changes, so without a
# button, we'd call the API after every single letter typed - a button lets
# the user finish typing first and only calls the API when they're ready.
if st.button("Get Weather"):
    if not API_KEY:
        st.error("No API key found. Make sure OPENWEATHER_API_KEY is set in your .env file.")
    elif not city:
        st.warning("Please enter a city name first.")
    else:
        weather = get_weather(city)

        if weather is None:
            st.error(f"Sorry, couldn't find weather for '{city}'. Check the spelling and try again.")
        else:
            emoji = pick_emoji(weather["description"])
            description = clean_up_description(weather["description"])

            st.subheader(f"{emoji} Weather in {weather['city_name']}, US")
            st.write(f"**Conditions:** {description}")

            # st.metric displays a label with a big, easy-to-read number
            col1, col2 = st.columns(2)
            col1.metric("Temperature (°C)", weather["temp"])
            col2.metric("Humidity (%)", weather["humidity"])

            # A small bar chart comparing temperature and humidity.
            # st.bar_chart wants a table (DataFrame), so we build a tiny
            # one with two rows: one for temp, one for humidity.
            st.write("Quick comparison chart:")
            chart_data = pd.DataFrame(
                {"Value": [weather["temp"], weather["humidity"]]},
                index=["Temperature (°C)", "Humidity (%)"],
            )
            st.bar_chart(chart_data)
