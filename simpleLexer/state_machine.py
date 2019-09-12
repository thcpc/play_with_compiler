#coding:utf-8
from token import *

class StateMachine():
    def __init__(self,script=""):
        self.script = script
        self.pos = 0
        self.state = InitTokenState(UnkownToken(""));

    def get_script(self):
        return self.script
    
    def char(self,pos):
        return self.script[pos]
    
    def get_pos(self):
        return self.pos
    
    def forward(self):
        self.pos += 1

    def prev(self):
        self.pos -= 1
    
    def peek(self):
        self.pos + 1

    def next(self):
        self.state = self.state.accept(self)
        
        if not self.has_next():
            return FinishTokenState(self.state.token)
        return self.state

    def has_next(self):
        return self.get_pos() < len(self.get_script())


class InitTokenState():

    def __init__(self,token):
        self.token = token
    def accept(self,machine):
        ch = machine.char(machine.get_pos())
        if ch.isdigit():
            machine.forward()
            return IntLiteralState(self.token.change_to(IntLiteralToken,ch))
        if ch.isalpha():
            machine.forward()
            return IdentifierState(self.token.change_to(IdentifierToken,ch))
        machine.forward()
        self.token.clean_text()
        return self
    
    def name(self):
        return "InitTokenState"

class State(object):
    def __init__(self,token):
        self.token = token

    def finish_state(self):
        return FinishTokenState(self.token)

class FinishTokenState(State):
    def __init__(self,token):
        super(FinishTokenState,self).__init__(token)

    def accept(self,machine):
        ch = machine.char(machine.get_pos())
        return InitTokenState(UnkownToken(ch))
    
    def name(self):
        return "FinishTokenState"


class IntLiteralState(State):
    def __init__(self,token):
        super(IntLiteralState,self).__init__(token)
    
    def name(self):
        return "IntLiteralState"
    
    def _is_digit(self,machine):
        ch = machine.char(machine.get_pos())
        if ch.isdigit():
            machine.forward()
            return IntLiteralState(self.token.add_text(ch))
        return None

    def accept(self,machine):
        return self._is_digit(machine) or self.finish_state()
       

class IdentifierState(State):
    #FIXME case not pass
    def __init__(self,token):
        super(IdentifierState,self).__init__(token)
    
    def name(self):
        return "IdentifierState"
    
    def _is_identifier(self,machine):
        ch = machine.char(machine.get_pos())
        # print("{0},{1}".format(machine.get_pos(),ch))
        
        if ch.isdigit() or ch.isalpha():
            machine.forward()
            return IdentifierState(self.token.add_text(ch))
        return None
    
    def accept(self,machine):
        return self._is_identifier(machine) or self.finish_state()


# if __name__ == "__main__":
#     print("aaa"[0])