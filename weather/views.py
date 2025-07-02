from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse
import requests
from datetime import datetime

apiUrl = "https://api.openweathermap.org/data/2.5/weather"
apiKey = "a022f72ea505715efcc711ed4a1e89e0" 

def index(request):
    return render(request, 'index.html')

def showdata(request):
    city = request.POST.get('text')
    
    if not city:
        return HTTPResponse("Please enter a city name.")

    params = {
        'q': city,
        'appid': apiKey,
        'units': 'metric'
    }

    response = requests.get(apiUrl, params=params)

    if response.status_code == 200:
        data = response.json()
        
        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')

        weather_data = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'temp_min': data['main']['temp_min'],
            'temp_max': data['main']['temp_max'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed'],
            'weather_main': data['weather'][0]['main'],
            'description': data['weather'][0]['description'],
            'sunrise': sunrise,
            'sunset': sunset,
        }

        return render(request, 'showData.html', weather_data)
    else:
        return HTTPResponse("City not found or error fetching data.")
