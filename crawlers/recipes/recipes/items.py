# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Recipe(Item):

    url = Field()
    name = Field()
    description = Field()
    category = Field()
