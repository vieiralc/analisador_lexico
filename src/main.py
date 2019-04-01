import lexer

def main():
    content = ""
    with open('test.lang', 'r') as file:
        content = file.read()
    
    lex = lexer.Lexer(content)
    tokens = lex.tokenize()

    if tokens is not None:
        print(tokens)

main()