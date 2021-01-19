import unittest
from ..buildings import Building, change_subtype

"""
    Tests om te kijken of de class Building en de bijbehorende functie goed werken
"""


class buildingtests(unittest.TestCase):

    def changeSubtypeTest(self):
        # should remove the word "functie" from any string and return the new string in uppercases
        x = 'woonfunctie'
        y = 'functiewoon'

        self.assertEquals(change_subtype(x), 'WOON')
        self.assertEquals(change_subtype(y), 'WOON')


    def classTest(self):
        # tests if the class attributes are made in the right order
        x = Building('woonfunctie', 50, 0.02, 'hoog', 7, 20)

        self.assertEquals(x.subtype, 'woonfunctie')
        self.assertEquals(x.area, 50)
        self.assertEquals(x.inundepth, 0.02)
