from billion_prices_india.spiders.BasePepperFry import BasePepperFry

__author__ = 'satish'


class PepperFry(BasePepperFry):
    """Scrape pet supplies tab from pepper fry"""
    name = "pf_test"
    start_urls = ['http://www.pepperfry.com/bed-bath-%s.html' % s for s in
                  ['bed-sheets', 'combo-offers', 'bed-covers', 'duvet-covers', 'blankets-quilts', 'bedding-diwan-sets']]