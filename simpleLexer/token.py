#coding:utf-8
class Token(object):
    def __init__(self,ch):
        self.text = ch
        self.type = ""
    
    def add_text(self,ch):
        self.text+=ch
        return self

    def clean_text(self):
        self.text = ""
        
    def change_to(self,token_clazz,ch):
        return token_clazz(self.text).add_text(ch)

    def to_s(self):
        return "{0}  {1}".format(self.text,self.type)

class UnkownToken(Token):
    def __init__(self,ch):
        super(UnkownToken,self).__init__(ch)
        self.type = "unkown"

class IdentifierToken(Token):
    # 标识符,关键字
    def __init__(self,ch):
        super(IdentifierToken,self).__init__(ch)
        self.type = "Identifier"

class IntLiteralToken(Token):
    # 整数变量值
    def __init__(self,ch):
        super(IntLiteralToken,self).__init__(ch)
        self.type = "IntLiteral"

class GtToken(Token):
    def __init__(self,ch):
        super(GtToken,self).__init__(ch)
        self.type = "GT"

class LtToken(Token):
    def __init__(self,ch):
        super(LtToken,self).__init__(ch)
        self.type = "LT"

class GEToken(Token):
    def __init__(self,ch):
        super(GEToken,self).__init__(ch)
        self.type = "GT"
