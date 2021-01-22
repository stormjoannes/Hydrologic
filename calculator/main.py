def getnearestpoint(arrx, arry, point):
    """Gets the nearest point."""
    if point in arrx:
        return arry[arrx.index(point)]
    else:
        for x in arrx:
            if x > point:
                x1y1 = (arrx[arrx.index(x) - 1], arry[arrx.index(x) - 1])
                x2y2 = (arrx[arrx.index(x)], arry[arrx.index(x)])
                return getvalue_euclidean(x1y1[0], x1y1[1], x2y2[0], x2y2[1], point)
        return arry[-1]


def getvalue_euclidean(x1, y1, x2, y2, requestedx):
    """Gets the y value of a given x, by applying the Euclidean Distance algorithm."""
    # Step 1: Get coefficient.
    coeff = ((y2 - y1) / (x2 - x1))
    # Step 2: Get y value. Start from x1y1.
    diffx = requestedx - x1
    return (coeff * diffx) + y1


def inundationdepthreductionfactor(type: str, subtype: str, depth: float):
    """Returns the reduction factor for inundationdepth based on type and subtype."""
    type, subtype = type.upper(), subtype.upper()

    x = [-0.01, 0.01, 0.05, 0.15, 0.3]
    if type == "BEBOUWING":
        y = [0, 0.1, 0.5, 1.0, 1.0]
    elif type == "INFRASTRUCTURE":
        y = [0, 0, 1, 1, 1]
    elif type == "LANDBOUW":
        y = [0, 1, 1, 1, 1]

    return getnearestpoint(x, y, depth)


def durationreductionfactor(type: str, subtype: str, days: float):
    """Returns the reduction factor for duration based on type and subtype."""
    type = type.upper()
    subtype = subtype.upper()

    x = [0, 0.5, 1, 3, 20]
    if type == "BEBOUWING":
        y = [1, 1, 1, 1, 1]
    elif type == "INFRASTRUCTURE":
        if subtype == "TERTIAR":
            y = [0.5, 1, 1, 1, 1]
        else:
            y = [0, 0.4, 0.8, 1, 1]
    elif type == "LANDBOUW":
        if subtype in ["GRAS", "GRANEN"]:
            y = [0, 0, 0.2, 0.4, 1]
        else:
            y = [0, 0, 0.2, 1, 1]

    return getnearestpoint(x, y, days)


def seasonreductionfactor(type: str, subtype: str, month: int):
    """Returns the reduction factor for duration based on type and subtype."""
    type = type.upper()
    subtype = subtype.upper()

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    if type in ["BEBOUWING", "INFRASTRUCTURE"]:
        y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    elif type == "LANDBOUW":
        if subtype == "GRAS":
            y = [0.3, 0.3, 0.5, 1, 1, 1, 1, 1, 1, 1, 0.5, 0.3, 0.3]
        elif subtype == "MAIS":
            y = [0.1, 0.1, 0.1, 0.4, 0.8, 1, 1, 1, 1, 1, 0.5, 0.1, 0.1]
        elif subtype == "AARDAPPELEN":
            y = [0.1, 0.1, 0.1, 0.5, 0.7, 0.9, 1, 1, 1, 1, 0.8, 0.1, 0.1]
        elif subtype in ["BIETEN", "OVERIG"]:
            y = [0.1, 0.1, 0.1, 0.5, 1, 1, 1, 1, 1, 1, 0.5, 0.1, 0.1]
        elif subtype == "GRANEN":
            y = [0.7, 0.7, 0.7, 0.7, 0.9, 1, 1, 1, 1, 1, 1, 0.7, 0.7]

    return getnearestpoint(x, y, month)


class Calc():
    """Calculates water damage based on a couple of parameters;
    - area (in m^2)
    - type (urban, infrastructure, agriculture, nature)
    - subtype (subtypes of the given type, string (single) or list (multiple)
    - scenario (LOW, MEDIUM, HIGH; str, dictates which price should be chosen)
    - inundepth (height which the water reaches in a building)"""

    def __init__(self, area: float, type: str, subtype: str or list, scenario: str, inundepth: float):
        """Initialises the calc."""
        # Save attributes
        self.area = area  # Area in m^2
        self.type = type.upper()  # Category, can be BEBOUWING, INFRASTRUCTUUR, etc.
        if isinstance(subtype,str):  # ONDERWIJS, INDUSTRIE for type BEBOUWING, etc, supports a list with multiple subtypes.
            self.subtype = subtype.upper()
        elif isinstance(subtype,list):
            for indx in range(len(subtype)):
                subtype[indx] = subtype[indx].upper()
            self.subtype = subtype
        self.scenario = scenario.upper()  # Scenario dictates the chosen price, as shown below.
        self.inundepth = inundepth  # Height which the water reaches in a given building.

        # Schade data opgehaald van https://www.waterschadeschatter.nl/static_media/lizard_damage/help/gebruikers%20handleiding.pdf
        self.damagedata = \
            {"BEBOUWING":
                {
                    "ONDERWIJS":         (163, 380, 271),
                    "INDUSTRIE":         (163, 380, 271),
                    "WINKEL":            (163, 380, 271),
                    "KANTOOR":           (163, 380, 271),
                    "LOGIES":        (163, 380, 271),
                    "WOON":              (163, 380, 271),
                    "BIJEENKOMST":       (163, 380, 271),
                    "CEL":               (27, 81, 54),
                    "SPORT":             (27, 81, 54),
                    "OVERIGE":           (27, 81, 54),
                },
            "INFRASTRUCTURE":
                {
                    "SPOOR":             (760, 760, 760),
                    "PRIMAIR":           (760, 760, 760),
                    "SECUNDAIR":         (760, 760, 760),
                    "TERITAIR":          (760, 760, 760),
                    "OVERIG":            (760, 760, 760)
                },
            "LANDBOUW":
                {
                    "GRAS":              (1033,1203,1094),
                    "GRANEN":            (1011,2617,1691),
                    "MAIS":              (1710,3334,2088),
                    "AARDAPPELEN":       (2432,2622,2552),
                    "OVERIG":            (3474,3909,3660),
                    "FRUITTEELT":        (18298,25434,22489),
                    "BLOEMBOLLEN":       (24692,32655,28441),
                    "HOOGSTAM":          (63175,114502,76165),
                    "GREENHOUSE":        (459743,492590,473839)
                },
            "NATUUR":
                {
                    "SPORTPARKEN":       (760,760,760),
                    "TERREINEN":         (760,760,760),
                    "BEGRAAFPLAATSEN":   (869,1303,1086),
                    "VOLKSTUINEN":       (869,1303,1086),
                    "RECREATIE":         (869,1303,1086),
                    "GROEN":             (869,1303,1086),
                    "OVERIG":            (869,1303,1086),
                }}

        if isinstance(self.subtype,list):  # If theres multiple subtypes, get the subtype with the highest average damage/m^2
            self.subtype = sorted(self.subtype,key=lambda x: self.damagedata[self.type][x][2])[-1]
        data = self.damagedata[self.type][self.subtype]

        self.minimum = data[0]  # Get the min, average, max for the given subtype.
        self.maximum = data[1]
        self.average = data[2]

        self.inunfactor = inundationdepthreductionfactor(self.type, self.subtype, self.inundepth)

    def calc(self):
        """Calculates water damage and returns it."""
        # Formula adapted from following source (direct damage only);
        # https://www.waterschadeschatter.nl/static_media/lizard_damage/help/schadeberekening.pdf
        # In the formula, a 'scenario' damage amount is specified, but not further defined,
        # here we choose to allow the user to define the scenario to define the price that is
        # used in the calculator. TODO: Further research should focus on the significance of these 'scenarios' in the formula.
        # Additionally, due to refactors, the model has been simplified significantly.

        if self.scenario == "LOW":
            return self.area * (self.minimum * self.inunfactor)
        elif self.scenario == "MEDIUM":
            return self.area * (self.average * self.inunfactor)
        elif self.scenario == "HIGH":
            return self.area * (self.maximum * self.inunfactor)

