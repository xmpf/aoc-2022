#!/usr/bin/env python3

import string
import heapq

class Game(object):
    def __init__(self, filename='input'):
        super().__init__()
        self.input = self.parse_input(filename)
        self.rows = 0
        self.cols = 0
        self.start = None
        self.end = None
        self.find_positions()

    def parse_input(self, filename):
        return [ line.strip() for line in open(filename, 'r') ]
    
    def find_positions(self):
        self.rows = len(self.input)
        self.cols = len(self.input[0])

        for x in range(self.rows):
            for y in range(self.cols):
                if self.input[x][y] == 'S':
                    self.start = (x, y)
                elif self.input[x][y] == 'E':
                    self.end = (x, y)
            if self.start and self.end:
                break
        return self.start, self.end

    def compute_height(self, x, y):
        height = self.input[x][y]
        if height == 'S':
            return 0
        elif height == 'E':
            return 25
        return string.ascii_lowercase.index(height)

    def find_neighbors(self, x, y):
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            i = x + di
            j = y + dj

            if not (i in range(self.rows) and j in range(self.cols)):
                continue
            
            if self.compute_height(i, j) <= self.compute_height(x, y) + 1:
                yield i, j

    def find_neighbors_b(self, x, y):
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            i = x + di
            j = y + dj

            if not (i in range(self.rows) and j in range(self.cols)):
                continue
            
            if self.compute_height(i, j) >= self.compute_height(x, y) - 1:
                yield i, j

    def find_path(self):
        queue = [(0, *self.start)]
        visited = [[False] * self.cols for _ in range(self.rows)]

        while True:
            steps, i, j = heapq.heappop(queue)

            if visited[i][j]:
                continue
            
            visited[i][j] = True
            if self.end == (i, j):
                return steps
            
            for ii, jj in self.find_neighbors(i, j):
                heapq.heappush(queue, (steps + 1, ii, jj))
            
    def find_path_b(self):
        queue = [(0, *self.end)]
        visited = [[False] * self.cols for _ in range(self.rows)]

        while True:
            steps, i, j = heapq.heappop(queue)

            if visited[i][j]:
                continue
            
            visited[i][j] = True
            if 0 == self.compute_height(i, j):
                return steps
            
            for ii, jj in self.find_neighbors_b(i, j):
                heapq.heappush(queue, (steps + 1, ii, jj))

    def solve_a(self):
        return self.find_path()

    def solve_b(self):
        return self.find_path_b()


def main():
    game = Game('input')
    
    part1 = game.solve_a()
    print(f'{part1=}')

    part2 = game.solve_b()
    print(f'{part2=}')

if __name__ == '__main__':
    main()
