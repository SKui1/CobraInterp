from CScanner import cScan
from CToken import TTypes
from CToken import TToken


def lCheck(tokens):
    pos = 0
    while pos < len(tokens):
        t = tokens[pos]
        if t.type == TTypes.INT or t.type == TTypes.FLOAT:
            pos += 1
        elif t.mtype == TTypes.LOGIC:
            if t.type == TTypes.MINUS:
                if tokens[pos + 1].type == TTypes.MINUS:
                    tokens[pos] = TToken("+", TTypes.PLUS, TTypes.LOGIC)
                    tokens.pop(pos + 1)
                else:
                    pT = tokens[pos - 1]
                    nT = tokens[pos + 1]
                    tokens.pop(pos)
                    tokens.pop(pos)
                    tmp = float(pT.value) - float(nT.value)
                    if tmp.is_integer():
                        tokens[pos - 1] = TToken(str(tmp), TTypes.INT, TTypes.SVAR)
                    else:
                        tokens[pos - 1] = TToken(str(tmp), TTypes.FLOAT, TTypes.SVAR)
            if t.type == TTypes.PLUS:
                pT = tokens[pos - 1]
                nT = tokens[pos + 1]
                tokens.pop(pos)
                tokens.pop(pos)
                tmp = float(pT.value) + float(nT.value)
                if tmp.is_integer():
                    tokens[pos - 1] = TToken(str(tmp), TTypes.INT, TTypes.SVAR)
                else:
                    tokens[pos - 1] = TToken(str(tmp), TTypes.FLOAT, TTypes.SVAR)
            if t.type == TTypes.SLASH:
                pT = tokens[pos - 1]
                nT = tokens[pos + 1]
                tokens.pop(pos)
                tokens.pop(pos)
                tmp = float(pT.value) / float(nT.value)
                if tmp.is_integer():
                    tokens[pos - 1] = TToken(str(tmp), TTypes.INT, TTypes.SVAR)
                else:
                    tokens[pos - 1] = TToken(str(tmp), TTypes.FLOAT, TTypes.SVAR)
            if t.type == TTypes.STAR:
                pT = tokens[pos - 1]
                nT = tokens[pos + 1]
                tokens.pop(pos)
                tokens.pop(pos)
                tmp = float(pT.value) * float(nT.value)
                if tmp.is_integer():
                    tokens[pos - 1] = TToken(str(tmp), TTypes.INT, TTypes.SVAR)
                else:
                    tokens[pos - 1] = TToken(str(tmp), TTypes.FLOAT, TTypes.SVAR)
    return tokens


def cCalc(tokens):
    tokens = lCheck(tokens)
    pos = 0

    while pos < len(tokens):
        t = tokens[pos]
        if t.type == TTypes.LEFT_PAREN or t.type == TTypes.RIGHT_PAREN:
            brace = []
            bpos = pos + 1
            while tokens[bpos].type != TTypes.LEFT_PAREN or tokens[bpos].type == TTypes.RIGHT_PAREN:
                brace.append(tokens[bpos])
                bpos += 1
            brace = lCheck(brace)
    return tokens[0]


while True:
    print(cCalc(cScan(input(">: "))))