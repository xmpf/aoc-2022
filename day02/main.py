#!/usr/bin/env python3

class Game(object):
    '''
    A: rock     : X : 1
    B: paper    : Y : 2
    C: scissors : Z : 3

    loose: 0
    draw: 3
    win: 6
    '''

    SCORE_LOSE = 0
    SCORE_DRAW = 3
    SCORE_WIN  = 6

    score_mappings = {
        -2: SCORE_WIN,
        -1: SCORE_LOSE,
         0: SCORE_DRAW,
         1: SCORE_WIN,
         2: SCORE_LOSE,
    }

    losing_move = {
        1: 3,
        2: 1,
        3: 2
    }

    winning_move = {
        1: 2,
        2: 3,
        3: 1
    }

    # char - 'A' == char - 'X'

    def __init__(self, filename='input'):
        super().__init__()
        self.input = self.parse_input(filename)
        

    def parse_input(self, filename):
        with open(filename, 'r') as f:
            contents = [ line.strip() for line in f.readlines() ]
        return contents

    def score_moves_a(self):
        score = 0
        for line in self.input:
            move_a, move_b = line.split(' ')
            move_a = ord(move_a) - ord('A') + 1
            move_b = ord(move_b) - ord('X') + 1
            score += self.score_mappings.get(move_b - move_a, 0) + move_b
        return score

    def score_moves_b(self):
        score = 0
        for line in self.input:
            move_a, move_b = line.split(' ')
            move_a = ord(move_a) - ord('A') + 1
            move_b = ord(move_b) - ord('X') + 1

            if move_b == 1:
                score += self.SCORE_LOSE + self.losing_move[move_a]
            elif move_b == 2:
                score += self.SCORE_DRAW + move_a
            elif move_b == 3:
                score += self.SCORE_WIN + self.winning_move[move_a]
        return score

def main():
    solution = Game('input')
    print(solution.score_moves_a())
    print(solution.score_moves_b())

if __name__ == '__main__':
    main()