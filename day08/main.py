#!/usr/bin/env python3

from collections import defaultdict

class Game(object):
    def __init__(self, filename='input'):
        super().__init__()
        self.input = self.parse_input(filename)
        self.rows = len(self.input)
        self.cols = len(self.input[0])
        self.grid = defaultdict(bool)

    def parse_input(self, filename):
        return [ [ int(x) for x in line.strip() ] for line in open(filename, 'r') ]
    
    def traverse_top_down(self):
        for col in range(0, self.cols - 1):
            prev_item = self.input[0][col]
            for row in range(self.rows):
                if self.input[row][col] > prev_item and not self.grid[(row, col)]:
                    self.grid[(row, col)] = True
                prev_item = max(prev_item, self.input[row][col])
            

    def traverse_bottom_up(self):
        for col in range(0, self.cols):
            prev_item = self.input[self.rows - 1][col]
            for row in range(self.rows - 1, -1, -1):
                if self.input[row][col] > prev_item and not self.grid[(row, col)]:
                    self.grid[(row, col)] = True
                prev_item = max(prev_item, self.input[row][col])

    def traverse_left_right(self):
        for row in range(self.rows):
            prev_item = self.input[row][0]
            for col in range(1, self.cols):
                if self.input[row][col] > prev_item and not self.grid[(row, col)]:
                    self.grid[(row, col)] = True
                prev_item = max(prev_item, self.input[row][col])

    def traverse_right_left(self):
        for row in range(self.rows):
            prev_item = self.input[row][-1]
            for col in range(self.cols - 1, -1, -1):
                if self.input[row][col] > prev_item and not self.grid[(row, col)]:
                    self.grid[(row, col)] = True
                prev_item = max(prev_item, self.input[row][col])

    def traverse_edges(self):
        for col in range(self.cols):
            self.grid[(0,  col)] = True
            self.grid[(self.rows - 1,  col)] = True

        for row in range(1, self.rows - 1):
            self.grid[(row,  0)] = True
            self.grid[(row, self.cols - 1)] = True
        return 2 * (self.rows + self.cols - 2)

    def traverse(self):
        self.traverse_edges()
        self.traverse_left_right()
        self.traverse_right_left()
        self.traverse_top_down()
        self.traverse_bottom_up()

    def solve_a(self):
        self.traverse()
        return sum(self.grid.values())

    def solve_b(self):
        DIR = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        ans = 0
        for i in range(self.rows):
            for j in range(self.cols):
                curr = self.input[i][j]
                score = 1
                for di, dj in DIR:
                    ii, jj = i + di, j + dj
                    dist = 0
                    while (0 <= ii < self.rows and 0 <= jj < self.cols) and self.input[ii][jj] < curr:
                        dist += 1
                        ii += di
                        jj += dj
                        if (0 <= ii < self.rows and 0 <= jj < self.cols) and self.input[ii][jj] >= curr:
                            dist += 1
                    score *= dist
                ans = max(ans, score)
        return ans
                    

def main():
    # game = Game('example_input')
    game = Game('input')
    
    part1 = game.solve_a()
    print(f'{part1=}')

    part2 = game.solve_b()
    print(f'{part2=}')

if __name__ == '__main__':
    main()
