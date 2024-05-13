import pygame
import random


class UserRoll:
    def init(self, rolls_needed):
        self.rolls = roll_num[0]
        self.rolls_needed = rolls_needed
        self.pity = self.rolls_needed - self.rolls

    def roll(self):
        ran_num = random.randint(1, self.pity)
        return ran_num
