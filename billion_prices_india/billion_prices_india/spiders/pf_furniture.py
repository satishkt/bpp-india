from billion_prices_india.spiders.BasePepperFry import BasePepperFry

__author__ = 'satish'


class PepperFry(BasePepperFry):
    """Scrape pet supplies tab from pepper fry"""
    name = "pf_furniture"
    start_urls = ['http://www.pepperfry.com/furniture-%s.html' % s for s in
                  ['sofas-one-seater-sofas', 'sofas-two-seater-sofas', 'sofas-sofas-couches-three-seater',
                   'sofas-sofa-sets', 'sofas-recliners', 'sofa-cum-beds', 'sofa-sectionals', 'futons', 'poufee-stools'
                                                                                                       'bar-cabinets',
                   'bar-chairs-stools', 'bar-trolleys', 'wine-racks', 'arm-chairs', 'sofas-bean-bags',
                   'ergonomic-chairs', 'executive-chairs', 'folding-chairs', 'metal-chairs', 'reception-area-chairs',
                   'rocking-chairs', 'settees-benches', 'stools-colonial', 'stools-contemporary',
                   'stools-industrial-modern',
                   'stools-rustic', 'stools-indian-ethnic', 'beds-king-sized-beds', 'beds-queen-sized-beds',
                   'beds-poster', 'beds-single',
                   'bed-side-tables-contemporary', 'bed-side-tables-modern', 'bed-side-tables-colonial',
                   'bed-side-tables-eclectic', 'bed-side-tables-indian-ethnic', 'bunk-beds-metal', 'bunk-beds-wooden',
                   'bed-room-sets', 'dressing-tables-contemporary',
                   'dressing-tables-colonial', 'dressing-tables-eclectic', 'coffee-tables-contemporary',
                   'coffee-tables-modern', 'coffee-tables-colonial', 'coffee-tables-eclectic',
                   'coffee-tables-indian-ethnic', 'large-size-coffee-tables-contemporary',
                   'large-size-coffee-tables-colonial', 'large-size-coffee-tables-modern',
                   'large-size-coffee-tables-indian-ethnic',
                   'furniture-coffee-table-sets', 'end-tables-contemporary', 'end-tables-modern', 'end-tables-colonial',
                   'end-tables-indian-ethnic', 'end-tables-eclectic', 'console-tables-contemporary',
                   'console-tables-colonial', 'console-tables-eclectic',
                   'sets-of-tables-contemporary', 'sets-of-tables-colonial', 'sets-of-tables-indian-ethnic',
                   'sets-of-tables-eclectic', 'study-laptop-tables-contemporary', 'study-laptop-tables-modern',
                   'study-laptop-tables-colonial', 'study-laptop-tables-indian-ethnic',
                   'study-laptop-tables-study-units', 'study-laptop-tables-wall-mounted-tables',
                   'dining-tables-contemporary', 'dining-tables-colonial', 'dining-tables-eclectic',
                   'dining-chairs-contemporary', 'dining-chairs-modern', 'dining-chairs-colonial',
                   'dining-sets-two-seater', 'dining-sets-four-seater', 'dining-sets-six-seater',
                   'dining-sets-eight-seater', 'entertainment-units-contemporary', 'entertainment-units-modern',
                   'entertainment-units-indian-ethnic', 'entertainment-units-eclectic', 'wardrobes-contemporary',
                   'wardrobes-modern', 'wardrobes-colonial',
                   'cabinets-and-sideboards-colonial', 'cabinets-and-sideboards-contemporary',
                   'cabinets-and-sideboards-indian-ethnic', 'cabinets-and-sideboards-modern',
                   'shoe-racks-engineered-wood', 'shoe-racks-solid-wood', 'shoe-racks-metal', 'hutch-cabinets',
                   'chest-of-drawers-contemporary', 'chest-of-drawers-colonial', 'chest-of-drawers-eclectic',
                   'chest-of-drawers-modern', 'bookcases', 'book-shelves-contemporary', 'book-shelves-colonial',
                   'book-shelves-contemporary', 'book-shelves-eclectic', 'book-shelves-modern',
                   'file-cabinets', 'magazine-racks', 'trunks-boxes', 'children-beds', 'children-cradles',
                   'children-chairs', 'children-storage',
                   'children-chair-table-sets', 'children-tables', 'kids-furniture-writing-study-tables',
                   'kids-furniture-seating', 'moulded-furniture-cabinets', 'moulded-furniture-organisers',
                   'moulded-furniture-stacking-chairs',
                   'moulded-furniture-tables', 'garden-outdoor-furniture']]