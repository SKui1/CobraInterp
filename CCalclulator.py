from itertools import repeat

from CScanner import cScan
from CToken import TTypes
from CToken import TToken

def cCalc(tokens):

    pos = 0

    while pos < len(tokens):
        t = tokens[pos]
        if t.type == TTypes.INT or t.type == TTypes.FLOAT:
            pos += 1
        elif t.mtype == TTypes.LOGIC:
            if t.type == TTypes.MINUS:
                pT = tokens[pos - 1]
                nT = tokens[pos + 1]
                tokens.pop(pos)
                tokens.pop(pos)
                tokens[pos - 1] = TToken(str(int(pT.value) - int(nT.value)), TTypes.INT, TTypes.SVAR)
            if t.type == TTypes.PLUS:
                pT = tokens[pos - 1]
                nT = tokens[pos + 1]
                tokens.pop(pos)
                tokens.pop(pos)
                tokens[pos - 1] = TToken(str(int(pT.value) + int(nT.value)), TTypes.INT, TTypes.SVAR)
    return tokens[0]


while True:
    print(cCalc(cScan(input(">: "))))