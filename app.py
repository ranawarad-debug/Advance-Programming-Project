from flask import Flask, render_template, jsonify, request
import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

app = Flask(__name__)

# Get API key from .env
API_KEY = os.getenv("API_KEY")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather', methods=['GET'])
def get_weather():

    city = request.args.get('city')

    if not city:
        return jsonify({
            "error": "City name is required"
        }), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if response.status_code != 200:
        return jsonify({
            "error": "City not found"
        }), 404

    weather_data = {
        "city": city,
        "temperature": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "pressure": data['main']['pressure'],
        "wind_speed": data['wind']['speed'],
        "description": data['weather'][0]['description'],
        "main_weather": data['weather'][0]['main']
    }

    return jsonify(weather_data)


if __name__ == '__main__':
    app.run(debug=True)