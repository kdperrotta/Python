"""
A work in progress. I need to perfect my regex statement and map out what I want to do once I have all the information scraped.
"""

from bs4 import BeautifulSoup
import requests
import re

url = "https://www.allrecipes.com/recipe/6698/moms-zucchini-bread/"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

def gather_ingredients(url):
    raw_ingredients = doc.findAll(class_ = "ingredients-item-name")
    formatted_ingredients = []

    for ingredient in raw_ingredients:
        formatted_ingredient = (str(ingredient)[54:-8].rstrip())
        formatted_ingredients.append(formatted_ingredient)
    print(formatted_ingredients)

    regex = r"(\d* ?[\u00BC-\u00BE\u2150-\u215E]* ?\d?) ([a-zA-Z]+) ?([a-zA-Z,\- ]+ ?[a-zA-Z,]*)?"
    ingredient_list = re.findall(regex, str(formatted_ingredients))


gather_ingredients(url)
