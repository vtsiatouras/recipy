from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..item_loaders import (RecipyItemLoader as SuntagesmeItemLoader, IngredientItemLoader)


class SuntagesmeSpider(CrawlSpider):

    name = "suntagesme"

    start_urls = [
        'https://www.syntages.me/syntages'
    ]
    
    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*//div[@class="pag2_n pag2_n_r"]/a[1]',))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@class="si_list1"]/a[1]',)), callback='parse')
    )

    base_url = 'https://www.syntages.me'

    def parse(self, response, **kwargs):
        item = SuntagesmeItemLoader(response=response)

        item.add_value('recipe_url', response.url)
        item.add_xpath('name', '//*[@class="si_titlos"]/h1/text()')
        item.add_xpath('category', '//*[@id="main"]/div[1]/div/ul/li[2]/a/text()')
        item.add_xpath('instructions', '//*[@itemprop="recipeInstructions"]/ul/li/text()')

        # In this site image url can be None in some recipes because it may has video instead of image
        img_path = response.xpath('//*[@class="si_photo tac"]/img/@src').get()
        item.add_value('image_url', self.base_url + img_path if img_path else None)

        ingredients = response.xpath('//*[@class="si_ylika_holder"]//li').getall()
        for ingredient in ingredients:
            ingredient = Selector(text=ingredient)
            il = IngredientItemLoader(selector=ingredient)
            il.add_xpath('ingredient', '//text()')
            item.add_value('ingredients', il.load_item())

        return item.load_item()
