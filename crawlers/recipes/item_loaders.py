from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, Identity, Join, MapCompose, TakeFirst
from scrapy.selector import Selector

from .items import Recipe, Ingredient


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
    instructions_in = MapCompose(lambda x: x.strip())
    instructions_out = Compose(Join(), lambda x: x.strip())

    ingredients_in = Identity()
    ingredients_out = Compose(lambda ingredients: [dict(i) for i in ingredients if i])


class IngredientItemLoader(ItemLoader):
    default_item_class = Ingredient
    default_selector_class = Selector
    ingredient_in = MapCompose(lambda x: x.strip())
    ingredient_out = Compose(Join(), lambda x: x.strip())
