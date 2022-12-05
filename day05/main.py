#!/usr/bin/env python3

import re
import string
import copy

class Game(object):
    
    stacks = []
    split_ix = 0

    def __init__(self, filename='input'):
        super().__init__()
        self.input = self.parse_input(filename)
        n = (1 + len( self.input[0] )) // 4
        self.stacks = [ [] for _ in range(1 + n) ]
        

    def parse_input(self, filename):
        contents = []
        ix = 0
        for line in open(filename, 'r'):
            contents.append(line)
            if line.startswith(' 1'):
                self.split_ix = ix
            ix += 1
        return contents

    def process_input_1(self):
        line_no = self.split_ix
        while line_no > 0:
            line_no -= 1
            line = self.input[line_no]
            for ix, bucket in enumerate(self.chunkify(line, 4), start=1):
                bucket = bucket.strip()
                if len(bucket) >= 3:
                    self.stacks[ix].append(bucket[1])

    def process_input_2(self, flag = False):
        stacks = copy.deepcopy(self.stacks)
        for line in self.input[self.split_ix + 2:]:
            how_much, from_stack, to_stack = list(map(int, re.findall(r'\b\d+\b', line)))
            popped = []
            for n in range(how_much):
                popped.append(stacks[from_stack].pop())
            if flag is True:
                popped.reverse()
            stacks[to_stack].extend(popped)
        return ''.join(x[-1] if x else '' for x in stacks[1:])

    def chunkify(self, line, n):
        for i in range(0, len(line), n):
            yield line[i:i+n]

    def solve_a(self):
        self.process_input_1()
        return self.process_input_2()

    def solve_b(self):
        return self.process_input_2(flag = True)

def main():
    game = Game('input')
    
    part1 = game.solve_a()
    print(f'{part1=}')

    part2 = game.solve_b()
    print(f'{part2=}')

if __name__ == '__main__':
    main()
