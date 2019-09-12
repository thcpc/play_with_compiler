import unittest
from token import *
from state_machine import *
from simple_lexer import *

class TestSimpleLexer(unittest.TestCase):

    def test_parse_intLiteralToken(self):
       lex = SimpleLexer()
       test_data = "1 222 3 1"
       lex.tokenize(test_data)
       
       for token in lex.tokens:
          
           self.assertIn(token.text,test_data.split(" "))
           if token.text in(test_data.split(" ")):
                self.assertEqual(token.type,"IntLiteral")
    
    def test_parse_IdentifierToken(self):
        lex = SimpleLexer()
        test_data = "k aaaaa bbb c3 d11"
        lex.tokenize(test_data)
        # print(map(lambda x: x.text ,lex.tokens))
        for token in lex.tokens:
            
            self.assertIn(token.text,test_data.split(" "))
            if token.text in(test_data.split(" ")):
                self.assertEqual(token.type,"Identifier")
    
    def test_parse_mix_int_in_token(self):
        lex = SimpleLexer()
        test_data = "11 aaaaa bbb 333 d11"
        lex.tokenize(test_data)
        for token in lex.tokens:
            self.assertIn(token.text,["11","aaaaa","bbb","333","dd","d11"])
            if token.text in(["11","333"]):
                self.assertEqual(token.type,"IntLiteral")
            else:
                self.assertEqual(token.type,"Identifier")
            
                
       



if __name__ == '__main__':
    unittest.main()