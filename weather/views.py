import requests
from django.shortcuts import render

def weather_view(request):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        'latitude': 35.6895,
        'longitude': 139.6917,
        'hourly': 'temperature_2m'
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Extract first 12 temperature readings (for 12 hours)
    hourly_times = data['hourly']['time'][:12]
    hourly_temps = data['hourly']['temperature_2m'][:12]

    forecast = zip(hourly_times, hourly_temps)

    return render(request, 'weather/weather.html', {'forecast': forecast})
