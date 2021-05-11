from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..item_loaders import (RecipyItemLoader as SkarmoutsosItemLoader, IngredientItemLoader)


class SkarmoutsosSpider(CrawlSpider):

    name = "skarmoutsos"

    start_urls = [
        'https://www.dimitrisskarmoutsos.gr/sintages'
    ]
    
    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@class="next"]',))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@class="recipeBox"]/a[1]',)), callback='parse')
    )

    base_url = 'https://www.dimitrisskarmoutsos.gr/'

    def parse(self, response, **kwargs):
        item = SkarmoutsosItemLoader(response=response)

        item.add_value('recipe_url', response.url)
        item.add_xpath('name', '//*[@id="recipeMain"]/div/h1/text()')
        item.add_xpath('category', '//*[@id="recCategoryBox"]/a/span/text()')
        item.add_xpath('instructions', '//*[@id="recipeMainRight"]/div[1]/p/text()')

        img_path = response.xpath('//*[@id="recipeMainLeft"]/img/@src').get()
        item.add_value('image_url', self.base_url + img_path if img_path else None)

        ingredients = response.xpath('//*[@id="ingredBox"]/*/li').getall()
        for ingredient in ingredients:
            ingredient = Selector(text=ingredient)
            il = IngredientItemLoader(selector=ingredient)
            il.add_xpath('ingredient', '//text()')
            item.add_value('ingredients', il.load_item())

        return item.load_item()
