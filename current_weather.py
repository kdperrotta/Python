from secrets import openweather_api_key
import requests

cityname = input("Please enter a city name and country code: ")

def get_current_temp(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    current_temp = response["main"]["temp"]
    temp_F = round((current_temp * 1.8) - 459.67)
    temp_C = round((current_temp - 273.15), 2)
    temp_message = "The temperature in " + cityname + " is currently: \n"
    temp_message += str(temp_F) + "°F\n" + str(temp_C) + "°C"
    print(temp_message)

def get_min_max_temp(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    min_temp = response["main"]["temp_min"]
    min_temp_F = round(((min_temp * 1.8) - 459.67), 1)
    min_temp_C = round((min_temp - 273.15), 2)
    max_temp = response["main"]["temp_max"]
    max_temp_F = round(((max_temp * 1.8) - 459.67), 1)
    max_temp_C = round((max_temp - 273.15), 2)
    minmax_message = "The maximum temperature in " + city + " today is: \n"
    minmax_message += str(max_temp_F) + "°F\n" + str(max_temp_C) + "°C\n"
    minmax_message += "The minimum temperature in " + city + " today is: \n"
    minmax_message += str(min_temp_F) + "°F\n" + str(min_temp_C) + "°C\n"
    print(minmax_message)

def get_weather_main(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    weather_main = response["weather"][0]["main"]
    print("The current weather in " + city + " is: " + weather_main)

def get_current_weather_overview(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()

    min_temp = response["main"]["temp_min"]
    min_temp_F = round(((min_temp * 1.8) - 459.67), 1)
    min_temp_C = round((min_temp - 273.15), 2)
    max_temp = response["main"]["temp_max"]
    max_temp_F = round(((max_temp * 1.8) - 459.67), 1)
    max_temp_C = round((max_temp - 273.15), 2)

    current_temp = response["main"]["temp"]
    temp_F = round((current_temp * 1.8) - 459.67)
    temp_C = round((current_temp - 273.15), 2)
    weather_main = response["weather"][0]["main"]
    weather_description = response["weather"][0]["description"]

    format_preference = input("Would you like the temperature in °F or °C? ")

    if format_preference.upper() == "F":
        message = "Today's weather in " + city + ":\n"
        message += "Current temperature: \n" + str(temp_F) + "°F\n"
        message += "\nHigh temperature: \n"
        message += str(max_temp_F) + "°F\n"
        message += "\nLow temperature: \n"
        message += str(min_temp_F) + "°F\n"
        message += "\nThe current weather is: " + weather_main + "\n"
        message += "Current weather description: " + weather_description.title() + "\n"

    elif format_preference.upper() == "C":
        message = "Today's weather in " + city + ":\n"
        message += "Current temperature: \n" + str(temp_C) + "°C\n"
        message += "\nHigh temperature: \n"
        message += str(max_temp_C) + "°C\n"
        message += "\nLow temperature: \n"
        message += str(min_temp_C) + "°C\n"
        message += "\nThe current weather is: " + weather_main + "\n"
        message += "Current weather description: " + weather_description.title() + "\n"

    else:
        print("I didn't understand. Please just enter 'C' or 'F'.")
    print(message)


get_current_weather_overview(openweather_api_key, cityname)
