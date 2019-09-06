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
        machine.forward()
        self.token.clean_text()
        return self
    
    def name(self):
        return "InitTokenState"

class FinishTokenState():
    def __init__(self,token):
        self.token = token

    def accept(self,machine):
        ch = machine.char(machine.get_pos())
        return InitTokenState(UnkownToken(ch))
    
    def name(self):
        return "FinishTokenState"


class IntLiteralState():
    def __init__(self,token):
        self.token = token
    
    def name(self):
        return "IntLiteralState"

    def accept(self,machine):
        ch = machine.char(machine.get_pos())
        if ch.isdigit():
            machine.forward()
            return IntLiteralState(self.token.add_text(ch))
        else:
            return FinishTokenState(self.token)

class IdentifierState():
    def __init__(self):
        pass

class Int1State():
    def __init__(self):
        pass

class Int2State():
    def __init__(self):
        pass

class Int3State():
    def __init__(self):
        pass

class GtState():
    def __init__(self):
        pass

class LtState():
    def __init__(self):
        pass

class GeState():
    def __init__(self):
        pass

# if __name__ == "__main__":
#     print("aaa"[0])