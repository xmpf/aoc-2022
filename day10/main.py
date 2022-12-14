#!/usr/bin/env python3

class Game(object):
    def __init__(self, filename='input'):
        super().__init__()
        self.input = self.parse_input(filename)
        self.clock = 0
        self.x = 1
        self.strengths = 0

    def parse_input(self, filename):
        return [ line.strip() for line in open(filename, 'r') ]
    
    def update_strengths(self):
        row = (self.clock - 1) // 40
        if self.clock % 40 == 20:
            self.strengths += self.x * self.clock

    def process_input(self):
        for line in self.input:
            self.clock += 1
            self.update_strengths()
            if line.startswith('addx'):
                value = int(line.split(" ")[1])
                self.clock += 1
                self.update_strengths()
                self.x += value

    def solve_a(self):
        self.process_input()
        return self.strengths

    def solve_b(self):
        pass

def main():
    game = Game('input')
    
    part1 = game.solve_a()
    print(f'{part1=}')

    part2 = game.solve_b()
    print(part2)

if __name__ == '__main__':
    main()
