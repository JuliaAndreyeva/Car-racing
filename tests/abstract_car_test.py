import sys
import os
import pytest
import pygame
from abstract_car import AbstractCar
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))


class TestAbstractCar:
    @pytest.fixture
    def car(self):
        # Початкові дані для тестів
        max_vel = 10
        rotation_vel = 5
        start_pos = (100, 100)
        acceleration = 1
        CAR = pygame.image.load("imgs/car2.png")
        return AbstractCar(max_vel, rotation_vel, start_pos, acceleration, CAR)

    def test_rotate_left(self, car):
        car.rotate(left=True)
        assert car.angle == 5

    def test_rotate_right(self, car):
        car.rotate(right=True)
        assert car.angle == -5

    @pytest.mark.parametrize("initial_vel,expected_vel", [(0, 1), (5, 6), (-3, -2)])
    def test_move_forward(self, car, initial_vel, expected_vel):
        car.vel = initial_vel
        car.move_forward()
        assert car.vel == expected_vel

    # Додамо параметризацію для тесту методу move_backward
    @pytest.mark.parametrize("initial_vel,expected_vel", [(0, -1), (5, 4), (-3, -4)])
    def test_move_backward(self, car, initial_vel, expected_vel):
        car.vel = initial_vel
        car.move_backward()
        assert car.vel == expected_vel

    def test_reduce_speed(self, car):
        car.vel = 5
        car.reduce_speed()
        assert car.vel == 4.5

    @pytest.mark.xfail(reason="Expected to fail")
    def test_collide(self, car):
        # Створення маски
        mask = pygame.mask.from_surface(pygame.Surface((50, 50)))
        poi = car.collide(mask, x=50, y=50)
        assert poi == (50, 50)

    def test_reset(self, car):
        car.x = 200
        car.y = 200
        car.angle = 90
        car.vel = 5
        car.reset()
        assert car.x == 100
        assert car.y == 100
        assert car.angle == 0
        assert car.vel == 0
