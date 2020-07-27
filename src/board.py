from colorama import Fore, Style
from config import *


class Window(object):
    """docstring for window."""

    def __init__(self):
        self.matrix = [[' '] * 30 for x in range(360)]
        self.init = [[' '] * 30 for x in range(360)]
        self.background = Background_Configaration()
        self.game_size = 240
        self.window_width = 120
        self.window_height = 30
        for x in range(240):
            self.matrix[x][0] = Style.BRIGHT + Fore.BLACK + 'x'
            self.matrix[x][29] = Style.BRIGHT + Fore.BLACK + 'x'
            self.init[x][0] = Style.BRIGHT + Fore.BLACK + 'x'
            self.init[x][29] = Style.BRIGHT + Fore.BLACK + 'x'
        for y in range(30):
            self.matrix[0][y] = Style.BRIGHT + Fore.BLACK + 'x'
            self.matrix[239][y] = Style.BRIGHT + Fore.BLACK + 'x'
            self.init[0][y] = Style.BRIGHT + Fore.BLACK + 'x'
            self.init[239][y] = Style.BRIGHT + Fore.BLACK + 'x'

    def __create_grass(self):
        for x in range(240):
            self.matrix[x][28] = Style.BRIGHT + Fore.GREEN + ','
            self.init[x][28] = Style.BRIGHT + Fore.GREEN + ','

    def __create_hole(self):
        for x in range(10):
            self.matrix[x + 112][28] = '\033[0m' + ' '
            self.init[x + 112][28] = '\033[0m' + ' '

    def __create_clouds(self, i, size):
        self.matrix[i - 1][4] = Style.BRIGHT + Fore.WHITE + '{'
        self.matrix[i + size][4] = Style.BRIGHT + Fore.WHITE + '}'
        for x in range(size):
            self.matrix[i + x][3] = Style.BRIGHT + Fore.WHITE + '_'
            self.matrix[i + x][5] = Style.BRIGHT + Fore.WHITE + '-'

    def __create_mountains(self, x):
        for i in range(7):
            self.matrix[i + x][i + 21] = '\033[0;33m' + '\\'
            self.matrix[x - i - 3][i + 21] = '\033[0;33m' + '/'
        self.matrix[x - 2][20] = '\033[0;33m' + '_'
        self.matrix[x - 1][20] = '\033[0;33m' + '_'

    def __create_bushes(self, x):
        iterate = 0
        for k in range(3):
            for i in range(3):
                if k % 2 == 1:
                    iterate = 3
                else:
                    iterate = 2
                for j in range(iterate):
                    self.matrix[i + x + k][27 -
                                           j] = '\033[0;32m' + '/'

    def __background_creator(self):
        self.__create_grass()
        self.__create_hole()
        for mount in self.background.mountains:
            self.__create_mountains(mount)
        for bush in self.background.bushes:
            self.__create_bushes(bush)
        for cloud in self.background.clouds:
            self.__create_clouds(*cloud)

    def update_frame(self, mario, life, time, level, goblin=None):
        self.__background_creator()
        if goblin is not None:
            goblin.create_person(self)
        mario.create_person(self)
        for y in range(30):
            for x in range(120):
                print(self.matrix[x + mario.pos][y], end="")
            print()
        if goblin is None:
            print(Fore.CYAN + "MARIO LIFE : " +
                  str(life) + " HEALTH : " + str(mario.health) +
                  " SCORE :  " + str(round(mario.score)) +
                  " TIME :  " + str(time) + " LEVEL : " + str(level))
        else:
            print(Fore.CYAN + "MARIO LIFE : " +
                  str(life) + " HEALTH : " + str(mario.health) +
                  " SCORE :  " + str(round(mario.score)) +
                  " TIME :  " + str(time) + " GOBLIN_HEALTH : " +
                  str(goblin.health) + " LEVEL : " + str(level) +
                  " Power Activation Time " + str(goblin.power_activater))
