#!/usr/bin/env python3

class Game(object):
    def __init__(self, filename='input', knot_len=2):
        super().__init__()
        self.input = self.parse_input(filename)
        self.knot_len = knot_len
        self.knots = [ [0, 0] for _ in range(knot_len) ]
        self.directions = {
            "R": [1,  0],
            "U": [0,  1],
            "L": [-1, 0],
            "D": [0, -1],
        }
        self.visited = set()

    def update_len(self, knot_len):
        self.knot_len = knot_len
        self.knots = [ [0, 0] for _ in range(knot_len) ]
        self.visited = set()

    def parse_input(self, filename):
        return [ line.strip() for line in open(filename, 'r') ]
    
    def are_touching(self, hx, hy, tx, ty):
        return abs(tx - hx) <= 1 and abs(ty - hy) <= 1

    def move(self, dx, dy):
        self.knots[0][0] += dx
        self.knots[0][1] += dy

        for i in range(1, self.knot_len):
            hx, hy = self.knots[i - 1]
            tx, ty = self.knots[i]

            if not self.are_touching(hx, hy, tx, ty):
                x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
                y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

                tx += x
                ty += y
            
            self.knots[i] = [tx, ty]

        self.visited.add(tuple(self.knots[-1]))

    def process_input(self):
        for line in self.input:
            d, n = line.split(" ")
            dx, dy = self.directions[d]
            for _ in range(int(n)):
                self.move(dx, dy)

    def solve_a(self):
        self.process_input()
        return len(self.visited)

    def solve_b(self):
        self.update_len(knot_len=10)
        self.process_input()
        return len(self.visited)

def main():
    game = Game('input')
    
    part1 = game.solve_a()
    print(f'{part1=}')

    part2 = game.solve_b()
    print(f'{part2=}')

if __name__ == '__main__':
    main()
