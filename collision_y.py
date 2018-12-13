class Collision_vertical(object):
    """Class to check x-axis collisions."""

    def __init__(self):
        pass

    def check_hit(self, mario, boxes):
        ans = False
        for brick in boxes:
            if mario.x + 2 >= brick[0].x and mario.x <= brick[0].x + 9 and \
                    mario.y > brick[0].y:
                ans = True
        return ans

    def pipe(self, mario, single_pipe, win):
        if mario.x + 2 >= single_pipe.x and mario.x <= single_pipe.x + 5 and \
                mario.y + (mario.jumpCount ** 2) > single_pipe.h - 2:
            mario.remove_person(win)
            mario.y = single_pipe.h - 2
            mario.jumpCount = 3
            mario.isJump = False
            mario.goDown = False
            mario.fall = 1
            mario.create_person(win)

    def brick(self, mario, brick, win):
        if mario.x + 2 >= brick.x and mario.x <= brick.x + 9 and mario.y + \
                (mario.jumpCount ** 2) > brick.y - 1 and mario.y < brick.y + 2:
            mario.remove_person(win)
            mario.y = brick.y - 1
            mario.jumpCount = 3
            mario.isJump = False
            mario.goDown = False
            mario.fall = 1
            mario.create_person(win)

    def check_on_pipes(self, mario, pipes):
        ans = False
        for single_pipe in pipes:
            if mario.x + 2 >= single_pipe.x and mario.x <= single_pipe.x + 5:
                ans = True
        return ans

    def fall_pipe(self, mario, pipes, win):
        if mario.climb_pipe and not(self.check_on_pipes(mario, pipes)):
            mario.fall_down(win)

    def check_ground(self, mario, pipes, boxes):
        if not(mario.isJump) and not(mario.goDown):
            for single_pipe in pipes:
                if (mario.x + 2 < single_pipe.x or
                    mario.x > single_pipe.x + 5) \
                        and mario.y < 27:
                    mario.goDown = True
                    mario.fall_down_start()

    def tort(self, mario, set_tort, win):
        for tortise in set_tort:
            if mario.x + 2 >= tortise.x + tortise.face * tortise.vel and \
                    mario.x <= tortise.x + tortise.face * tortise.vel + 2 and \
                    ((mario.neg == -1 and mario.isJump) or mario.goDown) and \
                    mario.y + mario.jumpCount ** 2 >= 27:
                mario.score += 100
                set_tort.pop(set_tort.index(tortise))
                tortise.remove_person(win)

    def goblin(self, mario, Goblin, win):
        if mario.x + 2 >= Goblin.x + Goblin.dir * Goblin.vel and \
                mario.x <= Goblin.x + Goblin.dir * Goblin.vel + 2 and \
                ((mario.neg == -1 and mario.isJump) or mario.goDown) and \
                mario.y + mario.jumpCount ** 2 >= 27:
            Goblin.health -= 1
            Goblin.freeze = True
            Goblin.remove_person(win)
            Goblin.x += 1
            Goblin.create_person(win)

    def check_hole(self, mario, win):
        if mario.x >= 112 and mario.x <= 120 and mario.y == 27:
            mario.y += 1
            return True
        return False

    def check_spring(self, mario, win, spring):
        if mario.x == spring.x and mario.y + 1 == spring.y:
            spring.remove_box(win)
            mario.remove_person(win)
            spring.y += 1
            mario.y += 1
            mario.onSpring = True
            spring.create_box(win)

    def restore(self, mario, win, spring):
        spring.remove_box(win)
        mario.remove_person(win)
        spring.y -= 1
        mario.y -= 1
        mario.onSpring = False
        spring.create_box(win)

    def on_ground_hit(self, mario):
        if mario.y == 27:
            mario.health -= 1
