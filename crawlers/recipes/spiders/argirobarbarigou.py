from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..item_loaders import (RecipyItemLoader as ArgiroBarbarigouItemLoader, IngredientItemLoader)


class ArgiroBarbarigouSpider(CrawlSpider):

    name = "argirobarbarigou"

    start_urls = [
        'https://www.argiro.gr/recipe-category/vasiko-sistatiko/',
    ]

    # callback='parse_category',
    rules = (
        # taking the link for the categories
        Rule(
            LinkExtractor(allow='recipe-category/', restrict_xpaths=('//*[@class="marg-tb-10"]/a[1]',))
        ),
        Rule(
            LinkExtractor(allow=(), restrict_xpaths=('//*[@class="next-set-posts"]/a',))
        ),
        Rule(
            LinkExtractor(allow=(),
                          restrict_xpaths=('//*[@class="tax-list-item uk-text-center matchHeight"]/a[1]',)),
            callback='parse'
        ),
    )

    # DEPRECATED
    def parse_category(self, response):
        current_category = response.xpath('//h1/text()').get().split(' ')[0]  # TODO: better parse here
        recipes_url = response.xpath('//*[@class="tax-list-item uk-text-center matchHeight"]/a[1]/@href')
        for r_url in recipes_url:
            yield response.follow(r_url, callback=self.parse, meta={"current_category": current_category})

        next_page = response.xpath('//*[@class="next-set-posts"]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_category)

    def parse(self, response, **kwargs):
        item = ArgiroBarbarigouItemLoader(response=response)

        # category extraction
        recipe_path = response.xpath('//*[@typeof="v:Breadcrumb"]')
        category = recipe_path[len(recipe_path) - 1].xpath('a/text()').get()

        item.add_value('url', response.url)
        item.add_xpath('name', '//h1/span/text()')
        item.add_value('category', category)
        item.add_xpath('instructions', '//*[@itemprop="recipeInstructions"]/p/text()')

        ingredients = response.xpath('//*[@itemprop="recipeIngredient"]').getall()
        for ingredient in ingredients:
            ingredient = Selector(text=ingredient)
            il = IngredientItemLoader(selector=ingredient)
            il.add_xpath('ingredient', '//text()')
            item.add_value('ingredients', il.load_item())

        return item.load_item()


