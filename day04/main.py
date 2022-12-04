#!/usr/bin/env python3

class Game(object):
    def __init__(self, filename='input'):
        super().__init__()
        self.input = self.parse_input(filename)

    def parse_input(self, filename):
        return [ line.strip() for line in open(filename, 'r') ]

    def solve_a(self):
        count = 0
        for line in self.input:
            group_a, group_b = map(lambda x: x.split('-'), line.split(','))
            group_a = list(map(int, group_a))
            group_b = list(map(int, group_b))

            if (group_b[0] <= group_a[0] and group_b[1] >= group_a[1]) or \
               (group_a[0] <= group_b[0] and group_a[1] >= group_b[1]):
                count += 1
        return count

    def solve_b(self):
        count = 0
        for line in self.input:
            group_a, group_b = map(lambda x: x.split('-'), line.split(','))
            group_a = list(map(int, group_a))
            group_b = list(map(int, group_b))
            if group_b[0] <= group_a[0] <= group_b[1] or \
               group_b[0] <= group_a[1] <= group_b[1] or \
               group_a[0] <= group_b[0] <= group_a[1] or \
               group_a[0] <= group_b[1] <= group_a[1]:
                count += 1
        return count

def main():
    game = Game('input')
    
    part1 = game.solve_a()
    print(f'{part1=}')

    part2 = game.solve_b()
    print(f'{part2=}')

if __name__ == '__main__':
    main()
