class Pacman:
    def __init__(self):
        self.location = [9, 10]

    def move(self, minimax, manhattan_dis_calc, expectimax):
        manhattan_dis = manhattan_dis_calc()
        alpha = -1000000000
        beta = 100000000
        #res = minimax(0, 0, 4, 0, manhattan_dis, alpha, beta)
        res = expectimax(0, 0, 1, 0, manhattan_dis)
        if type(res) is int:
            best_score = res
        else:
            best_score, self.location = res
        #print(best_score)

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
