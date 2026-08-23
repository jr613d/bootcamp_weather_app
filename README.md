# Weather Report App 🌤️

## Overview

A simple Streamlit app that looks up the current weather for a US city using
the [OpenWeatherMap API](https://openweathermap.org/api) and displays the
temperature, humidity, and conditions, with a quick comparison chart.

## Getting Started

### Prerequisites

- Python 3.9+
- Git
- A free API key from [OpenWeatherMap](https://openweathermap.org/api)

### Installation

```bash
# Clone the repo
git clone https://github.com/jr613d/bootcamp_weather_app.git
cd bootcamp_weather_app

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate      # macOS/Linux
.\.venv\Scripts\Activate.ps1   # Windows PowerShell

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root with your own API key:

```
OPENWEATHER_API_KEY=your_api_key_here
```

(If you're running this on Streamlit Community Cloud instead of locally, add
the same key under your app's Settings → Secrets, in the same `KEY = "value"`
format, instead of using a `.env` file.)

### Running the App

```bash
streamlit run get_weather.py
```

Then open your browser at http://localhost:8501.

## Usage Examples

1. Type a US city name (e.g. "Raleigh") into the text box.
2. Click **Get Weather**.
3. View the temperature, humidity, and conditions, along with a small bar
   chart comparing the two.

## Project History

This app started as a command-line script (Day 1 challenge) before being
rebuilt as a Streamlit app (Day 2 challenge). The original CLI version is
still visible in the commit history if you're curious how it evolved.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
