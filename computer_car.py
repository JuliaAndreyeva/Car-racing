from abstract_car import AbstractCar
from utils import scale_image
import pygame
import math

CAR = scale_image(pygame.image.load("imgs/car2.png"), 0.047)


class ComputerCar(AbstractCar):
    # IMG = CAR
    # START_POS = (150, 200)

    def __init__(self, img, max_vel, rotation_vel, path=[], start_pos=0, acceleration=0.1):
        super().__init__(max_vel, rotation_vel, start_pos, acceleration, img)
        self.path = path
        self.current_point = 0
        self.vel = max_vel
        # self.img = self.IMG
        self.img = self.img

    def draw_points(self, win):
        for point in self.path:
            pygame.draw.circle(win, (255, 0, 0), point, 7)

    def draw(self, win):
        super().draw(win)
        # self.draw_points(win)

    def calculate_angle(self):
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            desired_radian_angle = math.pi / 2
        else:
            desired_radian_angle = math.atan(x_diff / y_diff)

        if target_y > self.y:
            desired_radian_angle += math.pi

        difference_in_angle = self.angle - math.degrees(desired_radian_angle)
        if difference_in_angle >= 180:
            difference_in_angle -= 360

        if difference_in_angle > 0:
            self.angle -= min(self.rotation_vel, abs(difference_in_angle))
        else:
            self.angle += min(self.rotation_vel, abs(difference_in_angle))

    def update_path_point(self):
        target = self.path[self.current_point]
        rect = pygame.Rect(
            self.x, self.y, self.img.get_width(), self.img.get_height())
        if rect.collidepoint(*target):
            self.current_point += 1

    def move(self):
        if self.current_point >= len(self.path):
            return

        self.calculate_angle()
        self.update_path_point()
        super().move()

    def next_level(self, level):
        self.reset()
        self.vel = self.max_vel + (level - 1) * 0.2
        self.current_point = 0

    def first_level(self):
        self.reset()
        self.vel = self.max_vel
        self.current_point = 0
