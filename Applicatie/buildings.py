import shapefile


def create_data(file, days, month, scenario, values):
    print(file)
    # Shapefile reader is used to read .shp files so it can be used
    shpfile = shapefile.Reader(file)
    # get_attributes requires the shp file and the names of the attributes you want
    attributes = get_attributes(values, shpfile)
    buildings = create_buildings(attributes, days, month, scenario)

    return buildings


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

    type = ""

    # return type based on subtype
    if subtype in bebouwing:
        type = 'bebouwing'
    elif subtype in infrastructure:
        type = 'infrastructure'
    elif subtype in landbouw:
        type = 'landbouw'
    elif subtype in natuur:
        type = 'natuur'
    else:
        type = 'unknown'

    return type


def create_buildings(data, days, month, scenario):
    buidlings = []
    for x in data:
        """ this line is slightly hardcoded because the attributes (data)
            needs to be set in the correct order in the class.
            if you want to edit the attributes or change the order somewhere this line needs to be updated as well """
        building = Building(data[0], data[1], data[2], scenario, days, month)
        buidlings.append(building)

    return buidlings


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
# data = create_data('../../Ondiep/pandPolygon_Area075.shp', 7, 10, 'hoog', ['gebruiksdo', 'oppervlakt', 'MAX'])
# print(data)
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

