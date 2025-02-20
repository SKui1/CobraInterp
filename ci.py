import math
import json
import os
import time
import random


class Buff_m:
    b_main = []
    b_current = []
    v_global = {}
    l_strike = []
    l_slither = []
    l_coil = []

def i_lines (_f):
    _buffer = []
    _buffer = _f.readlines()
    return _buffer

def cobra (_f):
    buffer_main = Buff_m
    with open(_f) as f:
        buffer_main.b_main = i_lines(f)
        for i in buffer_main.b_main:
            print (i)
        
cobra("cobra test.txt")