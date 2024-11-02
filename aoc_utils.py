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

class Grid_Navigator():
    x = 0
    y = 0
    visited = list()
    
    def __init__(self, file: str):
        self.generate_grid(file)
    
    def generate_grid(self, file: str):
        self.grid = get_input(file)
        
    def get_current_position_value(self) -> Any:
        return self.grid[self.x][self.y]

    
    def go_left(self) -> bool:
        l,r,u,d = self._check_edge()
        if l:
            self.x = self.x-1
        return l
    
    def go_right(self) -> bool:
        l,r,u,d = self._check_edge()
        if r:
            self.x = self.x+1
        return r
    
    def go_up(self) -> bool:
        l,r,u,d = self._check_edge()
        if u:
            self.y = self.y-1
        return u
    
    def go_down(self) -> bool:
        l,r,u,d = self._check_edge()
        if d:
            self.y = self.y+1
        return d
    
    def check_around(self) -> list[int]:
        grid = self.grid
        x = self.x
        y = self.y
        left, right, up, down = self._check_edge()
        l = grid[x-1][y] if left else 0
        r = grid[x+1][y] if right else 0
        u = grid[x][y-1] if up else 0
        d = grid[x][y+1] if down else 0
        return [l, r, u, d]
    
    def _check_edge(self) -> list[bool]:
        left, right, up, down = [True, True, True, True]
        if self.x == 0:
            up = False
        if self.x == 12:
            right = False
        if self.y == 0:
            left = False
        if self.y == 12:
            down = False
        return [left, right, up, down]
    

def get_symbols(input):
    symbols = []
    for line in input:
        for i in line:
            if i not in INTS and i!='.':
                if i not in symbols:
                    symbols.append(i)
    return symbols

def get_input(file: str):
    raw_input = open(file,'r').read().split('\n')
    raw_input = [list(i) for i in raw_input]
    input = list()
    for i in raw_input: input.append([int(v) for v in i])
    return input
    
def read_file(file_name: str, delim='\n', listify=False, list_delim=False)->list:
    f = open(file_name, 'r')
    content = f.read()
    content = content.split(delim)
    if listify:
        content = [c.split(list_delim) for c in content] if list_delim else [list(c) for c in content]
        return content
    else:
        return content
    