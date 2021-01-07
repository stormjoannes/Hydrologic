import unittest

# Onderdeel 1: De simulatie kan op een punt in een gebied de schade uitrekenen.
# De bedoeling is dat dit uiteindelijk op deze manier uitgebreid kan worden voor een geheel gebied.

class PointCalcTest(unittest.TestCase):
    """Provides info for points, and expects the damage as an output."""

    def SinglePoint1(self):
        """Calculates the damage for a single point."""
        dmgperml = 3.49
