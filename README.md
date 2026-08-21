# bootcamp_weather_app

AIPI Python Bootcamp weather app, built up over two challenges:

- **Day 1:** a command-line script that looks up the weather for a city
- **Day 2:** the same weather lookup, now wrapped in a Streamlit app you run locally in your browser

Both use the [OpenWeatherMap API](https://openweathermap.org/api).

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

## Run the Streamlit app (Day 2)

```bash
streamlit run get_weather.py
```

This opens the app in your browser. Type a US city name, click **Get Weather**,
and you'll see the temperature (°C), humidity, a weather-themed emoji, and a
small chart comparing the two.

## Run the original CLI version (Day 1)

The very first version of this app is still in the git history if you'd like
to see it — check the commit log for "Add weather CLI app with temp, humidity,
and description." That version ran with:

```bash
python get_weather.py
```

and prompted for a city name directly in the terminal instead of a browser.
