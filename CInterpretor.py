from CScanner import cScan
from CToken import TTypes
from CToken import TToken

cVars = {}
def lCheck(tokens):
    pos = 0
    while pos < len(tokens):
        t = tokens[pos]
        if t.type == TTypes.INT or t.type == TTypes.FLOAT or t.type == TTypes.STRING or t.type == TTypes.YES or t.type == TTypes.NO:
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
                if pT.type == TTypes.UNK:
                    pT = cVars[pT.value][0]
                if pT.type == TTypes.STRING:
                    tokens[pos - 1] = TToken(str(pT.value + nT.value), TTypes.STRING, TTypes.SVAR)
                else:
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
        elif t.mtype == TTypes.BLOGIC:
            if t.type == TTypes.IS:
                # equality operator (=)
                pT = tokens[pos - 1]
                nT = tokens[pos + 1:]
                cVars[pT.value] = lCheck(nT)[:]
                return cVars[pT.value]
            if t.type == TTypes.SAME:
                # double equality operator (==)
                pT = tokens[pos - 1]
                nT = tokens[pos + 1]
                tokens.pop(pos)
                tokens.pop(pos)
                try:
                    if pT.value == nT.value:
                        tokens[pos - 1] = TToken("yes", TTypes.YES, TTypes.BLOGIC)
                    else:
                        tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
                except:
                    tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
            if t.type == TTypes.NOPE:
                # not operator (!)
                nT = tokens[pos + 1]
                tokens.pop(pos)
                try:
                    if nT.type == TTypes.NO:
                        tokens[pos] = TToken("yes", TTypes.YES, TTypes.BLOGIC)
                    else:
                        tokens[pos] = TToken("no", TTypes.NO, TTypes.BLOGIC)
                except:
                    tokens[pos] = TToken("no", TTypes.NO, TTypes.BLOGIC)
            if t.type == TTypes.DIFF:
                # not equal operator (!=)
                pT = tokens[pos - 1]
                nT = tokens[pos + 1]
                tokens.pop(pos)
                tokens.pop(pos)
                try:
                    if pT.value != nT.value:
                        tokens[pos - 1] = TToken("yes", TTypes.YES, TTypes.BLOGIC)
                    else:
                        tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
                except:
                    tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
            if t.type == TTypes.DANGER:
                # greater than (>)
                pT = tokens[pos - 1]
                nT = tokens[pos + 1]
                tokens.pop(pos)
                tokens.pop(pos)
                if nT.type != TTypes.IS:
                    try:
                        if pT.value > nT.value:
                            tokens[pos - 1] = TToken("yes", TTypes.YES, TTypes.BLOGIC)
                        else:
                            tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
                    except:
                        tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
                else:
                    nT = tokens[pos]
                    tokens.pos(pos)
                    try:
                        if pT.value >= nT.value:
                            tokens[pos - 1] = TToken("yes", TTypes.YES, TTypes.BLOGIC)
                        else:
                            tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
                    except:
                        tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
            if t.type == TTypes.SAFE:
                # less than (<)
                pT = tokens[pos - 1]
                nT = tokens[pos + 1]
                tokens.pop(pos)
                tokens.pop(pos)
                if nT.type != TTypes.IS:
                    try:
                        if pT.value < nT.value:
                            tokens[pos - 1] = TToken("yes", TTypes.YES, TTypes.BLOGIC)
                        else:
                            tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
                    except:
                        tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
                else:
                    nT = tokens[pos]
                    tokens.pos(pos)
                    try:
                        if pT.value <= nT.value:
                            tokens[pos - 1] = TToken("yes", TTypes.YES, TTypes.BLOGIC)
                        else:
                            tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
                    except:
                        tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
            if t.type == TTypes.AND:
                # and operator
                pT = tokens[pos - 1]
                nT = tokens[pos + 1]
                tokens.pop(pos)
                tokens.pop(pos)
                try:
                    if pT.type == TTypes.YES and nT.type == TTypes.YES:
                        tokens[pos - 1] = TToken("yes", TTypes.YES, TTypes.BLOGIC)
                    else:
                        tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
                except:
                    tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
            if t.type == TTypes.HASH:
                # or operator
                pT = tokens[pos - 1]
                nT = tokens[pos + 1]
                tokens.pop(pos)
                tokens.pop(pos)
                try:
                    if pT.type == TTypes.YES or nT.type == TTypes.YES:
                        tokens[pos - 1] = TToken("yes", TTypes.YES, TTypes.BLOGIC)
                    else:
                        tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
                except:
                    tokens[pos - 1] = TToken("no", TTypes.NO, TTypes.BLOGIC)
        elif t.mtype == TTypes.KWORD:
            if t.type == TTypes.HISS:
                nT = tokens[pos + 1:]
                return  nT[0]
        else:
            pos += 1
    return tokens


def cCalc(tokens):
    pos = 0

    while pos < len(tokens):
        t = tokens[pos]
        if t.type == TTypes.UNK and tokens[pos + 1].type != TTypes.IS:
            if cVars.get(t.value) != None:
                tokens[pos] = cVars[t.value]
            pos += 1
        elif t.type == TTypes.LEFT_PAREN:
            brace = []
            bS = pos
            bpos = pos + 1
            while tokens[bpos].type != TTypes.LEFT_PAREN and tokens[bpos].type != TTypes.RIGHT_PAREN:
                brace.append(tokens[bpos])
                bpos += 1
            brace = lCheck(brace)
            for i in range(0, bpos - bS):
                tokens.pop(bS)
            tokens[pos] = brace[0]
            print(tokens)
            break
        else:
            pos += 1

    tokens = lCheck(tokens)
    
    return tokens[0]


while True:
    a = cScan(input(">: "))
    print(a)
    print("~~~~")
    print(cCalc(a))