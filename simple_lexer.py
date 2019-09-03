class Token(object):
    def __init__(self):
        self.type = ""
        self.text = ""


class SimpleLexer(object):
    def __init__(self):
        self.tokens = []
        self.token = None

    def init_token(self, ch=''):
        if len(self.token.text) > 0:
            self.tokens.append(self.token)
            self.token = Token()
            # return "INIT"

        if ch.isdigit():
            self.token.text += ch
            self.token.type = "IntLiteral"
            return "IntLiteral"
        elif ch.isalpha():
            if ch == "i":
                self.token.text += ch
                self.token.type = "ID_INT1"
                return "ID_INT1"
            else:
                self.token.text += ch
                self.token.type = "ID"
                return "ID"
        elif ch == "=":
            self.token.text += ch
            self.token.type = "Assignment"
            return "Assignment"
        elif ch == ">":
            self.token.text += ch
            self.token.type = "GT"
            return "GT"
        elif ch == "<":
            self.token.text += ch
            self.token.type = "LT"
            return "LT"
        elif ch == "+":
            self.token.text += ch
            self.token.type = "PLUS"
            return "PLUS"
        elif ch == "-":
            self.token.text += ch
            self.token.type = "MINUS"
            return "MINUS"
        elif ch == "*":
            self.token.text += ch
            self.token.type = "STAR"
            return "STAR"
        elif ch == "/":
            self.token.text += ch
            self.token.type = "SLASH"
            return "SLASH"
        elif ch == "(":
            self.token.text += ch
            self.token.type = "LeftParen"
            return "LeftParen"
        elif ch == ")":
            self.token.text += ch
            self.token.type = "RightParen"
            return "RightParen"
        elif ch == ";":
            self.token.text += ch
            self.token.type = "SemiColon"
            return "SemiColon"
        else:
            return "INIT"

    def tokenize(self, script = ""):
        self.token = Token()
        status = "INIT"
        for ch in script:
            if status == "INIT":
                status = self.init_token(ch)
                continue
            if status == "IntLiteral":
                if ch.isdigit():
                    self.token.text += ch
                else:
                    status = self.init_token(ch)
                continue
            if status == "ID":
                if ch.isdigit() or ch.isalpha():
                    self.token.text += ch
                else:
                    status = self.init_token(ch)
                continue
            if status == "GT":
                if ch == "=":
                    self.token.type = "GE"
                    self.token.text += ch
                else:
                    status = self.init_token(ch)
                continue

            if status == "GE":
                status = self.init_token(ch)
                continue

            if status == "LT":
                if ch == "=":
                    self.token.type = "LE"
                    self.token.text += ch
                    status = self.init_token(ch)
                else:
                    status = self.init_token(ch)
                continue

            if status == "ID_INT1":
                if ch == "n":
                    self.token.text += ch
                    self.token.type = "ID_INT2"
                    status = "ID_INT2"
                elif ch.isdigit() or ch.isalpha():
                    self.token.text += ch
                    self.token.type = "ID"
                    status = "ID"
                else:
                    status = self.init_token(ch)
                continue

            if status == "ID_INT2":
                if ch == "t":
                    self.token.text += ch
                    self.token.type = "ID_INT"
                elif ch.isdigit() or ch.isalpha():
                    self.token.text += ch
                    self.token.type = "ID"
                    status = "ID"
                else:
                    status = self.init_token(ch)
                continue

            if status == "Assignment":
                if ch == "=":
                    self.token.text += ch
                    self.token.type = "EQ"
                    status = self.init_token(ch)
                else:
                    status = self.init_token(ch)
                continue

            if status == "PLUS" or status == "MINUS" or status == "STAR" or status == "SLASH" \
            or status == "LeftParen" or status == "RightParen" or status == "SemiColon":
                status = self.init_token(ch)
                continue
            status = self.init_token(ch)
        if len(self.token.text) > 0:
            self.init_token(ch)
        return self.tokens


def dump(tokens):
    for token in tokens:
        print("{0}:{1}".format(token.type, token.text))


if __name__ == "__main__":
    script = "age >= 45;"
    tokens = SimpleLexer().tokenize(script)
    dump(tokens)
    print("-----------------")
    script = "age <= 45;"
    tokens = SimpleLexer().tokenize(script)
    dump(tokens)
    print("-----------------")
    script = "int it12 <= 45;"
    tokens = SimpleLexer().tokenize(script)
    dump(tokens)
    print("-----------------")
    script = "int it12 ==45;"
    tokens = SimpleLexer().tokenize(script)
    dump(tokens)
    print("-----------------")
    script = "int it12 = 45;"
    tokens = SimpleLexer().tokenize(script)
    dump(tokens)

    print("-----------------")
    script = "int a +b= 45;"
    tokens = SimpleLexer().tokenize(script)
    dump(tokens)

    print("-----------------")
    script = "int a +b*c/d>= 45;"
    tokens = SimpleLexer().tokenize(script)
    dump(tokens)

    print("-----------------")
    script = "int (a +b*c/d)>= 45;"
    tokens = SimpleLexer().tokenize(script)
    dump(tokens)


