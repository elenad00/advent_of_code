""" 
--- Day 7: No Space Left On Device ---
You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input).

The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

lines that begin with $ are commands you executed

Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
    
Here, there are four directories: 
    / (the outermost directory), 
    a and d (which are in /), and 
    e (which is in a). 
    These directories also contain files of various sizes.

The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:
    e is 584 
    a is 94853 
        files f (size 29116)
        g (size 2557)
        h.lst (size 62596)
        i indirectly 
            (a contains e which contains i)
    d is 24933642
    / is 48381165

To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). 

Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
"""
import random
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
import aoc_utils

def generate_paths():
    paths = []
    path_sizes = {}
    current_path = []
    for line in input:
        if '$ cd' in line:
            _, cd, loc = line.split(' ')
            if loc == '..':
                _, current_path = add_to_paths(paths, current_path)
            elif loc == '/':
                current_path.append('/')
            else:
                current_path.append(loc+'/')
        elif '$ ls' not in line:
            size, name = line.split(' ')
            current_path.append(name)
            path, current_path = add_to_paths(paths, current_path)
            path_sizes[path] = int(size) if size!='dir' else 0
    return paths, path_sizes

def add_to_paths(paths: list, current_path: list):
    path = ''.join(current_path)
    paths.append(path)
    current_path = current_path[0:-1]
    return paths, current_path, path

def part_one():
    paths, path_sizes = generate_paths()
    print(path_sizes)
    return

input = aoc_utils.read_file('test_data/d7.txt')
part_one() # 1556596 too low