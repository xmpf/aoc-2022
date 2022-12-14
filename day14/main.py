#!/usr/bin/env python3

class Game(object):
    def __init__(self, filename='input'):
        super().__init__()
        self.input = self.parse_input(filename)

    def parse_input(self, filename):
        return [ line.strip() for line in open(filename, 'r') ]
    
    def solve_a(self):
        raise NotImplementedError

    def solve_b(self):
        raise NotImplementedError

def main():
    game = Game('input')
    
    part1 = game.solve_a()
    print(f'{part1=}')

    part2 = game.solve_b()
    print(f'{part2=}')

if __name__ == '__main__':
    main()
