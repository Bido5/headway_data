
INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF, REGEX, COMMA, STRING = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF', 'REGEX', 'COMMA', 'STRING'
)

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"

    def __repr__(self):
        return self.__str__()


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Invalid character")

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def string(self):
        result = ''
        self.advance()  # Skip the opening quote
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        if self.current_char == '"':
            self.advance()  # Skip the closing double quote
        return result

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.text[self.pos:self.pos + 5] == "Regex" and \
                    (self.pos + 5 == len(self.text) or self.text[self.pos + 5].isspace() or self.text[
                        self.pos + 5] in '()'):
                self.pos += 5
                self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
                return Token(REGEX, "Regex")
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            if self.current_char == '"':
                return Token(STRING, self.string())
            if self.current_char == ',':
                self.advance()
                return Token(COMMA, ',')
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')
            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')
            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')
            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')
            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')
            self.error()
        return Token(EOF, None)

