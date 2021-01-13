# Doel: Waterschade uitrekenen a.d.h.v. meegegeven informatie;
# Parameters: Waterstand, omgevingsgrootte, prijs/m^2

def getnearestpoint(arrx, arry, point):
    """Gets the nearest point."""
    if point in arrx:
        return arry[arrx.index(point)]
    else:
        for x in arrx:
            if x > point:
                x1y1 = (arrx[arrx.index(x)-1],arry[arrx.index(x)-1])
                x2y2 = (arrx[arrx.index(x)],arry[arrx.index(x)])
                return getvalue_euclidean(x1y1[0],x1y1[1],x2y2[0],x2y2[1],point)


def getvalue_euclidean(x1,y1,x2,y2,requestedx):
    """Gets the y value of a given x, by applying the Euclidean Distance algorithm."""
    # Step 1: Get coefficient.
    coeff = ((y2-y1)/(x2-x1))
    # Step 2: Get y value. Start from x1y1.
    diffx = requestedx - x1
    return (coeff*diffx) + y1


def inundationdepthreductionfactor(type: str, depth: float):
    """Returns the reduction factor for inundationdepth based on type and subtype."""
    type = type.upper()

    x = [-0.01, 0.01, 0.05, 0.15, 0.3]
    if type == "URBAN":
        y = [0, 0.1, 0.5, 1.0, 1.0]
    elif type == "INFRASTRUCTURE":
        y = [0,0,1,1,1]
    elif type == "AGRICULTURE":
        y = [0,1,1,1,1]
    return getnearestpoint(x,y,depth)


def durationreductionfactor(type: str,subtype: str,days: float):
    """Returns the reduction factor for duration based on type and subtype."""
    type = type.upper()
    subtype = subtype.upper()

    x = [0, 0.5, 1, 3, 20]
    if type == "URBAN":
        y = [1, 1, 1, 1, 1]
    elif type == "INFRASTRUCTURE":
        if subtype == "TERTIAR":
            y = [0.5, 1, 1, 1, 1]
        else:
            y = [0, 0.4, 0.8, 1, 1]
    elif type == "AGRICULTURE":
        if subtype in ["GRAS", "GRANEN"]:
            y = [0, 0, 0.2, 0.4, 1]
        else:
            y = [0, 0, 0.2, 1, 1]
    return getnearestpoint(x,y,days)


def seasonreductionfactor(type: str,subtype: str,month: int):
    """Returns the reduction factor for duration based on type and subtype."""
    type = type.upper()
    subtype = subtype.upper()

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    if type in ["URBAN", "INFRASTRUCTURE"]:
        y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    elif type == "AGRICULTURE":
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
    return getnearestpoint(x,y,month)


class Calc():
    """Calculates something"""
    def __init__(self, type, subtype, usage, scenario, inundepth, days, month):
        """Initialises the calc."""
        # Save attributes
        self.type = type
        self.subtype = subtype
        self.usage = usage
        self.scenario = scenario
        self.inundepth = inundepth
        self.days = days
        self.month = month

        self.inunfactor = inundationdepthreductionfactor(self.type,self.subtype,self.inundepth)

        self.durfactor = durationreductionfactor(self.type, self.subtype, self.days)

        self.seasonfactor = seasonreductionfactor(self.type, self.subtype, self.month)

# from decimal import Decimal
#
# class Point():
#     """Defines a single point (as 1 m^2)"""
#     def __init__(self, dpml, ml):
#         self.cpml = dpml
#         self.vol = ml
#
#     def getCost(self):
#         if isinstance(self.cpml, int) or isinstance(self.cpml, float):  # If the cost parameter is a constant
#             return float(Decimal(str(self.cpml)) * Decimal(str(self.vol)))  # Deze hele workaround om een float inaccuracy op te lossen
#         elif callable(self.cpml):  # If the cost parameter is a function
#             return self.cpml(self.vol)
#         else:
#             raise Exception("Invalid parameters given")
#
# class Area():
#     """Defines an collection of points"""
#     def __init__(self, pointcount,):
