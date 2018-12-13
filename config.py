class Background_Configaration(object):
    """docstring for Configaration."""

    def __init__(self):
        self.mountains = [21, 120, 190]
        self.bushes = [9, 34, 54, 105, 140, 210]
        self.clouds = [(21, 3), (81, 5), (121, 5), (167, 3), (201, 5)]


class Foreground_Configaration(object):
    """docstring for Foreground_Configaration."""

    def __init__(self):
        self.boxes1 = [(32, 16), (35, 16), (38, 16)]
        self.boxes2 = [(76, 16), (79, 16), (82, 16)]
        self.pipes = [56, 100]
        self.tortise = [(21, 27, 1, 1, 19, 53), (97, 27, 2, -1, 62, 97)]
        self.coins = [(32, 14), (36, 14), (40, 14), (23, 26), (27, 26),
                      (31, 26), (76, 26), (80, 26), (84, 26), (57, 20),
                      (60, 20)]
        self.mario = (10, 27)
