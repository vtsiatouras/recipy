import time

from scrapy import Request, Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..item_loaders import (RecipyItemLoader as SuntagesmeItemLoader, IngredientItemLoader)


class SuntagesmeSpider(CrawlSpider):

    name = "suntagesme"

    start_urls = [
        'https://www.syntages.me/syntages'
    ]
    
    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="syntages_selides"]/div/div[1]/div[2]/a[1]',))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@class="si_list1"]/a[1]',)), callback='parse')
    )


    def parse(self, response):
        item = SuntagesmeItemLoader(response=response)

        item.add_value('url', response.url)
        item.add_xpath('name', '//*[@class="si_titlos"]/h1/text()')
        item.add_xpath('category', '//*[@id="main"]/div[1]/div/ul/li[2]/a/text()')
        item.add_xpath('instructions', '//*[@itemprop="recipeInstructions"]/ul/li/text()')
        
        ingredients = response.xpath('//*[@class="si_ylika_yliko3"]')
        for ingr in ingredients:
            # construct the ingridient to a text. structure: <text> <a> <text>
            ingredient = ingr.xpath('text()').get()
            ingredient += ingr.xpath('a/text()').get()
            ingredient += ingr.xpath('text()')[1].get() if len(ingr.xpath('text()')) > 1 else ""

            ingredient = Selector(text=ingredient)
            il = IngredientItemLoader(selector=ingredient)
            il.add_xpath('ingredient', '//text()')
            item.add_value('ingredients', il.load_item())

        return item.load_item()
