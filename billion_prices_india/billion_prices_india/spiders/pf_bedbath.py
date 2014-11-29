from billion_prices_india.spiders.BasePepperFry import BasePepperFry

__author__ = 'sats'


class PepperFry(BasePepperFry):
    """Scrape pet supplies tab from pepper fry"""
    name = "pf_bedbath"
    start_urls = ['http://www.pepperfry.com/bed-bath-%s.html' % s for s in
                  ['bed-sheets', 'combo-offers', 'bed-covers', 'duvet-covers', 'blankets-quilts', 'bedding-diwan-sets',
                   'pillow-covers', 'pillow-inserts', 'mattresses', 'diwan-sets', 'mirrors', 'yoga-mats', 'bath-mats',
                   'bathroom-scales', 'bath-robes-gowns', 'towels', 'bathroom-cabinets', 'bathroom-shelves',
                   'towel-holders', 'toilet-paper-holders', 'bathroom-tumblers', 'clothes-hooks', 'personal-grooming',
                   'soap-dishes',
                   'soap-dispensers', 'cotton-swab-holders', 'bath-sets', 'sanitary-ware-showers',
                   'sanitary-ware-faucets', 'sanitary-ware-stop-cocks-and-angles', 'sanitary-ware-mixers',
                   'sanitary-ware-floor-drains', 'sanitary-ware-cisterns', 'sanitary-ware-pipes-hoses', 'kids']]


