import requests
import matplotlib.pyplot as plt

API_KEY = "YOUR_API_KEY"

city = input("Enter City Name: ")

url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

temps = []
times = []

for item in data['list'][:8]:
    temps.append(item['main']['temp'])
    times.append(item['dt_txt'])

plt.plot(times, temps, marker='o')

plt.xticks(rotation=45)

plt.title(f"Temperature Forecast for {city}")

plt.xlabel("Time")

plt.ylabel("Temperature °C")

plt.tight_layout()

plt.show()