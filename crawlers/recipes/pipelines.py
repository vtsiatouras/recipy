# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from django.apps import apps
from django.db import transaction


class RecipesPipeline:

    def process_item(self, item, spider):
        return item


class DBStoragePipeline:

    def process_item(self, item, spider):
        """
        Persists recipe item in the database. This method is called for every scraped item.
        :param item: scrapy.Item, required
        :param spider: scrapy.Spider, required
        :return: scrapy.Item
        """
        site_model = apps.get_model('recipy_api', 'Site')
        recipe_model = apps.get_model('recipy_api', 'Recipe')
        ingredient_model = apps.get_model('recipy_api', 'Ingredient')

        # Make sure that all queries will be executed in one single transaction
        with transaction.atomic():
            site_obj, _ = site_model.objects.get_or_create(name=spider.name, url=spider.base_url)

            # Check if recipe already exists in database
            try:
                _ = recipe_model.objects.get(url=item['recipe_url'], name=item['name'], category=item['category'])

                # If no exception is raised ignore the storing procedure
                return item
            except recipe_model.DoesNotExist:
                stored_recipe = recipe_model.objects.create(url=item['recipe_url'],
                                                            name=item['name'],
                                                            category=item['category'],
                                                            instructions=item.get('instructions', None),
                                                            image_url=item.get('image_url', None),
                                                            site=site_obj)

                ingredients_ids = []
                for ingredient in item['ingredients']:
                    ingredient_obj, _ = ingredient_model.objects.get_or_create(description=ingredient['ingredient'])
                    ingredients_ids.append(ingredient_obj.id)

                stored_recipe.ingredients.add(*ingredients_ids)

        return item
