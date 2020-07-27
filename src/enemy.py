from colorama import Fore, Style
from player import *


class Enemy(Mario_reddy):
    """docstring for Enemy."""

    def create_person(self, win):
        win.matrix[self.x][self.y] = Style.BRIGHT + Fore.CYAN + ']'
        win.matrix[self.x][self.y - 1] = Style.BRIGHT + Fore.CYAN + '['
        win.matrix[self.x + 1][self.y - 1] = Style.BRIGHT + Fore.CYAN + 'G'
        win.matrix[self.x + 2][self.y] = Style.BRIGHT + Fore.CYAN + '['
        win.matrix[self.x + 2][self.y - 1] = Style.BRIGHT + Fore.CYAN + ']'

    def move(self, dir, win):
        if self.x + dir * self.vel >= 124 and self.x + dir * self.vel <= 230:
            self.remove_person(win)
            self.x += (dir * self.vel)

    def attack(self, mario, win):
        if mario.x < self.x:
            self.move(-1, win)
        else:
            self.move(1, win)

    def __init__(self, x, y, win):
        super(Enemy, self).__init__(x, y, win)
        self.dir = 1
        self.vel = 1
        self.health = 1
        self.freeze = False
        self.power_activater = 0
        self.create_person(win)
