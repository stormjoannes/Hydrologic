from ..main import Point
import unittest

# Onderdeel 1: De simulatie kan op een punt in een gebied de schade uitrekenen.
# De bedoeling is dat dit uiteindelijk op deze manier uitgebreid kan worden voor een geheel gebied.

class PointCalcTest(unittest.TestCase):
    """Provides info for points, and expects the damage as an output."""

    def SinglePoint1(self):
        """Calculates the damage for a single point, using a constant value."""
        point = Point(0.53,20)  # $/ml and ml's.
        self.assertEqual(point.getCost(), 10.60)

    def SinglePoint2(self):
        """Calculates the damage for a single point, using a simple exponential formula function"""
        def expcost(x):
            """Takes the amount of ml in damages and outputs the cost"""
            return x**2 + 3

        point = Point(expcost,10)
        self.assertEqual(point.getCost(), 103)