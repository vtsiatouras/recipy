from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, Identity, Join, MapCompose, TakeFirst
from scrapy.selector import Selector

from .items import Recipe


class RecipyItemLoader(ItemLoader):

    default_item_class = Recipe
    default_selector_class = Selector
    default_input_processor = MapCompose(lambda x: x.strip())
    default_output_processor = Compose(TakeFirst())
    response_status_in = Identity()
    response_status_out = Compose(TakeFirst())

    # Add function to clean text
    name_out = Compose(TakeFirst(), lambda x: x.strip())
    category_out = Compose(TakeFirst(), lambda x: x.strip())
    description_in = MapCompose(lambda x: x.strip())
    description_out = Compose(Join(), lambda x: x.strip())
