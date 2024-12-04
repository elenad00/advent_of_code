import aoc_utils

traverse = {
    'n':(-1,0),
    'ne':(-1,1),
    'e':(0,1),
    'se':(1,1),
    's':(1,0),
    'sw':(1,-1),
    'w':(0,-1),
    'nw':(-1,-1)
}

class Grid_Navigator():
    x = 0
    y = 0
    visited = list()
    
    def __init__(self, file: str):
        self.grid = aoc_utils.read_file(file, listify=True)
        self.height = len(self.grid) # x
        self.width = len(self.grid[0]) # y
    
    def get_current_value(self):
        return self.grid[self.x][self.y]
    
    def move_direction(self, direction: str) -> bool:
        n, s, e, w = self._check_edge()
        x, y = self._mod_xy(direction)
        safe = False
        match direction:
            case "n":
                if n: safe=True
            case "ne":
                if n and e: safe=True
            case "e":
                if e: safe=True
            case "se":
                if s and e: safe=True
            case "s":
                if s: safe=True
            case "sw":
                if s and w: safe=True
            case "w":
                if w: safe=True
            case "nw": 
                if n and w: safe=True
            
        if safe:
            self.x = x
            self.y = y
            return True
        else:
            return False  
    
    def get_position_value(self, xy: list[int]) -> str | int:
        x, y = xy
        try: 
            return self.grid[x][y]
        except IndexError:
            return False
   
    def check_around(self) -> list[int]:
        nc,ec,sc,wc = self._check_edge()
        n = self.get_position_value(self._mod_xy('n')) if nc else 0
        ne = self.get_position_value(self._mod_xy('ne')) if nc and ec else 0
        e = self.get_position_value(self._mod_xy('e')) if ec else 0
        se = self.get_position_value(self._mod_xy('se')) if ec and sc else 0
        s = self.get_position_value(self._mod_xy('s')) if sc else 0
        sw = self.get_position_value(self._mod_xy('sw')) if ec and sc else 0
        w = self.get_position_value(self._mod_xy('w')) if wc else 0
        nw = self.get_position_value(self._mod_xy('nw')) if nc and wc else 0
        return [n, ne, e, se, s, sw, w, nw]
    
    def traverse_grid(self, direction: str, count: int) -> list[str, list]:
        ret = []
        coords = []
        for c in range(count):
            current_coords = [self.x, self.y]
            current_val = self.get_position_value(current_coords)
            if current_val:
                ret.append(current_val)
            else:
                print(
                    f"Cannot add {current_coords} due to indexing err, got as"
                    f" far as {ret} on move {c}"
                )
            success = self.move_direction(direction)
            if c<count-1:
                if not success:
                    print(f"Cannot move in direction {direction}, got as far as "
                        f"{ret} on move {c}")
                    return None, None
            coords.append(current_coords)
        return [''.join(ret), coords]
            
    def _check_edge(self) -> list[bool]:
        n = False if self.x == 0 else True
        e = False if self.y == self.width else True
        s = False if self.x == self.height else True
        w = False if self.y == 0 else True
        return [n,e,s,w]
    
    def _mod_xy(self, direction:str) -> list:
        xs,ys=traverse[direction]
        return [self.x+xs, self.y+ys]
    
    
