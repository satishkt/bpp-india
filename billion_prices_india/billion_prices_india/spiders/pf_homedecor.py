from billion_prices_india.spiders.BasePepperFry import BasePepperFry

__author__ = 'satish'


class PepperFry(BasePepperFry):
    """Scrape pet supplies tab from pepper fry"""
    name = "pf_homedecor"
    start_urls = ['http://www.pepperfry.com/home-decor-%s.html' % s for s in
                  ['wall-shelves', 'corner-shelves', 'cd-racks',
                   'jharokhas', 'screens-dividers', 'candles-diyas-stands',
                   'clocks', 'desk-shelf-clocks', 'curios-showpieces', 'curios-figurines',
                   'curios-trinket-jewellery-boxes', 'curios-key-holders', 'ash-trays',
                   'hookahs-accessories', 'spiritual-decor-temples', 'spiritual-decor-puja-supplies',
                   'spiritual-decor-incense-sticks', 'spiritual-decor-incense-sticks',
                   'spiritual-idols-figurines', 'spiritual-decor-bells-chimes', 'spiritual-decor-feng-shui',
                   'spiritual-decor-vastu-yantras', 'spiritual-gold-coins', 'spiritual-silver-coins', 'celebrations',
                   'photo-frames', 'wall-stickers-decals'
                      , 'wall-art', 'posters', 'nautical-decor', 'children-decor-clocks', 'kids-decor-kids-cushions',
                   'kids-teen-decor-stickers', 'kids-teen-decor-photo-frames', 'children-decor-posters']]
