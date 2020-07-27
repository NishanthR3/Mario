from colorama import Fore, Style
from people import *


class Tort(Person):
    """docstring for tort."""

    def create_person(self, win):
        win.matrix[self.x][self.y] = Fore.WHITE + '<'
        win.matrix[self.x + 1][self.y] = Fore.WHITE + 'O'
        win.matrix[self.x + 2][self.y] = Fore.WHITE + '>'

    def __init__(self, x, y, vel, face, e1, e2, win):
        super(Tort, self).__init__(x, y)
        self.vel = vel
        self.face = face
        self.e1 = e1
        self.e2 = e2
        self.create_person(win)

    def gaurd(self, win):
        if self.x - self.vel < self.e1:
            self.x = self.e1
            self.face = 1
        elif self.x + self.vel > self.e2:
            self.x = self.e2
            self.face = -1
        self.move(self.face, win)
