from CToken import TTypes
from CToken import TToken

def cScan (line):
    tokens = []
    pos = 0
    
    while pos < len(line):
        char = line[pos]
        #basic single
        if char == ";":
            tokens.append(TToken(";", TTypes.SEMICOLON, TTypes.CONTROL))
            pos += 1
        elif char.isdigit():
            sT = pos
            eT = pos
            while eT < len(line) and (line[eT].isdigit() or line[eT] == "."):
                eT += 1
            tT = line[sT:eT]
            tokens.append(TToken(tT, TTypes.INT, TTypes.SVAR))
            pos = eT
        elif char == "(":
            tokens.append(TToken("(", TTypes.LEFT_PAREN, TTypes.SCASE))
            pos += 1
        elif char == ")":
            tokens.append(TToken(")", TTypes.RIGHT_PAREN, TTypes.SCASE))
            pos += 1
        elif char == "{":
            tokens.append(TToken("{", TTypes.LEFT_BRACE, TTypes.CONTROL))
            pos += 1
        elif char == "}":
            tokens.append(TToken("}", TTypes.RIGHT_BRACE, TTypes.CONTROL))
            pos += 1
        elif char == ",":
            tokens.append(TToken(",", TTypes.COMMA, TTypes.CONTROL))
            pos += 1
        elif char == ".":
            tokens.append(TToken(".", TTypes.DOT, TTypes.CONTROL))
            pos += 1
        elif char == "~":
            tokens.append(TToken("~", TTypes.TILDE, TTypes.SCASE))
            pos += 1
        elif char == "&":
            tokens.append(TToken("&", TTypes.AND, TTypes.BLOGIC))
            pos += 1
        elif char == "#":
            tokens.append(TToken("#", TTypes.HASH, TTypes.BLOGIC))
            pos += 1
        
        #Logic
        elif char == '-':
            tokens.append(TToken("-", TTypes.MINUS, TTypes.LOGIC))
            pos += 1
        elif char == '+':
            tokens.append(TToken("+", TTypes.PLUS, TTypes.LOGIC))
            pos += 1
        elif char == '/':
            tokens.append(TToken("/", TTypes.SLASH, TTypes.LOGIC))
            pos += 1
        elif char == '*':
            tokens.append(TToken("*", TTypes.STAR, TTypes.LOGIC))
            pos += 1
        
        
        #String
        elif char == '"':
            sT = pos + 1
            eT = pos + 1
            while eT < len(line) and line[eT] != '"':
                eT += 1
            tT = line[sT:eT]
            tokens.append(TToken(tT, TTypes.STRING, TTypes.SVAR))
            pos = eT + 1

        #Multi Char
        elif char.isalpha():
            sT = pos
            eT = pos
            while eT < len(line) and line[eT].isalnum():
                eT += 1
            tT = line[sT:eT]
            
            
            #Logic
            if tT == "is":
                tokens.append(TToken("is", TTypes.IS, TTypes.BLOGIC))
                pos = eT
            elif tT == "same":
                tokens.append(TToken("same", TTypes.SAME, TTypes.BLOGIC))
                pos = eT
            elif tT == "nope":
                tokens.append(TToken("nope", TTypes.NOPE, TTypes.BLOGIC))
                pos = eT
            elif tT == "diff":
                tokens.append(TToken("diff", TTypes.DIFF, TTypes.BLOGIC))
                pos = eT
            elif tT == "danger":
                tokens.append(TToken("danger", TTypes.DANGER, TTypes.BLOGIC))
                pos = eT
            elif tT == "safe":
                tokens.append(TToken("safe", TTypes.SAFE, TTypes.BLOGIC))
                pos = eT
            elif tT == "yes":
                tokens.append(TToken("yes", TTypes.YES, TTypes.BLOGIC))
                pos = eT
            elif tT == "no":
                tokens.append(TToken("no", TTypes.NO, TTypes.BLOGIC))
                pos = eT
            
            #Keywords
            else:
                tokens.append(TToken("?", TTypes.UNK, TTypes.UNK))
                pos += eT
        #Catch
        else:
            pos += 1
    
    return tokens