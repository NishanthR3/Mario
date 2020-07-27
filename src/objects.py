from colorama import Fore, Style


class Box(object):
    """docstring for box."""

    def remove_box(self, win):
        for y in range(2):
            for x in range(3):
                win.matrix[self.x + x][self.y + y] = " "
                win.init[self.x + x][self.y + y] = " "

    def create_box(self, win):
        for y in range(2):
            for x in range(3):
                win.matrix[self.x + x][self.y +
                                       y] = Style.BRIGHT + Fore.YELLOW + self.c
                win.init[self.x + x][self.y +
                                     y] = Style.BRIGHT + Fore.YELLOW + self.c

    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        self.c = 'o'
        self.create_box(win)


class Spring(Box):
    """docstring for powerup_box."""

    def __init__(self, x, y, win):
        super(Spring, self).__init__(x, y, win)
        self.c = '?'
        self.create_box(win)


class Pipe(object):
    """docstring for pipe."""

    def create_pipe(self, win):
        for x in range(6):
            win.matrix[self.x][self.h + x] = Style.BRIGHT + Fore.BLUE + '|'
            win.matrix[self.x + 5][self.h + x] = Style.BRIGHT + Fore.BLUE + '|'
            win.init[self.x + 5][self.h + x] = Style.BRIGHT + Fore.BLUE + '|'
            win.init[self.x][self.h + x] = Style.BRIGHT + Fore.BLUE + '|'
        for x in range(4):
            win.matrix[self.x + 1 + x][self.h -
                                       1] = Style.BRIGHT + Fore.BLUE + '_'
            win.init[self.x + 1 + x][self.h -
                                     1] = Style.BRIGHT + Fore.BLUE + '_'

    def __init__(self, x, win):
        self.x = x
        self.h = 22
        self.create_pipe(win)


class Coins(object):
    """docstring for Coins."""

    def create_coin(self, win):
        win.matrix[self.x][self.y] = Style.BRIGHT + Fore.MAGENTA + 'O'
        win.init[self.x][self.y] = Style.BRIGHT + Fore.MAGENTA + 'O'

    def remove_coin(self, win):
        win.matrix[self.x][self.y] = ' '
        win.init[self.x][self.y] = ' '

    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        self.create_coin(win)
