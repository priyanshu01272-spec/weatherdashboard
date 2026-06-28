from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city", "").strip()

    if not city:
        return render_template("index.html", error="Please enter a city name.")

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
    except requests.exceptions.ConnectionError:
        return render_template("index.html", error="Network error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        return render_template("index.html", error="Request timed out. Please try again.")

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": round(data["main"]["temp"]),
            "feels_like": round(data["main"]["feels_like"]),
            "temp_min": round(data["main"]["temp_min"]),
            "temp_max": round(data["main"]["temp_max"]),
            "condition": data["weather"][0]["description"].title(),
            "main_weather": data["weather"][0]["main"],
            "icon": data["weather"][0]["icon"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "pressure": data["main"]["pressure"],
        }
        return render_template("weather.html", weather=weather_info)

    elif response.status_code == 404:
        return render_template(
            "index.html",
            error=f"City '{city}' not found. Please check the spelling and try again."
        )
    elif response.status_code == 401:
        return render_template("index.html", error="Invalid API key. Check your .env file.")
    else:
        return render_template("index.html", error="Something went wrong. Please try again later.")


if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv("PORT", 5001)))
