#!/usr/bin/env python3

from collections import defaultdict

class Game(object):
    def __init__(self, filename='input'):
        super().__init__()
        self.input = self.parse_input(filename)
        self.fs = defaultdict(int)

    def parse_input(self, filename):
        return [ line.strip().split() for line in open(filename, 'r') ]
    
    def process_input(self):
        dirstack = []
        for line in self.input:
            if line[1] == 'cd' and line[2] == '..':
                dirstack.pop()
            elif line[1] == 'cd':
                dirstack.append(line[2])
            elif line[1] == 'ls':
                continue
            elif line[0] == 'dir':
                continue
            else:
                cdir = ""
                for d in dirstack:
                    cdir += d   
                    cwd = '/'.join(cdir)
                    self.fs[cwd] += int(line[0])

    def solve_a(self):
        self.process_input()
        return sum(filter(lambda x: x < 100000, self.fs.values()))


    def solve_b(self):
        total_size = 70000000
        needed_size = 30000000
        max_used = total_size - needed_size
        to_free = self.fs['/'] - max_used
        values = list(self.fs.values())
        min_val = values[0]
        for sz in values[1:]:
            if sz >= to_free:
                min_val = min(min_val, sz)
        return min_val

def main():
    game = Game('input')
    
    part1 = game.solve_a()
    print(f'{part1=}')

    part2 = game.solve_b()
    print(f'{part2=}')

if __name__ == '__main__':
    main()
