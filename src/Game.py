import os
import time
import copy


class Game:
    def __init__(self, ghost1, ghost2, pacman):
        self.game_map = [
                    [0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0,
                     0, 0],
                    [0, 1, 1, 1, 1, 0,
                     1, 1, 1, 1, 1, 1,
                     1, 1, 0, 1, 1, 1,
                     1, 0],
                    [0, 1, 0, 0, 1, 0,
                     1, 0, 0, 0, 0, 0,
                     0, 1, 0, 1, 0, 0,
                     1, 0],
                    [0, 1, 0, 1, 1, 1,
                     1, 1, 1, 1, 1, 1,
                     1, 1, 1, 1, 1, 0,
                     1, 0],
                    [0, 1, 0, 1, 1, 1,
                     1, 0, 0, 1, 1, 0,
                     0, 1, 0, 0, 1, 0,
                     1, 0],
                    [0, 1, 1, 1, 1, 1,
                     1, 0, 1, 1, 1, 1,
                     0, 1, 1, 1, 1, 1,
                     1, 0],
                    [0, 1, 0, 1, 0, 0,
                     1, 0, 0, 0, 0, 0,
                     0, 1, 0, 0, 1, 0,
                     1, 0],
                    [0, 1, 0, 1, 1, 1,
                     1, 1, 1, 1, 1, 1,
                     1, 1, 1, 1, 1, 0,
                     1, 0],
                    [0, 1, 0, 0, 1, 0,
                     1, 0, 0, 0, 0, 0,
                     0, 1, 0, 1, 0, 0,
                     1, 0],
                    [0, 1, 1, 1, 1, 0,
                     1, 1, 1, 1, 1, 1,
                     1, 1, 0, 1, 1, 1,
                     1, 0],
                    [0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0,
                     0, 0]]
        self.ghost1 = ghost1
        self.ghost2 = ghost2
        self.pacman = pacman
        self.score = 0

    def print_game_map(self):
        print(self.count_score())
        self.update_game_map()
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
                if self.game_map[i][j] == 0:
                    print('X', end=' ')
                elif self.game_map[i][j] == 1:
                    print('.', end=' ')
                elif self.game_map[i][j] == 2:
                    print(' ', end=' ')

            print()
        time.sleep(0.25)
        os.system('clear')

    def calc_manhattan_distance(self):
        manhattan_distance_1 = abs(self.pacman.location[0] - self.ghost1.location[0]) + abs(self.pacman.location[1]
                                                                                            - self.ghost1.location[1])
        manhattan_distance_2 = abs(self.pacman.location[0] - self.ghost2.location[0]) + abs(self.pacman.location[1]
                                                                                            - self.ghost2.location[1])
        min_manhattan_distance = min(manhattan_distance_2, manhattan_distance_1)

        return min_manhattan_distance

    def given_location_possible_moves(self, location):
        res = []
        if self.game_map[location[0]][location[1] - 1] != 0:
            res.append([location[0], location[1] - 1])
        if self.game_map[location[0] - 1][location[1]] != 0:
            res.append([location[0] - 1, location[1]])
        if self.game_map[location[0]][location[1] + 1] != 0:
            res.append([location[0], location[1] + 1])
        if self.game_map[location[0] + 1][location[1]] != 0:
            res.append([location[0] + 1, location[1]])
        return res

    def bfs(self):
        mark = [[0 for x in range(22)] for y in range(22)]
        q = []
        dict = {tuple(self.pacman.location): 0}
        q.append(self.pacman.location)
        mark[self.pacman.location[0]][self.pacman.location[1]] = 1
        while len(q) != 0:
            t_loc = q.pop(0)
            if self.game_map[t_loc[0]][t_loc[1]] == 1:
                return dict[tuple(t_loc)]
            for move in self.given_location_possible_moves(t_loc):
                if mark[move[0]][move[1]] == 0:
                    mark[move[0]][move[1]] = 1
                    dict[tuple(move)] = dict[tuple(t_loc)] + 1
                    q.append(move)

        return 0

    def find_nearest_dot(self):
        return self.bfs()

    def count_remained_dots(self):
        remained_dots = 0
        for i in range(len(self.game_map)):
            for j in range(len(self.game_map[i])):
                if self.game_map[i][j] == 1:
                    remained_dots += 1
        return remained_dots

    def evaluate(self, eaten_dots, manhattan_dis, count_of_moves):
        nearest_dot = self.find_nearest_dot()
        remain_dots = self.count_remained_dots()
        if manhattan_dis <= 1:
            return 100 * self.calc_manhattan_distance() - 20 * nearest_dot
        return -4 * nearest_dot + 2 * eaten_dots + 1 * manhattan_dis - count_of_moves + 100000

    def count_score(self):
        if self.game_map[self.pacman.location[0]][self.pacman.location[1]] == 1:
            self.score += 10
        else:
            self.score -= 1
        return self.score

    def is_win(self):
        for i in self.game_map:
            if 1 in i:
                return False
        return True

    def is_lost(self):
        if self.pacman.location == self.ghost1.location or self.pacman.location == self.ghost2.location:
            return True

    def update_game_map(self):
        if self.game_map[self.pacman.location[0]][self.pacman.location[1]] == 1:
            self.game_map[self.pacman.location[0]][self.pacman.location[1]] = 2

    def minimax_update_game_map(self, eaten_dots):
        if self.game_map[self.pacman.location[0]][self.pacman.location[1]] == 1:
            self.game_map[self.pacman.location[0]][self.pacman.location[1]] = 2
            return eaten_dots + 30
        return eaten_dots

    def minimax(self, agent, curr_depth, depth, eaten_dots, manhattan_dis, alpha, beta):
        if self.is_win() or self.is_lost() or curr_depth == depth:
            return self.evaluate(eaten_dots, manhattan_dis, count_of_moves=curr_depth)
        if agent == 0:
            max_val = -100000000
            max_loc = [-1, -1]
            pac_tmp_loc = self.pacman.location
            game_map_tmp = copy.deepcopy(self.game_map)
            manhattan_dis_tmp = manhattan_dis
            for move in self.pacman.possible_moves(self.game_map):
                self.pacman.location = move
                new_eaten_dots = self.minimax_update_game_map(eaten_dots)
                new_manhattan_dis = self.calc_manhattan_distance()
                new_val = self.minimax((agent + 1) % 3, curr_depth, depth, new_eaten_dots, new_manhattan_dis, alpha, beta)
                if max_val < new_val:
                    max_loc = self.pacman.location
                    max_val = max(max_val, new_val)
                self.pacman.location = pac_tmp_loc
                manhattan_dis = manhattan_dis_tmp
                self.game_map = copy.deepcopy(game_map_tmp)
                alpha = max(alpha, max_val)
                if alpha >= beta:
                    break
            if curr_depth == 0:
                return max_val, max_loc
            return max_val
        if agent == 1:
            min_val_g1 = 10000000
            g1_tmp_loc = self.ghost1.location
            for move in self.ghost1.possible_moves(self.game_map):
                self.ghost1.location = move
                new_val = self.minimax((agent + 1) % 3, curr_depth, depth, eaten_dots, manhattan_dis, alpha, beta)
                self.ghost1.location = g1_tmp_loc
                if min_val_g1 > new_val:
                    min_val_g1 = new_val
                beta = min(min_val_g1, beta)
                if beta <= alpha:
                    break
            return min_val_g1
        if agent == 2:
            min_val_g2 = 10000000
            g2_tmp_loc = self.ghost2.location
            for move in self.ghost2.possible_moves(self.game_map):
                self.ghost2.location = move
                new_val = self.minimax((agent + 1) % 3, curr_depth + 1, depth, eaten_dots, manhattan_dis, alpha, beta)
                self.ghost2.location = g2_tmp_loc
                if min_val_g2 > new_val:
                    min_val_g2 = new_val
                beta = min(min_val_g2, beta)
                if beta <= alpha:
                    break
            return min_val_g2

    def expectimax(self, agent, curr_depth, depth, eaten_dots, manhattan_dis):
        if self.is_win() or self.is_lost() or curr_depth == depth:
            return self.evaluate(eaten_dots, manhattan_dis, count_of_moves=curr_depth)
        if agent == 0:
            max_val = -100000000
            max_loc = [-1, -1]
            pac_tmp_loc = self.pacman.location
            game_map_tmp = copy.deepcopy(self.game_map)
            manhattan_dis_tmp = manhattan_dis
            for move in self.pacman.possible_moves(self.game_map):
                self.pacman.location = move
                new_eaten_dots = self.minimax_update_game_map(eaten_dots)
                new_manhattan_dis = self.calc_manhattan_distance()
                new_val = self.expectimax((agent + 1) % 3, curr_depth, depth, new_eaten_dots, new_manhattan_dis)
                if max_val < new_val:
                    max_loc = self.pacman.location
                    max_val = max(max_val, new_val)
                self.pacman.location = pac_tmp_loc
                manhattan_dis = manhattan_dis_tmp
                self.game_map = copy.deepcopy(game_map_tmp)
            if curr_depth == 0:
                return max_val, max_loc
            return max_val
        if agent == 1:
            g1_tmp_loc = self.ghost1.location
            sum_val = 0
            for move in self.ghost1.possible_moves(self.game_map):
                self.ghost1.location = move
                sum_val += self.expectimax((agent + 1) % 3, curr_depth, depth, eaten_dots, manhattan_dis)
                self.ghost1.location = g1_tmp_loc
            return sum_val / len(self.ghost1.possible_moves(self.game_map))
        if agent == 2:
            g2_tmp_loc = self.ghost2.location
            sum_val = 0
            for move in self.ghost2.possible_moves(self.game_map):
                self.ghost2.location = move
                sum_val += self.expectimax((agent + 1) % 3, curr_depth + 1, depth, eaten_dots, manhattan_dis)
                self.ghost2.location = g2_tmp_loc
            return sum_val / len(self.ghost2.possible_moves(self.game_map))




