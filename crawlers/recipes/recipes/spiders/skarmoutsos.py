import time

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..item_loaders import RecipyItemLoader as SkarmoutsosItemLoader


class SkarmoutsosSpider(CrawlSpider):

    name = "skarmoutsos"

    start_urls = [
        'https://www.dimitrisskarmoutsos.gr/sintages'
    ]
    
    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@class="next"]',))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@class="recipeBox"]/a[1]',)), callback='parse')
    )


    def parse(self, response):
        item = SkarmoutsosItemLoader(response=response)
        item.add_xpath('name', '//*[@id="recipeMain"]/div/h1/text()')
        return item.load_item()


        # start_tm = time.time()
        # page_recipies = response.xpath('//*[@id="recipesCategArea"]/div[*]')
        # for recipie in page_recipies:
        #     yield {
        #         'title': recipie.css('a span.recipeTitle::text').get(),
        #         'url': recipie.css('a::attr(href)').get()
        #     }
        

        # next_route = response.xpath('//*[@class="next"]/@href').get()
        # print("Next Route ~~> ", next_route)
        # if next_route is not None:
        #     next_page = "https://www.dimitrisskarmoutsos.gr/" + next_route
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callable=self.parse)


        # duration = time.time() - start_tm
        # print("Complete. Took: {:.2f}".format(duration))