"""
This command is exectued in the terminal.
EXAMPLE: python3 manage.py create_ads

This command generates an ads.json which in turn
can be loaded in to the db:
EXAMPLE: python3 manage.py loaddata ads.json

It takes a number_of_ads as param.
EXAMPLE python3 manage.py create_ads -n 5000

Each add will generate the following fields:

    TITLE           >> Generated with faker
    SLUG            >> Based on faker TITLE generation
    PRICE           >> Random integer between 10 and 1 000 000
    SELLER          >> Static user, Faker
    CREATED_ON      >> Random date, generated from faker
    SOLD            >> Random True or False
    LOCATION        >> Generated from faker
    CATEGORIES      >> Based on list in APP
    IMAGE           >> Fetched from CC commons API with generated TITLE as search param.
    MAX_PRICE       >> RANDOM or default 1 000 000
    MIN_PRICE       >> RANDOM or default 10

"""

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime


GenAdsVars = {
    "TITLE": "",
    "SLUG": "",
    "PRICE": 0,
    "SELLER": "Faker",
    "CREATED_ON": "",
    "SOLD": False,
    "LOCATION": "",
    "CATEGORIES": [
        'Pianos/keyboards',
        'Guitar/Bass/Amps',
        'Drums/Symbals',
        'Woodwind',
        'Brass',
        'Studio Equipment',
        'Bowed Instruments',
        'Other..',
    ],
    "IMAGE": "",
    "MIN_PRICE": 100,
    "MAX_PRICE": 100000
}


class Provider(faker.providers.BaseProvider):
    """ Setup a faker Base Provider """
    def ecommerce_category(self):
        """ USE app specific categories that are init before run. """
        return self.random_element(GenAdsVars.CATEGORIES)


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('number_of_ads', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        number_of_ads = kwargs.get('number_of_ads')[0]
        print(number_of_ads)
        fake = Faker(["sv_SE"])
        fake.add_provider(Provider)
        for p in range(number_of_ads):
            profile = fake.profile()
            print(profile["username"])