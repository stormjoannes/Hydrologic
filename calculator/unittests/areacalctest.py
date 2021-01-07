import unittest

# Onderdeel 2: Uiteindelijk moet de simulatie om kunnen gaan met gebieden met daarin een gedefinieerde schadeprijs
# per ml. Dat wordt hier getest; er worden een paar scenario's voorgelegd waarin een boel punten samengevoegd worden
# tot een gebied.

class AreaCalcTest(unittest.TestCase):
    """Provides info for points, and expects the damage as an output."""