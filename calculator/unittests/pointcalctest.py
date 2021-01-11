from ..main import Point
import unittest

# Onderdeel 1: De simulatie kan op een punt in een gebied de schade uitrekenen.
# De bedoeling is dat dit uiteindelijk op deze manier uitgebreid kan worden voor een geheel gebied.

class PointCalcTest(unittest.TestCase):
    """Provides info for points, and expects the damage as an output.
    Functionality: Calculate damages on each point in a given property.
    Points are defines as a 1 by 1 meter space in the property, although
    this can be finetuned."""

    def test_costconstant(self):
        """Calculates the damage for a single point, using a constant value.
        Functionality: Base damage calculation."""
        point = Point(0.53,20)  # $/ml and ml's.
        self.assertEqual(10.6, point.getCost())

    def test_costformula(self):
        """Calculates the damage for a single point, using a simple exponential formula function.
        Functionality: Damage calculation through supplied function."""
        def expcost(x):
            """Takes the amount of ml in damages and outputs the cost"""
            return x**2 + 3

        point = Point(expcost,10)
        self.assertEqual(103, point.getCost())

