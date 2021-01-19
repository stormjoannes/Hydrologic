import shapefile
from create_directory import create_directory


def create_data(files, scenario, values):
    # create_directory(files)
    # Shapefile reader is used to read .shp files so it can be used
    shpfile = shapefile.Reader(files)
    # get_attributes requires the shp file and the names of the attributes you want
    attributes = get_attributes(values, shpfile)
    buildings = create_buildings(attributes, scenario)

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


def change_subtype(subtype):
    # As far as we know all subtypes end with "functie" so we simple remove this so that it is compatible with the calculator
    if "functie" in subtype:
        new_sub = subtype.replace('functie', '')
        return new_sub.upper()


def create_buildings(data, scenario):
    buidlings = []
    for x in data:
        """ this line is slightly hardcoded because the attributes (data)
            needs to be set in the correct order in the class.
            if you want to edit the attributes or change the order somewhere this line needs to be updated as well """
        building = Building(x[0], x[1], x[2], scenario)
        buidlings.append(building)

        print("subtype", building.subtype)
        print("opp", building.area)
        print("inundepth", building.inundepth)

    return buidlings


class Building:

    def __init__(self, subtype, area, inundepth, scenario):
        self.subtype = change_subtype(subtype)
        self.area = area
        self.inundepth = inundepth
        self.scenario = scenario


# # dit is een test path dit wordt later vervangen met het bestand wat van de applicatie komt
data = create_data('../../Ondiep/pandPolygon_Area075.shp', 'hoog', ['gebruiksdo', 'oppervlakt', 'MAX'])
print(data)
# # code om tif bestand om te zetten in een numpy array
# img = Image.open('../Ondiep/resultaten/waterOpStraat.tif')
# imnp = np.array(img)
#
#
#
# fields zijn attributes van het object (het object is in deze context een gebouw dat onderwater kan staan)


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

