import time

from Game import Game
from Ghost import Ghost
from Pacman import Pacman
if __name__ == '__main__':
    ghost1 = Ghost(4, 10)
    ghost2 = Ghost(6, 2)
    pacman = Pacman()
    g = Game(ghost1, ghost2, pacman)
    while True:
        ghost1.move(g.game_map)
        ghost2.move(g.game_map)
        pacman.move(g.minimax)
        print(ghost1.location)
        print(ghost2.location)
        print(pacman.location)
        g.print_game_map()





