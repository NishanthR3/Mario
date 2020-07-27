from colorama import Fore, Style


class Person(object):
    """docstring for person."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def create_person(self, win):
        pass

    def remove_person(self, win):
        win.matrix[self.x][self.y] = win.init[self.x][self.y]
        win.matrix[self.x + 1][self.y] = win.init[self.x + 1][self.y]
        win.matrix[self.x + 2][self.y] = win.init[self.x + 2][self.y]

    def move(self, dir, win):
        self.remove_person(win)
        self.x += (dir * self.vel)
        self.create_person(win)
