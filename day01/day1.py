#!/usr/bin/env python3

from collections import defaultdict

class Day1(object):

    elve_to_sum = defaultdict(int)
    maximum = 0

    def __init__(self, filename='./input'):
        super().__init__()
        self.contents = self.parse_file(filename)

    def parse_file(self, filename):
        with open(filename, 'r') as f:
            contents = [ line.rstrip() for line in f.readlines() ]
        return contents

    def compute_sum_and_max(self):
        ix = 0
        self.maximum = 0
        for calorie in self.contents:
            if calorie == '':
                self.maximum = max(self.maximum, self.elve_to_sum[ix])
                ix += 1
                continue
            self.elve_to_sum[ix] += int(calorie)
        return self.elve_to_sum, self.maximum

    def day1a(self):
        _, maximum = self.compute_sum_and_max()
        print(f'Part 1: {maximum}')

    def day1b(self):
        top_three_sum = sum(sorted(self.elve_to_sum.values(), reverse=True)[:3])
        print(f'Part 2: {top_three_sum}')

def main():
    day1 = Day1()
    day1.day1a()
    day1.day1b()

if __name__ == '__main__':
    main()