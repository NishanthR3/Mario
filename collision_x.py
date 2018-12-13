import os


class Collision_horizontal(object):
    """Class to check x-axis collisions."""

    def __init__(self):
        pass

    def check(self, dir, mario, pipes, boxes):
        return (self.pipes(dir, mario, pipes) or self.boxes(dir, mario, boxes))

    def pipes(self, dir, mario, pipes):
        ans = False
        for single_pipe in pipes:
            ans = (ans or self.pipe(dir, mario, single_pipe))
        return ans

    def pipe(self, dir, mario, single_pipe):
        if dir == 1 and mario.x + 2 < single_pipe.x and \
                mario.x + 2 + mario.vel >= single_pipe.x and \
                mario.y > single_pipe.h:
            return True
        elif dir == -1 and mario.x > single_pipe.x + 5 and \
                mario.x - mario.vel <= single_pipe.x + 5 and \
                mario.y > single_pipe.h:
            return True
        else:
            return False

    def boxes(self, dir, mario, boxes):
        ans = False
        for brick in boxes:
            ans = (ans or self.brick(dir, mario, brick[0]))
        return ans

    def brick(self, dir, mario, brick):
        if dir == 1 and mario.x + 2 < brick.x and \
                mario.x + 2 + mario.vel >= brick.x and mario.y > brick.y and \
                mario.y < brick.y + 2:
            return True
        elif dir == -1 and mario.x > brick.x + 9 and \
                mario.x - mario.vel <= brick.x + 9 and mario.y > brick.y and \
                mario.y < brick.y + 2:
            return True
        else:
            return False

    def tort(self, mario, set_tort, win):
        for tortise in set_tort:
            if mario.x + 2 >= tortise.x and mario.x <= tortise.x + 2 and \
                    mario.y == 27:
                mario.health -= 1
                tortise.remove_person(win)
                tortise.create_person(win)

    def goblin(self, mario, Goblin, win):
        if mario.x + 2 >= Goblin.x and mario.x <= Goblin.x + 2 and \
                (mario.y == 27 or mario.y == 26):
            mario.health -= 1
            Goblin.remove_person(win)
            Goblin.create_person(win)

    def coin(self, mario, coins, win):
        for coin in coins:
            if mario.x + 2 >= coin.x and mario.x <= coin.x and \
                    (mario.y == coin.y or mario.y - 1 == coin.y):
                mario.score += 50
                os.system("aplay -q smb_coin.wav &")
                coins.pop(coins.index(coin))
                coin.remove_coin(win)
                del coin
