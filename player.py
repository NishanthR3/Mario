from colorama import Fore, Style
from people import *


class Mario_reddy(Person):
    """docstring for mario_reddy."""

    def create_person(self, win):
        win.matrix[self.x][self.y] = Style.BRIGHT + Fore.RED + ']'
        win.matrix[self.x][self.y - 1] = Style.BRIGHT + Fore.RED + '['
        win.matrix[self.x + 1][self.y - 1] = Style.BRIGHT + Fore.RED + 'N'
        win.matrix[self.x + 2][self.y] = Style.BRIGHT + Fore.RED + '['
        win.matrix[self.x + 2][self.y - 1] = Style.BRIGHT + Fore.RED + ']'

    def remove_person(self, win):
        win.matrix[self.x][self.y] = win.init[self.x][self.y]
        win.matrix[self.x][self.y - 1] = win.init[self.x][self.y - 1]
        win.matrix[self.x + 1][self.y - 1] = win.init[self.x + 1][self.y - 1]
        win.matrix[self.x + 2][self.y] = win.init[self.x + 2][self.y]
        win.matrix[self.x + 2][self.y - 1] = win.init[self.x + 2][self.y - 1]

    def __init__(self, x, y, win):
        super(Mario_reddy, self).__init__(x, y)
        self.vel = 3
        self.neg = 1
        self.pos = 0
        self.isJump = False
        self.goDown = False
        self.jumpCount = 3
        self.fall = 1
        self.health = 6
        self.score = 0
        self.hit = False
        self.onSpring = False
        self.create_person(win)

    def move(self, dir, win, level):
        if level == 1 and \
                self.x + dir * self.vel >= 2 and \
                self.x + dir * self.vel <= 124:
            self.remove_person(win)
            self.pos += (dir * self.vel)
            self.x += dir * self.vel
        elif level == 2 and \
                self.x + dir * self.vel >= 124 and \
                self.x + dir * self.vel <= 230:
            self.remove_person(win)
            self.pos += (dir * self.vel)
            self.x += dir * self.vel

    def jump_init(self):
        self.isJump = True
        self.jumpCount = 3

    def jump(self, win):
        if self.jumpCount >= -3:
            self.neg = 1
            if self.jumpCount < 0:
                self.neg = -1
            self.remove_person(win)
            self.y -= ((self.jumpCount ** 2) * self.neg)
            self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = 3
            self.neg = 1

    def fall_down_start(self):
        self.goDown = True
        self.fall = 1
        self.jumpCount = 3
        self.isJump = False

    def fall_down(self, win):
        if self.y + self.fall ** 2 >= 27:
            self.remove_person(win)
            self.y = 27
            self.fall = 0
            self.goDown = False
            self.isJump = False
        else:
            self.remove_person(win)
            self.y += (self.fall ** 2)
            self.fall += 1
            self.isJump = False
