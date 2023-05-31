"""Prints NASA API response to terminal, does not send email."""

from secrets import nasa_api_key
import requests

nasa_url = "https://api.nasa.gov/planetary/apod?api_key={}".format(nasa_api_key)

response = requests.get(nasa_url).json()

for key, value in response.items():
    print(key + " // " + value)
