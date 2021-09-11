
from typing import Text


INTEGER,PLUS,MINUS,MULTI,DIV,EOF = 'INTEGER','PLUS','MINUS','MULTI','DIV','EOF'

class Token:
    
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __str__(self):
        return "Token({},{})".format(self.type,self.value)


class Interpreter:

    def __init__(self,text):
        self.text = text.replace(" ","")
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Error parsing input")

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1 :
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)


    def get_next_token(self):

        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER,self.integer())
            
            if self.current_char == "+":
                self.advance()
                return Token(PLUS,self.current_char)

            if self.current_char == '-':
                self.advance()
                return Token(MINUS,self.current_char)

            if self.current_char == '/':
                self.advance()
                return Token(DIV,self.current_char)

            if self.current_char == '*':
                self.advance()
                return Token(MULTI,self.current_char)

            self.error()
        return Token(EOF,None)
    
    def eat(self,token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def term(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        self.current_token = self.get_next_token()
        
        result = self.term()
        while self.current_token.type in (PLUS,MINUS,DIV,MULTI):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result += self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result -= self.term()
            elif token.type == DIV:
                self.eat(PLUS)
                result /= self.term()
            elif token.type == MULTI:
                self.eat(MULTI)
                result *= self.term()
            
        return result



def main():
    while True:
        try:
            text = input('>>> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

main()
    


        


