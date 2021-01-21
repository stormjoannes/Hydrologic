import shapefile
import os
from calculator.main import Calc
import pandas as pd


def create_data(nbh, scenario, values):
    # get the pandPolygon for the correct neighbourhood
    # next to nbh enter the path where you keep all neighbourhoods
    path = get_neighbourhood_path(nbh, r'C:\Users\brand\hbo\jaar_2\BS\hydro\Buurten')
    # use it in the shapefile reader
    shpfile = shapefile.Reader(path)
    # get_attributes requires the shp file and the names of the attributes you want
    attributes = get_attributes(values, shpfile)
    # return a list with all buidlings
    buildings = create_buildings(attributes, scenario)

    return buildings


def get_neighbourhood_path(nbh, path):
    neighbourhoods = os.listdir(path)
    for neighbourhood in neighbourhoods:
        if neighbourhood == nbh:
            nbh_path = os.path.join(path, nbh, 'pandPolygon_Area075.shp')
            return nbh_path


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
    # turn string to lowercase
    subtype = subtype.lower()
    # remove spaces in string
    subtype = subtype.replace(' ', '')
    # some subtype values contain more than 1 subtype. We turn these strings into lists
    if ',' in subtype:
        subtype_list = subtype.split(',')
        # As far as we know all subtypes end with "functie" or "gebruiks" so we simple remove this so that it is compatible with the calculator
        for x in range(0, len(subtype_list)):
            if "functie" in subtype_list[x]:
                subtype_list[x] = subtype_list[x].replace('functie', '')
            if "gebruiks" in subtype_list[x]:
                subtype_list[x] = subtype_list[x].replace('gebruiks', '')

        return [x.upper() for x in subtype_list]

    else:
        # As far as we know all subtypes end with "functie" or "gebruiks" so we simple remove this so that it is compatible with the calculator
        if "functie" in subtype:
            subtype = subtype.replace('functie', '')
        if "gebruiks" in subtype:
            subtype = subtype.replace('gebruiks', '')
        return subtype.upper()


def is_none(building):
    # check if subtype and area are not 0
    if building[0] == "":
        return True
    elif building[1] == 0.0:
        return True
    else:
        return False


def create_buildings(data, scenario):
    # create a dataframe for the frontend
    buildings = {'subtype': [], 'oppervlakte (in m²)': [], 'inundatiediepte': [], 'scenario': [], "waterschade (totaal in euro's)": [], 'lat': [], 'lng': []}
    for x in data:
        # check if x is none
        if not is_none(x):
            """ this line is slightly hardcoded because the attributes (data)
                needs to be set in the correct order in the class.
                if you want to edit the attributes or change the order somewhere this line needs to be updated as well 
                for now it needs the subtype(0), area(1), inundepth(2), scenario, lng(4), lat(3)"""
            building = Building(x[0], x[1], x[2], scenario, x[4], x[3])
            # add all class variables to the dataframe
            buildings['subtype'].append(building.subtype)
            buildings['oppervlakte (in m²)'].append(building.area)
            buildings['inundatiediepte'].append(building.inundepth)
            buildings['scenario'].append(building.scenario)
            buildings['lat'].append(building.lat)
            buildings['lng'].append(building.lng)
            buildings["waterschade (totaal in euro's)"].append(round(building.waterschatting, 2))

    return pd.DataFrame(data=buildings)


class Building:

    def __init__(self, subtype, area, inundepth, scenario, lat, lng):
        self.subtype = change_subtype(subtype)
        self.area = area
        self.inundepth = inundepth
        self.scenario = scenario
        self.lat = float(lat - 0.0009846483658)
        self.lng = float(lng - 0.0003943217995)

        calculator = Calc(self.area, 'BEBOUWING',  self.subtype, self.scenario, self.inundepth)
        self.waterschatting = calculator.calc()

    def __str__(self):
        return " Subtype:" + str(self.subtype) + \
               "\n Area:" + str(self.area) + \
               "\n Inundepth:" + str(self.inundepth) + \
               "\n Scenario:" + str(self.scenario) + \
               "\n Latitude:" + str(self.lat) + \
               "\n Longitude:" + str(self.lng)


data = create_data('Ondiep', 'HIGH', ['gebruiksdo', 'oppervlakt', 'MAX', 'LAT', 'LNG'])
print(data.index)
