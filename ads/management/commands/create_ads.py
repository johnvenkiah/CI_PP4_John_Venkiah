"""
This command is exectued in the terminal.
EXAMPLE: python3 manage.py create_ads

This command generates an ads.json which in turn
can be loaded in to the db:
EXAMPLE: python3 manage.py loaddata ads.json

It takes a number_of_ads as param.
EXAMPLE python3 manage.py create_ads -n 5000

Each add will generate the following fields:

    TITLE           >> Generated with custom providers faker and wikipedia api.
    SLUG            >> Based on faker TITLE generation
    PRICE           >> Random integer between MIN_PRICE and MAX_PRICE
    SELLER          >> Static user, Faker
    CREATED_ON      >> Random date, generated from faker
    SOLD            >> Random True or False
    LOCATION        >> Generated from faker
    CATEGORIES      >> Based on list in APP
    IMAGE           >> Fetched from CC commons API
                    >> with generated TITLE as search param.
    MAX_PRICE       >> 1 000 000
    MIN_PRICE       >> 100

"""

import faker.providers
import wikipedia
import random
import datetime
import json
from django.core.management.base import BaseCommand
from faker import Faker
import requests

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
    def app_category(self):
        """ USE app specific categories that are init before run. """
        return self.random_element([
            'Pianos/keyboards',
            'Guitar/Bass/Amps',
            'Drums/Symbals',
            'Woodwind',
            'Brass',
            'Studio Equipment',
            'Bowed Instruments',
            'Other..',
        ])

    def wikipedia_search_pianos(self):
        return self.random_element([
            wikipedia.search("Pianos"),
            wikipedia.search('Electric Pianos')
        ])

    def wikipedia_search_guitars(self):
        return self.random_element([
            wikipedia.search("Guitar"),
            wikipedia.search('Bass'),
            wikipedia.search('Amps'),
        ])

    def wikipedia_search_drums(self):
        return self.random_element([
            wikipedia.search("Drums"),
            wikipedia.search('Cymbals'),
        ])

    def wikipedia_search_brass(self):
        return self.random_element([
            wikipedia.search("Brass"),
            wikipedia.search('Trumpet'),
            wikipedia.search('Trombone'),
        ])

    def wikipedia_search_woodwind(self):
        return self.random_element([
            wikipedia.search("Woodwind"),
            wikipedia.search('Tenor Saxophone'),
            wikipedia.search('Clarinett'),
            wikipedia.search('Flute'),
        ])

    def wikipedia_search_studio(self):
        return self.random_element([
            wikipedia.search("Studio"),
            wikipedia.search('Microhpone'),
            wikipedia.search('PA'),
            wikipedia.search('Mixer'),
        ])

    def wikipedia_search_bowed(self):
        return self.random_element([
            wikipedia.search("Cello"),
            wikipedia.search('Violin'),
            wikipedia.search('Bowed Instruments'),
            wikipedia.search('Harp'),
        ])

    def wikipedia_search_other(self):
        return self.random_element([
            wikipedia.search("Musical Instrument"),
            wikipedia.search('Electronic Instruments'),
        ])


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('number_of_ads', nargs='+', type=int)

    def create_ad_title(self, category, db):
        for item in db:
            if item['category'] == category:
                items = item['items']
                outer = random.randint(0, len(items) - 1)
                return items[outer]

    def get_image_url(self, title):
        res = requests.get('https://api.creativecommons.engineering/v1/images?q=test', headers={'Authorization': 'access_token Bearer h2XUajejV5SM6f9rsHXk6QMRMTnxoZ'})
        r = res.json()
        results = r['results']
        index = random.randint(0, len(results))
        target = results[index]
        return target['url']

    def handle(self, *args, **kwargs):
        number_of_ads = kwargs.get('number_of_ads')[0]

        fake = Faker(["en_GB"])
        fake.add_provider(Provider)

        searches_db = [
            {
                'category': 'Pianos/keyboards',
                'items': fake.wikipedia_search_pianos()
            },
            {
                'category': 'Guitar/Bass/Amps', 
                'items': fake.wikipedia_search_guitars()
            },
            {
                'category': 'Drums/Symbals', 
                'items': fake.wikipedia_search_drums()
            },
            {
                'category': 'Woodwind', 
                'items': fake.wikipedia_search_woodwind()
            },
            {
                'category': 'Brass', 
                'items': fake.wikipedia_search_brass()
            },
            {
                'category': 'Studio Equipment', 
                'items': fake.wikipedia_search_studio()
            },
            {
                'category': 'Bowed Instruments', 
                'items': fake.wikipedia_search_bowed()
            },
            {
                'category': 'Other..', 
                'items': fake.wikipedia_search_other()
            },
        ]

        start_date = datetime.date(year=2015, month=1, day=1)
        
        pk = 20
        new_ads = []
        for p in range(number_of_ads):
            category = fake.app_category()
            title = self.create_ad_title(category, searches_db)
            slug = title.replace(" ", "-")
            seller = 11
            price = random.randint(100, 1000000)
            created_on = fake.iso8601()
            sold = bool(random.getrandbits(1))
            location = fake.address()
            image = self.get_image_url(title)
            ad = {
                    "model": "ads.ad",
                    "pk": p+pk,
                    "fields": {
                        "title": f"{title}",
                        "slug": f"{slug.lower()}",
                        "seller": seller,
                        "image": f"{image}",
                        "category": f"{category}",
                        "description": "Great guitar for kids.Nice color.",
                        "created_on": f"{created_on}",
                        "price": price,
                        "location": f"{location}",
                        "city": fake.city(),
                        "sold": sold,
                        "saved": []
                    }
                }
            new_ads.append(ad)

        with open('new_ads.json', 'w') as f:
            json.dump(new_ads, f, indent=6)