# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Recipe(Item):
    recipe_url = Field()
    name = Field()
    instructions = Field()
    category = Field()
    ingredients = Field()
    image_url = Field()


class Ingredient(Item):
    ingredient = Field()
