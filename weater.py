import requests
import argparse




def weather_check(city):
    api_token = "e4d6d1f0b51027b7f69dde004f4b4f31"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = { 
        'q': city,
        'appid': api_token,
        'units': 'metric'
    }   
    responese = requests.get(url,params=params)
    data = responese.json()
    return data

def main():
    parser = argparse.ArgumentParser(description="Wheater check program: ")
    parser.add_argument('City',help="Name of the city for information: ")
    parser.add_argument('--option','-o',default="",choices=['temperature','cloud cover','humidity','speed_wind'],help="weather information option to display: ")
    args = parser.parse_args()
    city = args(city)
    option = args.option
    data = weather_check(city)
    if option == "":
        print(weather_check(data))
    if option == "temperature":
        print(f"Weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
    elif option == "pressure":
        print(f"Weather in {data['name']}:")
        print(f"Pressure: {data['main']['pressure']} hPa")
    elif option == "humidity":
        print(f"Weather in {data['name']}:")
        print(f"Humidity: {data['main']['humidity']}%")
    elif option == "wind_speed":
        print(f"Weather in {data['name']}:")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    


if __name__ == '__main__':
    main()