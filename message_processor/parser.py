from .lexer import INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF, REGEX, COMMA, STRING, Token

class AST:
    pass

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr

class RegexOp(AST):
    def __init__(self, attr, pattern):
        self.attr = attr
        self.pattern = pattern

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid syntax")

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
            return UnaryOp(token, self.factor())
        elif token.type == MINUS:
            self.eat(MINUS)
            return UnaryOp(token, self.factor())
        elif token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        elif token.type == REGEX:
            self.eat(REGEX)
            self.eat(LPAREN)
            attr = self.current_token.value  # This is the value of ATTR
            self.eat(STRING)  # We expect an integer in place of ATTR value
            self.eat(COMMA)  # Expect a comma
            pattern = self.current_token.value  # This is the regex pattern
            self.eat(STRING)  # Expect a string for the regex pattern
            self.eat(RPAREN)  # Closing parenthesis
            return RegexOp(attr, pattern)

    def term(self):
        node = self.factor()
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            self.eat(token.type)
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            self.eat(token.type)
            node = BinOp(left=node, op=token, right=self.term())
        return node

    def parse(self):
        node = self.expr()
        if self.current_token.type != EOF:
            self.error()
        return node
