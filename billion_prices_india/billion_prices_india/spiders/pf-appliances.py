from billion_prices_india.spiders.BasePepperFry import BasePepperFry

__author__ = 'satish'


class PepperFry(BasePepperFry):
    """Scrape pet supplies tab from pepper fry"""
    name = "pf_appliances"
    start_urls = ['http://www.pepperfry.com/appliances-%s.html' % s for s in
                  ['fans-ceiling', 'fans-table', 'wall-mounted', 'table-fans-air-coolers','exhaust-fans','vacuum-cleaners','exhaust-fans','voltage-stabilizers','inverters-ups','electric-irons','heaters','geysers','washing-machines','refrigerators'
                  ,'water-purifiers','juicer-mixer-grinders','gas-stoves','microwave-otg','induction-cooktops','food-processors','roti-makers','toasters-sandwich-makers','hand-blenders','fryers-snack-makers','coffee-makers','electric-kettles'
                  ,'choppers-slicers','steam-electric-cookers','chimney-hoods']]
