# 🌤️ Weather Dashboard

A Flask web app that shows real-time weather data for any city using the OpenWeatherMap API.

## Features
- Search any city in the world
- Shows: Temperature, Feels Like, Min/Max, Humidity, Wind Speed, Pressure, Sky Condition
- Quick-search buttons for popular cities
- Error handling for invalid city names

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/weather_dashboard.git
cd weather_dashboard
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
OPENWEATHER_API_KEY=your_api_key_here
```

### 6. Run the application

```bash
python app.py
```

### 7. Open in your browser

```
http://127.0.0.1:5000
```

---

## Project Structure
```
weather_dashboard/
├── app.py              # Flask routes + API logic
├── .env                # API key (never commit this!)
├── .gitignore
├── requirements.txt
├── templates/
│   ├── base.html       # Shared layout (navbar, footer)
│   ├── index.html      # Search form page
│   └── weather.html    # Results page
└── static/
    └── style.css       # Styling
```

## API Used
[OpenWeatherMap Current Weather API](https://openweathermap.org/current)
- Free tier: 60 calls/minute, 1,000,000 calls/month
