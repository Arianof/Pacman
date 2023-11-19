import random


class Ghost:
    def __init__(self, i, j):
        self.location = [i, j]

    def move(self, game_map):
        move_list = [1, 2, 3, 4]
        next_move = random.choice(move_list)
        if next_move == 1:
            self.move_up(game_map)
        elif next_move == 2:
            self.move_right(game_map)
        elif next_move == 3:
            self.move_down(game_map)
        else:
            self.move_left(game_map)

    def move_up(self, game_map):
        if game_map[self.location[0] - 1][self.location[1]] == 0:
            return
        else:
            self.location[0] -= 1

    def move_right(self, game_map):
        if game_map[self.location[0]][self.location[1] + 1] == 0:
            return
        else:
            self.location[1] += 1

    def move_down(self, game_map):
        if game_map[self.location[0] + 1][self.location[1]] == 0:
            return
        else:
            self.location[0] += 1

    def move_left(self, game_map):
        if game_map[self.location[0]][self.location[1] - 1] == 0:
            return
        else:
            self.location[1] -= 1

    def possible_moves(self, game_map):
        res = []
        if game_map[self.location[0]][self.location[1] - 1] != 0:
            res.append([self.location[0], self.location[1] - 1])
        if game_map[self.location[0] - 1][self.location[1]] != 0:
            res.append([self.location[0] - 1, self.location[1]])
        if game_map[self.location[0]][self.location[1] + 1] != 0:
            res.append([self.location[0], self.location[1] + 1])
        if game_map[self.location[0] + 1][self.location[1]] != 0:
            res.append([self.location[0] + 1, self.location[1]])
        return res

