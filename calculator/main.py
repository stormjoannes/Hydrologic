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

def inundationdepthreductionfactor(type: str,subtype: str,depth: float):
    """Returns the reduction factor for inundationdepth based on type and subtype."""
    type = type.upper()
    subtype = subtype.upper()

    if type == "URBAN":
        x = [-0.01, 0.01, 0.05, 0.15, 0.3]
        y = [0, 0.1, 0.5, 1.0, 1.0]
    elif type == "INFRASTRUCTURE":
        x = [-0.01,0.01,0.05,0.15,0.3]
        y = [0,0,1,1,1]
    elif type == "AGRICULTURE":
        x = [-0.01,0.01,0.05,0.15,0.3]
        y = [0,1,1,1,1]

    return getnearestpoint(x,y,depth)

def durationreductionfactor(type: str,subtype: str,days: int):
    """Returns the reduction factor for duration based on type and subtype."""
    if type == "URBAN":
        x = [1,20]
        y = [1,1]
    elif type == "INFRASTRUCTURE":
        raise NotImplementedError
    elif type == "AGRICULTURE":
        raise NotImplementedError

    return getnearestpoint(x,y,days)


def seasonreductionfactor(type: str,subtype: str,month: int):
    """Returns the reduction factor for duration based on type and subtype."""
    if type == "URBAN":
        x = [1,12]
        y = [1,1]
    elif type == "INFRASTRUCTURE":
        x = [1,12]
        y = [1,1]
    elif type == "AGRICULTURE":
        raise NotImplementedError

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