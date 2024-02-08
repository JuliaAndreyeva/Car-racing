from abc import ABC
import pygame
import math
from main import CAR


class AbstractCar(ABC):
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

        def rotate(self, left=False, right=False):
            if left:
                self.angle += self.rotation_vel
            elif right:
                self.angle -= self.rotation_vel

        def move_forward(self):
            self.vel = min(self.vel + self.accelaration, self.max_vel)
            self.move()

        def move(self):
           radians = math.radians(self.angle)
           vertical = math.cos(radians) * self.vel
           horizontal = math.sin(radians) * self.vel

           self.y -= vertical
           self.x -= horizontal

        def reduce_speed(self):
            self.vel = max(self.vel - self.acceleration / 2, 0)
            self.move()

class PlayerCar(AbstractCar):
    IMG = CAR
    START_POS = (180, 200)