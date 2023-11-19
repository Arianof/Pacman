class Pacman:
    def __init__(self):
        self.location = [9, 10]

    def move(self, minimax):
        best_score, self.location = minimax(0, 0, 1, 0)
        print(best_score)

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
