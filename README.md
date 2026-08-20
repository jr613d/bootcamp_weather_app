# bootcamp_weather_app

Week 5 Day 1 challenge for AIPI Python Bootcamp — a command-line app that looks up
the current weather for a city using the [OpenWeatherMap API](https://openweathermap.org/api).

## Setup

```bash
git clone https://github.com/jr613d/bootcamp_weather_app.git
cd bootcamp_weather_app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root with your own API key:

```
OPENWEATHER_API_KEY=your_api_key_here
```

## Run it

```bash
python get_weather.py
```

You'll be prompted to enter a city name, then it prints the temperature (°C),
humidity, and current conditions.
