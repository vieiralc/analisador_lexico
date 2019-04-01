import re

class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
        tokens = []
        source_code = self.source_code.split()

        source_index = 0
        error = False
        lines = 1

        while source_index < len(source_code):
            word = source_code[source_index]

            if word == "var": 
                tokens.append(["VAR_DECLARATION", word])
            
            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                if word[len(word) - 1] == ";":
                    tokens.append(['IDENTIFICADOR', word[0:len(word) - 1]])
                else:
                    tokens.append(['IDENTIFICADOR', word])

            elif re.match('[0-9]', word):
                if word[len(word) - 1] == ";":
                    tokens.append(['INTEGER', word[0:len(word) - 1]])
                else:
                    tokens.append(['INTEGER', word])

            elif word in "=/*-+":
                tokens.append(['OPERATOR', word])

            else:
                error = True
                print('ERROR in line', lines, 'Error: ', word)

            if word[len(word) - 1] == ";":
                tokens.append(['STATEMENT_END', ';'])
                lines += 1

            source_index += 1
        
        if not error:
            return tokens, lines