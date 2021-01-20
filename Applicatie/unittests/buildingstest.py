import unittest
from Applicatie.buildings import Building, change_subtype

"""
    Tests om te kijken of de class Building en de bijbehorende functie goed werken
"""


class BuildingTest(unittest.TestCase):

    def test_changeSubtypeFunctie(self):
        # should remove the word "functie" from any string and return the new string in uppercases
        x = 'woonfunctie'
        y = 'functiewoon'

        self.assertEquals(change_subtype(x), 'WOON')
        self.assertEquals(change_subtype(y), 'WOON')

    def test_changeSubtypeGebruiks(self):
        # should remove the word "gebruiks" from any string and return the new string in uppercases
        x = 'overige gebruiks'

        self.assertEquals(change_subtype(x), 'OVERIGE')

    def test_changeSubtypeList(self):
        # should split a string that exists of several subtypes into a list
        x = 'woonfunctie, bijeenkomstfunctie'

        self.assertEquals(change_subtype(x), ['WOON', 'BIJEENKOMST'])

    def test_class(self):
        # tests if the class attributes are made in the right order
        x = Building('woonfunctie', 50, 0.02, 'HIGH', 502, 504)

        self.assertEquals(x.subtype, 'WOON')
        self.assertEquals(x.area, 50)
        self.assertEquals(x.inundepth, 0.02)


if __name__ == '__main__':
    unittest.main()