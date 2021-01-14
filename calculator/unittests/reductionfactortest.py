# Doel: Opstellen van reductiefactor-formules voor gebruik in de calculator
# Er zijn 3 soorten reductiefactoren voor directe schade;
# - Reductiefactor inundatiediepte
# - Reductiefactor duur overlast
# - Reductiefactor seizoen
# De reductiefactoren kennen een unieke grafiek/formule voor elk classificatie.
# De volgende classificaties zijn present:
# - Bebouwing (urban)
# - Wegen (infrastructuur)
# - Gewassen (landbouw)

from ..main import Calc
import unittest

class reductionfactortest(unittest.TestCase):
    """Tests the reductionfactors for urban damages.
    Here, the reductionfactors for duration and season are always 1,
    and should be tested to ensure this is the case. The only varying
    reductionfactor is the inundationdepth"""

    def test_inundationfactorzero(self):
        """Tests a case in which the inundation reduction factor should be 0."""
        calc = Calc(area=100, type="BEBOUWING",subtype="ONDERWIJS",usage="HIGH",scenario="HIGH",inundepth=-0.01, days=5, month=3)  # Inundationdepth(-0.01) == Factor(0)
        factor = calc.inunfactor
        self.assertEqual(factor, 0)

    def test_inundationfactorhalf(self):
        """Tests a case in which the inundation reduction factor should be 0.5"""
        calc = Calc(area=100, type="BEBOUWING",subtype="ONDERWIJS",usage="HIGH",scenario="HIGH",inundepth=0.05, days=5, month=3)  # Inundationdepth(0.05) == Factor(0.5)
        factor = calc.inunfactor
        self.assertEqual(factor, 0.5)

    def test_inundationfactorfull(self):
        """Tests a case in which the inundation reduction factor should be 1"""
        calc = Calc(area=100, type="BEBOUWING",subtype="ONDERWIJS",usage="HIGH",scenario="HIGH",inundepth=0.15, days=5, month=3)  # Inundationdepth(0.15) == Factor(1)
        factor = calc.inunfactor
        self.assertEqual(factor, 1)

    def test_durationfactorconsistency(self):
        """Tests whether the duration reduction factor is always consistent (is 1 in different cases)"""
        for i in range(0, 21):
            calc = Calc(area=100, type="BEBOUWING",subtype="ONDERWIJS",usage="HIGH",scenario="HIGH",inundepth=0.3, days=i, month=3)
            factor = calc.durfactor
            self.assertEqual(factor, 1)

    def test_seasonfactorconsistency(self):
        """Tests whether the duration reduction factor is always consistent (is 1 in different cases)"""
        for j in range(0,13):
            calc = Calc(area=100, type="BEBOUWING",subtype="ONDERWIJS",usage="HIGH",scenario="HIGH",inundepth=0.3, days=5, month=j)
            factor = calc.seasonfactor
            self.assertEqual(factor, 1)
