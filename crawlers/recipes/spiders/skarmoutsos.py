from time import sleep
from scrapy import Request, Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..tools import get_filepath
from ..item_loaders import (RecipyItemLoader as SkarmoutsosItemLoader, IngredientItemLoader)


class SkarmoutsosSpider(CrawlSpider):

    name = "skarmoutsos"
    allowed_domains = ["dimitrisskarmoutsos.gr"]

    start_urls = [
        'https://dimitrisskarmoutsos.gr',
    ]

    rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="top-menu"]/li[2]/a',)), callback='parse'),)

    base_url = 'https://dimitrisskarmoutsos.gr/'

    def __init__(self, *args, **kwargs):
        super(SkarmoutsosSpider, self).__init__(*args, **kwargs)
        # create a new instance of Chrome driver
        options = Options()
        options.add_argument("--headless")  # run headless
        options.add_argument("--kiosk")  # run in full screen mode
        print(get_filepath('recipes/selenium_drivers', 'geckodriver'))
        self.driver = webdriver.Firefox(executable_path=get_filepath('/selenium_drivers', 'geckodriver'),
                                        options=options)

    def parse(self, response, **kwargs):
        """
        :param response: response module, required
        :return: yield recipe urls
        """
        self.driver.get(response.url)
        sleep(5)

        # Expand page to view all recipes in this category page
        while True:
            try:
                WebDriverWait(self.driver, 5). \
                    until(EC.element_to_be_clickable((By.XPATH, '//div[@class="dmach-loadmore et_pb_button "]'))).click()
                sleep(5)
            except TimeoutException:
                break

        # Get recipes URLs
        recipe_links = self.driver.find_elements_by_xpath('//div[contains(@class, "recipe-title")]//a')
        for link in recipe_links:
            yield Request(link.get_attribute("href"), callback=self.parse_recipe)

    @staticmethod
    def parse_recipe(response):
        """
        :param response: response module, required
        :return: yield recipe item
        """
        item = SkarmoutsosItemLoader(response=response)

        item.add_value('recipe_url', response.url)
        item.add_xpath('name', '//h1[@itemprop="name"]/text()')
        item.add_xpath('instructions', '//table[@class="dmach-repeater-table"]/tbody/tr/td[2]/text()')
        item.add_xpath('category', '//p[@class="dmach-postmeta-value"]/a[contains(@class, "dmach_cat")]/text()')

        image_url = response.xpath('//meta[@property="og:image"]/@content').get()
        item.add_value('image_url', image_url if image_url else None)

        ingredients = response.xpath('//div[contains(@class, "et_pb_de_mach_acf_item_3_tb_body")]//div[contains(@class, "dmach-acf-item-content")]/p/text()').getall()
        for ingredient in ingredients:
            ingredient = Selector(text=ingredient)
            il = IngredientItemLoader(selector=ingredient)
            il.add_xpath('ingredient', '//text()')
            item.add_value('ingredients', il.load_item())

        return item.load_item()

    def closed(self, reason):

        self.driver.quit()
        self.driver = None
