from billion_prices_india.spiders.BasePepperFry import BasePepperFry

__author__ = 'satish'


class PepperFry(BasePepperFry):
    """Scrape pet supplies tab from pepper fry"""
    name = "pf_furnishings"
    start_urls = ['http://www.pepperfry.com/furnishings-%s.html' % s for s in
                  ['curtains-door-curtains', 'curtains-window-curtains', 'curtains-shower-curtains',
                   'curtains-curtain-rods', 'blinds-shades', 'area-rugs',
                   'carpets', 'dhurries-runners', 'wall-papers', 'wall-lights-wall-mounted',
                   'wall-lights-wall-spot-lights', 'wall-lights-bathroom-lights', 'ceiling-lights-chandeliers',
                   'ceiling-lights-hanging-lights', 'ceiling-lights-recessed-lights', 'ceiling-lights-flush-mounted',
                   'tube-lights', 'table-lamps',
                   'study-lamps', 'floor-lamps', 'outdoor-lighting', 'light-bulbs', 'cfls',
                   'led-rechargeable-lights']]
