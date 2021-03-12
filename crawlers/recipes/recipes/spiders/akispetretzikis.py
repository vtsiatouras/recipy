from time import sleep
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..item_loaders import RecipyItemLoader as AkisPetretzikisItemLoader
from crawlers.recipes.tools import get_filepath
from ..settings import LOGS_DIRECTORY, SELENIUM_WEBDRIVER_LOGS


class AkisPetretzikisSpider(CrawlSpider):

    name = 'akispetretzikis'
    allowed_domains = ['akispetretzikis.com']

    start_urls = [
        'https://akispetretzikis.com/el/categories/p/kathgories-syntagwn',
        'https://akispetretzikis.com/el/categories/p/eidos-geymatos',
        'https://akispetretzikis.com/el/categories/p/ey-zhn',
        'https://akispetretzikis.com/el/categories/p/eidikh-diaita',
        'https://akispetretzikis.com/el/categories/p/giortina'
    ]

    rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="more"]/a',)), callback='parse', follow=True),)

    def __init__(self, *args, **kwargs):
        super(AkisPetretzikisSpider, self).__init__(*args, **kwargs)
        # create a new instance of Chrome driver
        options = Options()
        options.add_argument("--headless")  # run headless
        options.add_argument("--kiosk")  # run in full screen mode
        self.driver = webdriver.Chrome(executable_path=get_filepath('recipes/selenium_drivers', 'chromedriver'),
                                       options=options,
                                       service_log_path=LOGS_DIRECTORY + '/' + SELENIUM_WEBDRIVER_LOGS)

    def parse(self, response, **kwargs):
        """
        :param response: response module, required
        :return: yield recipe urls
        """
        self.driver.get(response.url)
        sleep(5)

        # Click Decline to GDPR consent pop-up in order to disappear
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll"]'))
            ).click()
        except TimeoutException:
            pass

        # Expand page to view all recipes in this category page
        while True:
            try:
                WebDriverWait(self.driver, 20).\
                    until(EC.element_to_be_clickable((By.XPATH, '//*[@id="next_page_link"]/a'))).click()
                sleep(5)
            except TimeoutException:
                break

        # Get recipes URLs
        recipe_links = self.driver.find_elements_by_xpath('//*[@class="v_box recipe-card"]/'
                                                          'div[@class="texts"]/h4/a[@href]')
        for link in recipe_links:
            yield Request(link.get_attribute("href"), callback=self.parse_recipe)

    @staticmethod
    def parse_recipe(response):
        """
        :param response: response module, required
        :return: yield recipe item
        """
        item = AkisPetretzikisItemLoader(response=response)

        item.add_value('url', response.url)
        item.add_xpath('name', '//*[@id="recipe"]//h1[@class="title"]/text()')
        item.add_xpath('description', '//*[@id="recipe"]//div[@class="text"]//text()')
        item.add_xpath('category', '//*[@id="recipe"]//div[@class="recipe-breadcrumb"]/a/text()')

        return item.load_item()

    def closed(self, reason):

        self.driver.quit()
        self.driver = None