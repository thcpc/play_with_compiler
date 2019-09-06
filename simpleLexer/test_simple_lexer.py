import unittest
from token import *
from state_machine import *
from simple_lexer import *

class TestSimpleLexer(unittest.TestCase):

    def test_parse_intLiteralToken(self):
       lex = SimpleLexer()
       lex.tokenize("1 222 3 1")
       for token in lex.tokens:
           self.assertIn(token.text,["1","222","3","1"])
           if token.text in(["1","222","3","1"]):
                self.assertEqual(token.type,"IntLiteral")
       



if __name__ == '__main__':
    unittest.main()