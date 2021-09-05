
from typing import Text


INTEGER,PLUS,EOF = 'INTEGER','PLUS','EOF'

class Token:
    
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __str__(self):
        return "Token({},{})".format(self.type,self.value)


class Interpreter:

    def __init__(self,text):
        self.text = text
        self.pos = 0

    def error(self):
        raise Exception("Error parsing input")

    def get_next_token(self):

        text = self.text
        if self.pos > len(self.text) -1:
            return Token(EOF,None)

        current_char = text[self.pos]

        if current_char.isdigit():
            self.pos += 1
            return Token(INTEGER,int(current_char))
        
        if current_char == "+":
            self.pos += 1
            return Token(PLUS,current_char)


        self.error()
    
    def eat(self,token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(INTEGER)

        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)


        return left.value + right.value



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
    


        


