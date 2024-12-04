""" This module contains the basic functions for AOC without having
to rewrite the same code over and over again """

from typing import Any

INTS = [
    0,1,2,3,4,5,6,7,8,9,
    '0','1','2','3','4','5','6','7','8','9'
]
INTS_DICT = {
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'
}

INV_INTS_DICT = {
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

NUMBERS = [k for k in INV_INTS_DICT.keys()]
    

def get_symbols(input):
    symbols = []
    for line in input:
        for i in line:
            if i not in INTS and i!='.':
                if i not in symbols:
                    symbols.append(i)
    return symbols
    
def read_file(file_name: str, delim='\n', listify=False, list_delim=False)->list:
    """ """
    f = open(file_name, 'r')
    content = f.read()
    content = content.split(delim)
    if listify:
        content = [c.split(list_delim) for c in content] if list_delim else [list(c) for c in content]
        return content
    else:
        return content
    