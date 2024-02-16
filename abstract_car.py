from abc import ABC
import pygame
import math
from utils import blit_rotate_center, scale_image


CAR = scale_image(pygame.image.load("imgs/car1.png"), 0.04)


class AbstractCar(ABC):
    def __init__(self, max_vel, rotation_vel, start_pos, acceleration):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = start_pos
        self.start_position = start_pos
        self.acceleration = acceleration

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
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

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    def reset(self):
        self.x, self.y = self.start_position
        self.angle = 0
        self.vel = 0

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel / 2)
        self.move()


class PlayerCar(AbstractCar):
    IMG = CAR

    def __init__(self, max_vel, rotation_vel, start_pos, acceleration):
        super().__init__(max_vel, rotation_vel, start_pos, acceleration)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        #self.vel = -0.2 * self.vel
        self.vel = -self.vel
        self.move()
