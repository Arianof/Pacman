import os
import time


class Game:
    def __init__(self, ghost1, ghost2, pacman):
        self.game_map = [
                    ['X', 'X', 'X', 'X', 'X', 'X',
                     'X', 'X', 'X', 'X', 'X', 'X',
                     'X', 'X', 'X', 'X', 'X', 'X',
                     'X', 'X'],
                    ['X', ' ', ' ', ' ', ' ', 'X',
                     ' ', ' ', ' ', ' ', ' ', ' ',
                     ' ', ' ', 'X', ' ', ' ', ' ',
                     ' ', 'X'],
                    ['X', ' ', 'X', 'X', ' ', 'X',
                     ' ', 'X', 'X', 'X', 'X', 'X',
                     'X', ' ', 'X', ' ', 'X', 'X',
                     ' ', 'X'],
                    ['X', ' ', 'X', ' ', ' ', ' ',
                     ' ', ' ', ' ', ' ', ' ', ' ',
                     ' ', ' ', ' ', ' ', ' ', 'X',
                     ' ', 'X'],
                    ['X', ' ', 'X', ' ', 'X', 'X',
                     ' ', 'X', 'X', ' ', ' ', 'X',
                     'X', ' ', 'X', 'X', ' ', 'X',
                     ' ', 'X'],
                    ['X', ' ', ' ', ' ', ' ', ' ',
                     ' ', 'X', ' ', ' ', ' ', ' ',
                     'X', ' ', ' ', ' ', ' ', ' ',
                     ' ', 'X'],
                    ['X', ' ', 'X', ' ', 'X', 'X',
                     ' ', 'X', 'X', 'X', 'X', 'X',
                     'X', ' ', 'X', 'X', ' ', 'X',
                     ' ', 'X'],
                    ['X', ' ', 'X', ' ', ' ', ' ',
                     ' ', ' ', ' ', ' ', ' ', ' ',
                     ' ', ' ', ' ', ' ', ' ', 'X',
                     ' ', 'X'],
                    ['X', ' ', 'X', 'X', ' ', 'X',
                     ' ', 'X', 'X', 'X', 'X', 'X',
                     'X', ' ', 'X', ' ', 'X', 'X',
                     ' ', 'X'],
                    ['X', ' ', ' ', ' ', ' ', 'X',
                     ' ', ' ', ' ', ' ', ' ', ' ',
                     ' ', ' ', 'X', ' ', ' ', ' ',
                     ' ', 'X'],
                    ['X', 'X', 'X', 'X', 'X', 'X',
                     'X', 'X', 'X', 'X', 'X', 'X',
                     'X', 'X', 'X', 'X', 'X', 'X',
                     'X', 'X']]
        self.ghost1 = ghost1
        self.ghost2 = ghost2
        self.pacman = pacman

    def print_game_map(self):
        for i in range(len(self.game_map)):
            for j in range(len(self.game_map[i])):
                if [i, j] == self.ghost1.location:
                    print('1', end=' ')
                    continue
                if [i, j] == self.ghost2.location:
                    print('2', end=' ')
                    continue
                elif [i, j] == self.pacman.location:
                    print('P', end=' ')
                    continue
                print(self.game_map[i][j], end=' ')
            print()
        time.sleep(0.5)
        os.system('clear')

    def is_game_over(self):
        if self.pacman.location == self.ghost1.location or self.pacman.location == self.ghost2.location:
            return True

    def evaluate(self):
        manhattan_distance_1 = abs(self.pacman.location[0] - self.ghost1.location[0]) + abs(self.pacman.location[1]
                                                                                            - self.ghost1.location[1])
        manhattan_distance_2 = abs(self.pacman.location[0] - self.ghost2.location[0]) + abs(self.pacman.location[1]
                                                                                            - self.ghost2.location[1])
        min_manhattan_distance = min(manhattan_distance_2, manhattan_distance_1)

        return min_manhattan_distance

    def is_win(self):
        pass

    def is_lost(self):
        if self.pacman.location == self.ghost1.location or self.pacman.location == self.ghost2.location:
            return True

    def minimax(self, agent, curr_depth, depth):
        if self.is_win() or self.is_lost() or curr_depth == depth:
            return self.evaluate()
        if agent == 0:
            max_val = -100000000
            max_loc = [-1, -1]
            pac_tmp_loc = self.pacman.location
            for move in self.pacman.possible_moves(self.game_map):
                self.pacman.location = move
                new_val = self.minimax((agent + 1) % 3, curr_depth, depth)
                if max_val < new_val:
                    max_loc = self.pacman.location
                self.pacman.location = pac_tmp_loc
                max_val = max(max_val, new_val)
            if curr_depth == 0:
                return max_val, max_loc
            return max_val
        if agent == 1:
            min_val_g1 = 10000000
            g1_tmp_loc = self.ghost1.location
            for move in self.ghost1.possible_moves(self.game_map):
                self.ghost1.location = move
                new_val = self.minimax((agent + 1) % 3, curr_depth, depth)
                self.ghost1.location = g1_tmp_loc
                min_val_g1 = min(min_val_g1, new_val)
            return min_val_g1
        if agent == 2:
            min_val_g2 = 10000000
            g2_tmp_loc = self.ghost2.location
            for move in self.ghost2.possible_moves(self.game_map):
                self.ghost2.location = move
                new_val = self.minimax((agent + 1) % 3, curr_depth + 1, depth)
                self.ghost2.location = g2_tmp_loc
                min_val_g2 = min(min_val_g2, new_val)
            return min_val_g2


