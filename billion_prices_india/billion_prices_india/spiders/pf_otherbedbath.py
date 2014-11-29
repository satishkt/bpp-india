from billion_prices_india.spiders.BasePepperFry import BasePepperFry

__author__ = 'satish'


class PepperFry(BasePepperFry):
    """Scrape pet supplies tab from pepper fry"""
    name = "pf_otherbedbath"
    start_urls = ['http://www.pepperfry.com/furnishings-curtains-shower-curtains.html',
                  'http://www.pepperfry.com/furnishings-wall-lights-bathroom-lights.html',
                  'http://www.pepperfry.com/appliances-geysers.html']
