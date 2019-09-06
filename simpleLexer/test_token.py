import unittest
from token import *

class TestToken(unittest.TestCase):

    def test_change_to(self):
        token1 = UnkownToken("i")
        token2 = token1.change_to(IdentifierToken,"n")
        self.assertEquals(token2.type,"Identifier")
        self.assertEquals(token2.text,"in")

if __name__ == '__main__':
    unittest.main()