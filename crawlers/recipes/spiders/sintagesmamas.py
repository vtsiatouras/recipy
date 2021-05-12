from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..item_loaders import (RecipyItemLoader as SintagesmamasItemLoader, IngredientItemLoader)


class SintagesmamasSpider(CrawlSpider):

    name = "sintagesmamas"

    start_urls = [
        'https://www.sintagesmamas.com'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*//ul[@class="recipe-categories"]//*//a',))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*//li[@class="pager__item--next"]//a', ))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*//h3[@class="node__title"]//a',)), callback='parse')
    )

    base_url = 'https://www.sintagesmamas.com'

    def parse(self, response, **kwargs):
        item = SintagesmamasItemLoader(response=response)

        item.add_value('recipe_url', response.url)
        item.add_xpath('name', '//*/h1[@class="title"]/span/text()')
        item.add_xpath('category', '//*/div[contains(@class, "field--name-field-category")]//a/text()')
        item.add_xpath('instructions',
                       '//*/div[contains(@class, "field--name-field-instructions")]/div[@class="field__item"]/p/text()')

        img_path = response.xpath('//*/img[@typeof="foaf:Image"]/@src').get()
        item.add_value('image_url', self.base_url + img_path if img_path else None)

        ingredients = response.xpath('//*/div[contains(@class, "field--name-field-ingredients")]//li').getall()
        for ingredient in ingredients:
            ingredient = Selector(text=ingredient)
            il = IngredientItemLoader(selector=ingredient)
            il.add_xpath('ingredient', '//text()')
            item.add_value('ingredients', il.load_item())

        return item.load_item()