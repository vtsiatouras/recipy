from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..item_loaders import (RecipyItemLoader as ArgiroBarbarigouItemLoader, IngredientItemLoader)


class ArgiroBarbarigouSpider(CrawlSpider):

    name = "argirobarbarigou"

    start_urls = [
        'https://www.argiro.gr/recipe-category/pota-rofimata/'
        'https://www.argiro.gr/recipe-category/vasiko-sistatiko/',
        'https://www.argiro.gr/recipe-category/nisiotikes-sintages/',
        'https://www.argiro.gr/recipe-category/pites-almires-tartes/',
        'https://www.argiro.gr/recipe-category/gluka/',
        'https://www.argiro.gr/recipe-category/eidiki-diatrofi/',
        'https://www.argiro.gr/recipe-category/nisiotikes-sintages/'
    ]

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

    base_url = 'https://www.argiro.gr'

    def parse(self, response, **kwargs):
        item = ArgiroBarbarigouItemLoader(response=response)

        # category extraction
        recipe_path = response.xpath('//*[@typeof="v:Breadcrumb"]')
        category = recipe_path[len(recipe_path) - 1].xpath('a/text()').get()

        item.add_value('recipe_url', response.url)
        item.add_xpath('name', '//h1/span/text()')
        item.add_value('category', category)
        item.add_xpath('instructions',
                       '//*[@itemprop="recipeInstructions"]/*[not(@class="theiaStickySidebar")]//text()')

        img_path = response.xpath('//*[@itemprop="image"]/@src').get()
        item.add_value('image_url', img_path if img_path else None)

        ingredients = response.xpath('//*[@itemprop="recipeIngredient"]').getall()
        for ingredient in ingredients:
            ingredient = Selector(text=ingredient)
            il = IngredientItemLoader(selector=ingredient)
            il.add_xpath('ingredient', '//text()')
            item.add_value('ingredients', il.load_item())

        return item.load_item()
