from dataclasses import dataclass

class TTypes:
    #Single Char
    LEFT_PAREN = 1
    RIGHT_PAREN = 2
    LEFT_BRACE = 3
    RIGHT_BRACE = 4
    COMMA = 5
    DOT = 6
    MINUS = 7
    PLUS = 8
    SEMICOLON = 9
    SLASH = 10
    STAR = 11
    TILDE = 12
    AND = 13
    HASH = 14

    #Keywords
    HISS = 15
    SNEG = 16
    HATCH = 17
    STRIKE = 18
    RECOIL = 19
    SLITHER = 20
    SERPENT = 21
    COIL = 22
    THINK = 23

    #Logic
    IS = 24
    SAME = 25
    NOPE = 26
    DIFF = 27
    DANGER = 28
    SAFE = 29
    
    #types
    INT = 30
    FLOAT = 31
    STRING = 32
    
    #M types
    LOGIC = 33
    BLOGIC = 34
    CONTROL = 35
    KWORD = 36
    SCASE = 37
    SVAR = 38
    
    #Outcome
    YES = 39
    NO = 40
    
    
    #Other
    UNK = 41

@dataclass
class TToken:
    value: str
    type: TTypes
    mtype: TTypes

    def __repr__(self):
        return self.value