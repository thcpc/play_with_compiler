from state_machine import *

class SimpleLexer():
    def __init__(self):
        self.tokens = []
    
    def tokenize(self,script):
        machine = StateMachine(script)
        while(machine.has_next()):
            state = machine.next()
            if state.name() == "FinishTokenState":
                self.tokens.append(state.token)


if __name__=="__main__":
    lex = SimpleLexer()
    lex.tokenize("1;222 3 1")
    for token in lex.tokens:
        print(token.to_s())