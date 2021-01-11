from ..main import Area
import unittest

# Onderdeel 2: Uiteindelijk moet de simulatie om kunnen gaan met gebieden met daarin een gedefinieerde schadeprijs
# per ml. Dat wordt hier getest; er worden een paar scenario's voorgelegd waarin een boel punten samengevoegd worden
# tot een gebied.

class AreaCalcTest(unittest.TestCase):
    """Provides info for points, and expects the damage as an output.
    Functionality: Allow for multiple points to be evaluated for damages
    and added up in order to extract the total in damages. Requires one
    function/constant that dictates the damage and the waterflow at each
    point. Additionally, the definition of space taken by a single point
    may be fine-tuned in an area in order to house more/less points as is
    needed."""

    def Area1(self):
        """Creates an area out of multiple points.
        Function: Baseline area function"""
        # Points do not actually use any space, but are built up out of sections in the space.
        # Suppose we have a fictional space consisting of 40 m^2 that has flooded equally
        # by around 10 ml and the damage consists of 3.5 $/ml of flooding;
        mainarea = Area(40,10,3.5)
        totalcost = mainarea.calc()
        self.assertEqual(totalcost,1400)

    def Area2(self):
        """Creates an area out of multiple points with varying levels of water damage.
        Function: Apply Monte Carlo to increase accuracy of water damages by adding (very
        small) differences in water levels"""
        mainarea = Area(40,range(10,12),4)
        totalcost = mainarea.calc()
        self.assertIn(totalcost,range(1600,1921))
