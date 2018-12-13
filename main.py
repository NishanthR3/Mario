import os
import sys
import collision_x
import collision_y
from colorama import Fore
from board import *
from objects import *
from people import *
from tortise import *
from player import *
from enemy import *
from input import Get, input_to
from config import *


class Engine(object):
    """class for engine."""

    def __init__(self):
        self.lives = 3
        self.time = 0
        self.level = 1
        self.done = False
        self.characters = Foreground_Configaration()

    def __intialize(self):
        self.getch = Get()
        self.win = Window()
        self.x_collisions = collision_x.Collision_horizontal()
        self.y_collisions = collision_y.Collision_vertical()
        self.boxes1 = []
        self.boxes2 = []
        self.pipes = []
        self.set_tort = []
        self.coins = []
        for brick in self.characters.boxes1:
            self.boxes1.append(Box(*brick, self.win))
        for brick in self.characters.boxes2:
            if len(self.boxes2) != 1:
                self.boxes2.append(Box(*brick, self.win))
            else:
                self.boxes2.append(Spring(*brick, self.win))
        self.boxes = [self.boxes1, self.boxes2]
        for pipe in self.characters.pipes:
            self.pipes.append(Pipe(pipe, self.win))
        for tort in self.characters.tortise:
            self.set_tort.append(Tort(*tort, self.win))
        for coins in self.characters.coins:
            self.coins.append(Coins(*coins, self.win))
        self.mario = Mario_reddy((*self.characters.mario), self.win)
        os.system("aplay -q smb_new.wav &")
        os.system("clear")
        self.win.update_frame(self.mario, self.lives,  0, 1)

    def __restart(self):
        os.system("aplay -q smb_die.wav &")
        self.lives -= 1
        self.level = 1
        self.time = 0
        self.__intialize()
        self.__level_one_run()

    def __game_updates(self):
        if self.lives == 0:
            os.system('clear')
            print()
            sys.exit()
        if self.mario.health == 0:
            self.__restart()
        self.time += 0.3
        if self.time <= 20 and self.done:
            self.mario.score += 200
        self.mario.score = self.mario.score + (20 - self.time)

    def __level_update(self):
        if self.mario.x >= 124:
            self.level = 2
            self.Goblin = Enemy(220, 27, self.win)
            self.__level_two_run()

    def __frame_updates(self, goblin=None):
        os.system('clear')
        if goblin is None:
            self.win.update_frame(
                self.mario, self.lives,
                round(self.time), self.level)
        else:
            self.win.update_frame(
                self.mario, self.lives,
                round(self.time), self.level, goblin)

    def __ground_move(self, input, bool_value_1, bool_value_2):
        if input == 'a' and not(bool_value_1):
            os.system("aplay -q smb_touch.wav &")
            self.mario.move(-1, self.win, self.level)
        elif input == 'd' and not(bool_value_2):
            os.system("clear")
            os.system("aplay -q smb_touch.wav &")
            self.mario.move(1, self.win, self.level)
        elif input == 'q':
            os.system('clear')
            sys.exit()

    def __jump_move(self, input, bool_value_1, bool_value_2):
        if not(self.mario.isJump):
            if input == 'w' and not(bool_value_1):
                os.system("aplay -q smb_jump.wav &")
                self.mario.jump_init()
            elif input == 'w' and bool_value_1:
                self.mario.remove_person(self.win)
                self.mario.y = 19
        else:
            self.mario.jump(self.win)
            if bool_value_2:
                for single_pipe in self.pipes:
                    self.y_collisions.pipe(
                        self.mario, single_pipe, self.win)
                for brick in self.boxes:
                    self.y_collisions.brick(self.mario, brick[0], self.win)

    def __goDown_move(self, input, bool_value):
        if self.mario.goDown:
            self.mario.fall_down(self.win)
            if bool_value:
                for single_pipe in self.pipes:
                    self.y_collisions.pipe(
                        self.mario, single_pipe, self.win)
                for brick in self.boxes:
                    self.y_collisions.brick(self.mario, brick[0], self.win)

    def __collision_check(self):
        self.mario.hit = self.y_collisions.check_hit(
            self.mario, self.boxes)
        self.y_collisions.tort(self.mario, self.set_tort, self.win)
        self.x_collisions.tort(
            self.mario, self.set_tort, self.win)
        self.x_collisions.coin(self.mario, self.coins, self.win)
        self.y_collisions.check_ground(
            self.mario, self.pipes, self.boxes)

    def __final_fight(self):
        self.x_collisions.goblin(
            self.mario, self.Goblin, self.win)
        if not(self.Goblin.freeze):
            self.y_collisions.goblin(
                self.mario, self.Goblin, self.win)
        else:
            self.Goblin.freeze = False
        self.Goblin.power_activater += 1
        self.Goblin.power_activater = self.Goblin.power_activater % 8
        if self.Goblin.power_activater == 2:
            if self.mario.y == 27:
                self.mario.health -= 1

    def __level_two_run(self):
        while self.lives > 0:
            input = input_to(self.getch)
            self.__game_updates()
            if not(self.done):
                self.__final_fight()
            if self.done:
                print(self.mario.x)
            if self.done and self.mario.x >= 227:
                os.system('aplay -q smb_world_clear.wav &')
                os.system('clear')
                print("You Won")
                print("SCORE : " + str(round(self.mario.score)))
                sys.exit()
            if not(self.done):
                if self.Goblin.health <= 0:
                    self.mario.score += 200
                    self.Goblin.remove_person(self.win)
                    self.done = True
                    del self.Goblin
            if not(self.done):
                self.Goblin.attack(self.mario, self.win)
            self.__ground_move(input, False, False)
            self.__jump_move(input, False, False)
            self.y_collisions.check_ground(
                self.mario, self.pipes, self.boxes)
            self.__goDown_move(input, False)
            if not(self.done):
                self.__frame_updates(self.Goblin)
            else:
                self.__frame_updates()

    def __level_one_run(self):
        while self.lives > 0:
            input = input_to(self.getch)
            self.__game_updates()
            self.__level_update()
            if(self.y_collisions.check_hole(self.mario, self.win)):
                self.__restart()
            for self.tortise in self.set_tort:
                self.tortise.gaurd(self.win)
            self.__ground_move(input,
                               self.x_collisions.check(-1, self.mario,
                                                       self.pipes, self.boxes),
                               self.x_collisions.check(1, self.mario,
                                                       self.pipes, self.boxes))
            if self.mario.onSpring:
                self.y_collisions.restore(
                    self.mario, self.win, self.boxes2[1])
            if not(self.mario.onSpring):
                self.__jump_move(input, self.mario.hit, True)
                self.__collision_check()
                self.__goDown_move(input, True)
                self.y_collisions.check_spring(
                    self.mario, self.win, self.boxes2[1])
            self.__frame_updates()

    def run_game(self):
        self.__intialize()
        self.__level_one_run()
        os.system('aplay -q smb_gameover.wav &')
        os.system('clear')
        print("You Lost")
        sys.exit()


game = Engine()
game.run_game()
