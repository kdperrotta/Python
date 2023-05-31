from secrets import openweather_api_key
import requests
import time

filename = "user_coordinates_for_forecast.txt"
APIkey = openweather_api_key


def get_coordinates(api_key, city):
    urlcoord = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    responsecoord = requests.get(urlcoord).json()
    city_lat = str(responsecoord["coord"]["lat"])
    city_long = str(responsecoord["coord"]["lon"])
    with open(filename, "w+") as file_object:
        file_object.write(city_lat + "\n")
        file_object.write(city_long)

def format_temp_C(temp):
    temp = round((temp - 273.15), 1)
    return temp

def format_temp_F(temp):
    temp = round((temp * 1.8) - 459.67)
    return temp

def format_date(raw_date):
    nice_date = (time.ctime(raw_date)[:8]) + (time.ctime(raw_date)[8:10])
    return nice_date

def get_forecast_temp(api_key, city):
    response = requests.get(url).json()
    day_1_temp = response["daily"][0]["temp"]["day"]
    day_2_temp = response["daily"][1]["temp"]["day"]
    day_3_temp = response["daily"][2]["temp"]["day"]
    day_4_temp = response["daily"][3]["temp"]["day"]
    day_5_temp = response["daily"][4]["temp"]["day"]
    day_6_temp = response["daily"][5]["temp"]["day"]
    day_7_temp = response["daily"][6]["temp"]["day"]
    day_8_temp = response["daily"][7]["temp"]["day"]

    temp_message = "The temperature in " + cityname + " for: \n"
    temp_message += "\nToday: \n" + str(format_temp_F(day_1_temp)) + "°F\n" + str(format_temp_C(day_1_temp)) + "°C\n"
    temp_message += "\nTomorrow: \n" + str(format_temp_F(day_2_temp)) + "°F\n" + str(format_temp_C(day_2_temp)) + "°C\n"
    temp_message += "\n" + format_date(response["daily"][2]["dt"]) + ":\n" + str(format_temp_F(day_3_temp)) + "°F\n" + str(format_temp_C(day_3_temp)) + "°C\n"
    temp_message += "\n" + format_date(response["daily"][3]["dt"]) + ":\n" + str(format_temp_F(day_4_temp)) + "°F\n" + str(format_temp_C(day_4_temp)) + "°C\n"
    temp_message += "\n" + format_date(response["daily"][4]["dt"]) + ":\n" + str(format_temp_F(day_5_temp)) + "°F\n" + str(format_temp_C(day_5_temp)) + "°C\n"
    temp_message += "\n" + format_date(response["daily"][5]["dt"]) + ":\n" + str(format_temp_F(day_6_temp)) + "°F\n" + str(format_temp_C(day_6_temp)) + "°C\n"
    temp_message += "\n" + format_date(response["daily"][6]["dt"]) + ":\n" + str(format_temp_F(day_7_temp)) + "°F\n" + str(format_temp_C(day_7_temp)) + "°C\n"
    temp_message += "\n" + format_date(response["daily"][7]["dt"]) + ":\n" + str(format_temp_F(day_8_temp)) + "°F\n" + str(format_temp_C(day_8_temp)) + "°C\n"
    print(temp_message)

def get_forecast_conditions(api_key, city):
    response = requests.get(url).json()
    day_1_condition = response["daily"][0]["weather"][0]["main"]
    day_2_condition = response["daily"][1]["weather"][0]["main"]
    day_3_condition = response["daily"][2]["weather"][0]["main"]
    day_4_condition = response["daily"][3]["weather"][0]["main"]
    day_5_condition = response["daily"][4]["weather"][0]["main"]
    day_6_condition = response["daily"][5]["weather"][0]["main"]
    day_7_condition = response["daily"][6]["weather"][0]["main"]
    day_8_condition = response["daily"][7]["weather"][0]["main"]

    cond_message = "The weather conditions in " + cityname + " for: \n"
    cond_message += "\nToday: \n" + day_1_condition
    cond_message += "\n\nTomorrow: \n" + day_2_condition
    cond_message += "\n\n" + format_date(response["daily"][2]["dt"]) + ":\n" + day_3_condition
    cond_message += "\n\n" + format_date(response["daily"][3]["dt"]) + ":\n" + day_4_condition
    cond_message += "\n\n" + format_date(response["daily"][4]["dt"]) + ":\n" + day_5_condition
    cond_message += "\n\n" + format_date(response["daily"][5]["dt"]) + ":\n" + day_6_condition
    cond_message += "\n\n" + format_date(response["daily"][6]["dt"]) + ":\n" + day_7_condition
    cond_message += "\n\n" + format_date(response["daily"][7]["dt"]) + ":\n" + day_8_condition
    print(cond_message)

def get_forecast_descriptions(api_key, city):
    response = requests.get(url).json()
    day_1_description = response["daily"][0]["weather"][0]["description"]
    day_2_description = response["daily"][1]["weather"][0]["description"]
    day_3_description = response["daily"][2]["weather"][0]["description"]
    day_4_description = response["daily"][3]["weather"][0]["description"]
    day_5_description = response["daily"][4]["weather"][0]["description"]
    day_6_description = response["daily"][5]["weather"][0]["description"]
    day_7_description = response["daily"][6]["weather"][0]["description"]
    day_8_description = response["daily"][7]["weather"][0]["description"]

    desc_message = "The weather description in " + cityname + " for: \n"
    desc_message += "\nToday: \n" + day_1_description.title()
    desc_message += "\n\nTomorrow: \n" + day_2_description.title()
    desc_message += "\n\n" + format_date(response["daily"][2]["dt"]) + ":\n" + day_3_description.title()
    desc_message += "\n\n" + format_date(response["daily"][3]["dt"]) + ":\n" + day_4_description.title()
    desc_message += "\n\n" + format_date(response["daily"][4]["dt"]) + ":\n" + day_5_description.title()
    desc_message += "\n\n" + format_date(response["daily"][5]["dt"]) + ":\n" + day_6_description.title()
    desc_message += "\n\n" + format_date(response["daily"][6]["dt"]) + ":\n" + day_7_description.title()
    desc_message += "\n\n" + format_date(response["daily"][7]["dt"]) + ":\n" + day_8_description.title()
    print(desc_message)

#just an example, not writing the whole thing
def get_forecast_pop(api_key, city):
    response = requests.get(url).json()
    day_1_pop = (response["daily"][0]["pop"]) * 100
    format_day_1_pop = str(int(day_1_pop)) + "%"
    print(format_day_1_pop)

def get_full_forecast(api_key, city):

    while True:
        if city == "q":
            break
        else:
            coordinates = []
            get_coordinates(api_key, city.title())
            with open(filename, "r") as file_object:
                coordsfile = file_object.readlines()
                for line in coordsfile:
                    coordinates.append(line.rstrip())
                lat = coordinates[0]
                lon = coordinates[1]
                url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}"
                url += f"&exclude={None}&appid={api_key}"
                response = requests.get(url).json()
            break

    day_1_temp = response["daily"][0]["temp"]["day"]
    day_1_condition = response["daily"][0]["weather"][0]["main"]
    day_1_description = response["daily"][0]["weather"][0]["description"]
    day_1_pop = (response["daily"][0]["pop"]) * 100
    format_day_1_pop = str(int(day_1_pop)) + "%"
    day_1_high = response["daily"][0]["temp"]["max"]
    day_1_low = response["daily"][0]["temp"]["min"]

    day_2_temp = response["daily"][1]["temp"]["day"]
    day_2_condition = response["daily"][1]["weather"][0]["main"]
    day_2_description = response["daily"][1]["weather"][0]["description"]
    day_2_pop = (response["daily"][1]["pop"]) * 100
    format_day_2_pop = str(int(day_2_pop)) + "%"
    day_2_high = response["daily"][1]["temp"]["max"]
    day_2_low = response["daily"][1]["temp"]["min"]

    day_3_temp = response["daily"][2]["temp"]["day"]
    day_3_condition = response["daily"][2]["weather"][0]["main"]
    day_3_description = response["daily"][2]["weather"][0]["description"]
    day_3_pop = (response["daily"][2]["pop"]) * 100
    format_day_3_pop = str(int(day_3_pop)) + "%"
    day_3_high = response["daily"][2]["temp"]["max"]
    day_3_low = response["daily"][2]["temp"]["min"]

    day_4_temp = response["daily"][3]["temp"]["day"]
    day_4_condition = response["daily"][3]["weather"][0]["main"]
    day_4_description = response["daily"][3]["weather"][0]["description"]
    day_4_pop = (response["daily"][3]["pop"]) * 100
    format_day_4_pop = str(int(day_4_pop)) + "%"
    day_4_high = response["daily"][3]["temp"]["max"]
    day_4_low = response["daily"][3]["temp"]["min"]

    day_5_temp = response["daily"][4]["temp"]["day"]
    day_5_condition = response["daily"][4]["weather"][0]["main"]
    day_5_description = response["daily"][4]["weather"][0]["description"]
    day_5_pop = (response["daily"][4]["pop"]) * 100
    format_day_5_pop = str(int(day_5_pop)) + "%"
    day_5_high = response["daily"][4]["temp"]["max"]
    day_5_low = response["daily"][4]["temp"]["min"]

    day_6_temp = response["daily"][5]["temp"]["day"]
    day_6_condition = response["daily"][5]["weather"][0]["main"]
    day_6_description = response["daily"][5]["weather"][0]["description"]
    day_6_pop = (response["daily"][5]["pop"]) * 100
    format_day_6_pop = str(int(day_6_pop)) + "%"
    day_6_high = response["daily"][5]["temp"]["max"]
    day_6_low = response["daily"][5]["temp"]["min"]

    day_7_temp = response["daily"][6]["temp"]["day"]
    day_7_condition = response["daily"][6]["weather"][0]["main"]
    day_7_description = response["daily"][6]["weather"][0]["description"]
    day_7_pop = (response["daily"][6]["pop"]) * 100
    format_day_7_pop = str(int(day_7_pop)) + "%"
    day_7_high = response["daily"][6]["temp"]["max"]
    day_7_low = response["daily"][6]["temp"]["min"]

    day_8_temp = response["daily"][7]["temp"]["day"]
    day_8_condition = response["daily"][7]["weather"][0]["main"]
    day_8_description = response["daily"][7]["weather"][0]["description"]
    day_8_pop = (response["daily"][7]["pop"]) * 100
    format_day_8_pop = str(int(day_8_pop)) + "%"
    day_8_high = response["daily"][7]["temp"]["max"]
    day_8_low = response["daily"][7]["temp"]["min"]

    fore_message = "The forecast for " + city.title() + " for: \n"
    fore_message += "\nToday: \n"
    fore_message += "Forcasted Temperature: " + str(format_temp_F(day_1_temp)) + "°F, " + str(format_temp_C(day_1_temp)) + "°C\n"
    fore_message += "High: " + str(format_temp_F(day_1_high)) + "°F, " + str(format_temp_C(day_1_high)) + "°C\n"
    fore_message += "Low: " + str(format_temp_F(day_1_low)) + "°F, " + str(format_temp_C(day_1_low)) + "°C\n"
    fore_message += "Weather Conditions: " + day_1_condition
    fore_message += "\nDescription: " + day_1_description.title()
    fore_message += "\nChance of Precipitation: " + format_day_1_pop

    fore_message += "\n\nTomorrow: \n"
    fore_message += "Forcasted Temperature: " + str(format_temp_F(day_2_temp)) + "°F, " + str(format_temp_C(day_2_temp)) + "°C\n"
    fore_message += "High: " + str(format_temp_F(day_2_high)) + "°F, " + str(format_temp_C(day_2_high)) + "°C\n"
    fore_message += "Low: " + str(format_temp_F(day_2_low)) + "°F, " + str(format_temp_C(day_2_low)) + "°C\n"
    fore_message += "Weather Conditions: " + day_2_condition
    fore_message += "\nDescription: " + day_2_description.title()
    fore_message += "\nChance of Precipitation: " + format_day_2_pop

    fore_message += "\n\n" + format_date(response["daily"][2]["dt"]) + ":"
    fore_message += "\nForcasted Temperature: " + str(format_temp_F(day_3_temp)) + "°F, " + str(format_temp_C(day_3_temp)) + "°C\n"
    fore_message += "High: " + str(format_temp_F(day_3_high)) + "°F, " + str(format_temp_C(day_3_high)) + "°C\n"
    fore_message += "Low: " + str(format_temp_F(day_3_low)) + "°F, " + str(format_temp_C(day_3_low)) + "°C\n"
    fore_message += "Weather Conditions: " + day_3_condition
    fore_message += "\nDescription: " + day_3_description.title()
    fore_message += "\nChance of Precipitation: " + format_day_3_pop

    fore_message += "\n\n" + format_date(response["daily"][3]["dt"]) + ":"
    fore_message += "\nForcasted Temperature: " + str(format_temp_F(day_4_temp)) + "°F, " + str(format_temp_C(day_4_temp)) + "°C\n"
    fore_message += "High: " + str(format_temp_F(day_4_high)) + "°F, " + str(format_temp_C(day_4_high)) + "°C\n"
    fore_message += "Low: " + str(format_temp_F(day_4_low)) + "°F, " + str(format_temp_C(day_4_low)) + "°C\n"
    fore_message += "Weather Conditions: " + day_4_condition
    fore_message += "\nDescription: " + day_4_description.title()
    fore_message += "\nChance of Precipitation: " + format_day_4_pop

    fore_message += "\n\n" + format_date(response["daily"][4]["dt"]) + ":"
    fore_message += "\nForcasted Temperature: " + str(format_temp_F(day_5_temp)) + "°F, " + str(format_temp_C(day_5_temp)) + "°C\n"
    fore_message += "High: " + str(format_temp_F(day_5_high)) + "°F, " + str(format_temp_C(day_5_high)) + "°C\n"
    fore_message += "Low: " + str(format_temp_F(day_5_low)) + "°F, " + str(format_temp_C(day_5_low)) + "°C\n"
    fore_message += "Weather Conditions: " + day_5_condition
    fore_message += "\nDescription: " + day_5_description.title()
    fore_message += "\nChance of Precipitation: " + format_day_5_pop

    fore_message += "\n\n" + format_date(response["daily"][5]["dt"]) + ":"
    fore_message += "\nForcasted Temperature: " + str(format_temp_F(day_6_temp)) + "°F, " + str(format_temp_C(day_6_temp)) + "°C\n"
    fore_message += "High: " + str(format_temp_F(day_6_high)) + "°F, " + str(format_temp_C(day_6_high)) + "°C\n"
    fore_message += "Low: " + str(format_temp_F(day_6_low)) + "°F, " + str(format_temp_C(day_6_low)) + "°C\n"
    fore_message += "Weather Conditions: " + day_6_condition
    fore_message += "\nDescription: " + day_6_description.title()
    fore_message += "\nChance of Precipitation: " + format_day_6_pop

    fore_message += "\n\n" + format_date(response["daily"][6]["dt"]) + ":"
    fore_message += "\nForcasted Temperature: " + str(format_temp_F(day_7_temp)) + "°F, " + str(format_temp_C(day_7_temp)) + "°C\n"
    fore_message += "High: " + str(format_temp_F(day_7_high)) + "°F, " + str(format_temp_C(day_7_high)) + "°C\n"
    fore_message += "Low: " + str(format_temp_F(day_7_low)) + "°F, " + str(format_temp_C(day_7_low)) + "°C\n"
    fore_message += "Weather Conditions: " + day_7_condition
    fore_message += "\nDescription: " + day_7_description.title()
    fore_message += "\nChance of Precipitation: " + format_day_7_pop

    fore_message += "\n\n" + format_date(response["daily"][7]["dt"]) + ":"
    fore_message += "\nForcasted Temperature: " + str(format_temp_F(day_8_temp)) + "°F, " + str(format_temp_C(day_8_temp)) + "°C\n"
    fore_message += "High: " + str(format_temp_F(day_8_high)) + "°F, " + str(format_temp_C(day_8_high)) + "°C\n"
    fore_message += "Low: " + str(format_temp_F(day_8_low)) + "°F, " + str(format_temp_C(day_8_low)) + "°C\n"
    fore_message += "Weather Conditions: " + day_8_condition
    fore_message += "\nDescription: " + day_8_description.title()
    fore_message += "\nChance of Precipitation: " + format_day_8_pop

    print(fore_message)


get_full_forecast(openweather_api_key, city = input("Please enter a city name and country code: "))
