# 🌦️ Weather Dashboard

A Flask-based web application that provides real-time weather information for any city using the OpenWeatherMap API. The application fetches live weather data and displays it through a clean, responsive user interface with proper error handling.

---

## ✨ Features

* 🌍 Search weather for any city worldwide
* 🌡️ Displays current temperature and feels-like temperature
* 📈 Shows minimum and maximum temperature
* 💧 Displays humidity level
* 💨 Shows wind speed
* 🌤️ Displays current weather condition
* ⚠️ Handles invalid city names gracefully
* 🔐 Stores API keys securely using environment variables
* 📱 Responsive and user-friendly interface

---

## 🛠️ Tech Stack

* Python
* Flask
* HTML5
* CSS3
* Jinja2
* Requests
* Python-dotenv
* OpenWeatherMap API

---

## 📁 Project Structure

```text
weather_dashboard/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── weather.html
│
├── .env
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/priyanshu01272-spec/jobvacancyfinder.git
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

---

## 🔑 API Configuration

1. Create a free account on OpenWeatherMap.
2. Generate an API key from your dashboard.
3. Create a `.env` file in the project root.

Add the following:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

> If you have changed the Flask port (for example, to **5002**), open:
>
> ```
> http://127.0.0.1:5002
> ```

---

## 🚀 Future Improvements

* 5-day weather forecast
* Automatic location detection
* Dark/Light mode
* Recent search history
* Temperature unit conversion (°C / °F)
* Weather icons and animations

---

## 👨‍💻 Author

**Priyanshu Sharma**

GitHub: https://github.com/priyanshu01272-spec
