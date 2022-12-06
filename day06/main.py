#!/usr/bin/env python3

class Game(object):

    window_size_part_a = 4
    window_size_part_b = 14

    def __init__(self, filename='input'):
        super().__init__()
        self.input = self.parse_input(filename)

    def parse_input(self, filename):
        return [ line.strip() for line in open(filename, 'r') ]
    
    def find_marker(self, line, window_size):
        strlen = len(line)
        offset = 0
        marker = None
        for start in range(strlen - window_size + 1):
            end = start + window_size
            window = line[start:end]
            if len(set(window)) == window_size:
                offset = end
                marker = window
                break
        return marker, offset

    def solve_a(self):
        for line in self.input:
            marker, offset = self.find_marker(line, self.window_size_part_a)
            print(f'{marker=} {offset=}')
        return offset

    def solve_b(self):
        for line in self.input:
            marker, offset = self.find_marker(line, self.window_size_part_b)
            print(f'{marker=} {offset=}')
        return offset

def main():
    game = Game('input')
    
    part1 = game.solve_a()
    print(f'{part1=}\n')

    part2 = game.solve_b()
    print(f'{part2=}')

if __name__ == '__main__':
    main()
