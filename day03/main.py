#!/usr/bin/env python3

import string
import logging
from functools import reduce

logging.basicConfig(encoding='utf-8', level=logging.ERROR)

class Game(object):

    alphabet = string.ascii_lowercase + string.ascii_uppercase
    priorities = dict([(char, ix) for ix,char in enumerate(alphabet, start=1)])

    def __init__(self, filename='input'):
        super().__init__()
        self.input = self.parse_input(filename)

    def parse_input(self, filename):
        return [ line.strip() for line in open(filename, 'r') ]

    def split_at(self, lst, offset):
        return lst[:offset], lst[offset:]

    def solve_a(self):
        global_common_items = []
        for line in self.input:
            sack_a, sack_b = self.split_at(line, len(line) // 2)
            set_a = set(sack_a)
            set_b = set(sack_b)
            common_items = set_a.intersection(set_b)
            logging.debug(f'{sack_a=}, {sack_b=}, {common_items=}')
            global_common_items.extend(common_items)
        return reduce(lambda acc, x: acc + self.priorities.get(x, 0), global_common_items, 0)

    def chunkify(self, lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def solve_b(self):
        CHUNK_SIZE = 3
        badges = []
        for group in self.chunkify(self.input, CHUNK_SIZE):
            group_badge = set(group[0])
            for g in group[1:]:
                group_badge = group_badge.intersection(g)
            logging.debug(f'{group=} => {group_badge=}')
            badges.extend(group_badge)
        return reduce(lambda acc, x: acc + self.priorities.get(x, 0), badges, 0)

def main():
    day03 = Game('input')
    part1 = day03.solve_a()
    print(f'{part1=}')

    part2 = day03.solve_b()
    print(f'{part2=}')

if __name__ == '__main__':
    main()