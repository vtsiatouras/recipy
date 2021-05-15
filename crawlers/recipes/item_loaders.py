from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, Identity, Join, MapCompose, TakeFirst
from scrapy.selector import Selector

from .items import Recipe, Ingredient


class RecipyItemLoader(ItemLoader):

    default_item_class = Recipe
    default_selector_class = Selector
    default_input_processor = MapCompose(lambda x: clean_text(x))
    default_output_processor = Compose(TakeFirst())
    response_status_in = Identity()
    response_status_out = Compose(TakeFirst())

    # Add function to clean text
    name_out = Compose(TakeFirst(), lambda x: clean_text(x))
    category_out = Compose(TakeFirst(), lambda x: clean_text(x))
    instructions_in = MapCompose(lambda x: clean_text(x))
    instructions_out = Compose(Join(), lambda x: clean_text(x) if x else None)

    ingredients_in = Identity()
    ingredients_out = Compose(lambda ingredients: [dict(i) for i in ingredients if i])


class IngredientItemLoader(ItemLoader):
    default_item_class = Ingredient
    default_selector_class = Selector
    ingredient_in = MapCompose(lambda x: clean_text(x))
    ingredient_out = Compose(Join(), lambda x: clean_text(x))


def clean_text(txt):
    return txt.replace(u'\xa0', ' ').strip()
