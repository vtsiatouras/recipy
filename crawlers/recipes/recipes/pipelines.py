# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class RecipesPipeline:
    def process_item(self, item, spider):
        return item


class DBStoragePipeline:
    # Create DB session here
    # def __init__(self) -> None:
    #   Add code here

    # def process_item(self, item, spider):
    #     """
    #     Persists recipe item in the database. This method is called for every scraped item.
    #     :param item: scrapy.Item, required
    #     :param spider: scrapy.Spider, required
    #     :return: scrapy.Item
    #     """
    #   Add code here

    # def close_spider(self, spider) -> None:
    #     """
    #     :param spider: Spider object
    #     :return: None
    #     """
    #    Add code here (close DB session)

    pass
