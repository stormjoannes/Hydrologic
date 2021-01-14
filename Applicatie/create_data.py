import numpy as np
from PIL import Image
import shapefile


def get_data(file):
    # Shapefile reader is used to read .shp files so it can be used
    shpfile = shapefile.Reader(file)
    # get_attributes requires the shp file and the names of the attributes you want
    attributes = get_attributes(['oppervlakt', 'gebruiksdo', 'MAX'], shpfile)
    return attributes


def get_attributes(attributes, file):
    # returns a list of lists.
    all_attr = []
    # get all records. a single record is in this context a building
    file_records = file.records()

    # create a list with the correct attribute(s) for each record (building)
    for x in range(0, len(file_records)):
        attr = []
        rec = file.record(x)
        for attribute in attributes:
            attr.append(rec[attribute])
        # add building attribute(s) to list
        all_attr.append(attr)

    return all_attr


def get_type(subtype):
    # use all types and subtypes the calculator can use
    bebouwing = ['onderwijsfunctie', 'industriefunctie', 'winkelfunctie', 'kantoorfunctie', 'logistiekfunctie',
                 'woonfunctie', 'bijeenkomstfunctie', 'celfunctie', 'sportfunctie', 'overige gebruiksfunctie']
    infrastructure = ['spoor', 'primair', 'secundair', 'tertair', 'overige gebruiksfunctie']
    landbouw = ['gras', 'granen', 'mais', 'aardappelen', 'overige gebruiksfunctie', 'fruitteelt', 'bloembollen', 'hoogstam', 'greenhouse']
    natuur = ['sportparken', 'terreinen', 'begraafplaatsen', 'volkstuinen', 'recreatie', 'groen', 'overige gebruiksfunctie']

    # return type based on subtype
    if subtype in bebouwing:
        type = 'bebouwing'
    elif subtype in infrastructure:
        type = 'infrastructure'
    elif subtype in landbouw:
        type = 'landbouw'
    elif subtype in natuur:
        type = 'natuur'

    return type


class Building:

    def __init__(self, subtype, area, inundepth, scenario, days, month):
        self.subtype = subtype
        self.area = area
        self.inundepth = inundepth
        self.scenario = scenario
        self.days = days
        self.month = month

        self.type = get_type(self.subtype)





# dit is een test path dit wordt later vervangen met het bestand wat van de applicatie komt
data = get_data('../Ondiep/pandPolygon_Area075.shp')
print(data)
test = set()
for x in data:
    test.add(x[1])
print(test)

# # code om tif bestand om te zetten in een numpy array
# img = Image.open('../Ondiep/resultaten/waterOpStraat.tif')
# imnp = np.array(img)
#
#
#
# # fields zijn attributes van het object (het object is in deze context een gebouw dat onderwater kan staan)

#
# # records is een lijst van alle objects (alle gebouwen dus)
# records = shpfile.records()
#
# # met behulp van een for loop kan je bij elk object specifieke data opvragen
# for x in range(0, len(records)):
#     rec = shpfile.record(x)
#     print(rec.MAX)
#
# for x in imnp:
#     print(x)

