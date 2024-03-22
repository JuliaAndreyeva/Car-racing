import sys
import os
import pytest
import pygame

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from computer_car import ComputerCar


class TestComputerCar:

    @pytest.fixture
    def computer_car(self):
        # Початкові дані для тестів
        max_vel = 10
        rotation_vel = 5
        start_pos = (100, 100)
        acceleration = 1
        path = [(150, 150), (200, 200), (250, 250)]  # Припустимо, що це ваш шлях
        return ComputerCar(max_vel, rotation_vel, path, start_pos, acceleration)

    def test_draw_points(self, computer_car):
        # Створюємо віртуальне вікно для тестування малювання
        win = pygame.Surface((500, 500))
        # Викликаємо метод малювання точок
        computer_car.draw_points(win)
        # Перевіряємо, що в кожній точці було намальовано червоне коло радіусом 7
        for point in computer_car.path:
            assert win.get_at(point) == (255, 0, 0, 255)

    def test_update_path_point(self, computer_car):
        # Перевірка коректності оновлення поточної точки шляху
        computer_car.x = 150
        computer_car.y = 150
        computer_car.img = pygame.Surface((20, 20))
        computer_car.update_path_point()
        # Очікуємо, що поточна точка шляху буде оновлена після зіткнення з точкою (150, 150)
        assert computer_car.current_point == 1

    def test_next_level(self, computer_car):
        # Перевірка зміни рівня у комп'ютерної машини
        computer_car.vel = 5
        computer_car.next_level(2)
        # Очікуємо, що після переходу на наступний рівень швидкість збільшиться на 0.2
        assert computer_car.vel == 10.2
        # Перевіряємо, що поточна точка повернеться на початкову
        assert computer_car.current_point == 0

    def test_first_level(self, computer_car):
        # Перевірка переходу до першого рівня у комп'ютерної машини
        computer_car.vel = 7
        computer_car.current_point = 2
        computer_car.first_level()
        # Очікуємо, що після переходу на перший рівень швидкість повернеться до початкового значення
        assert computer_car.vel == 10
        assert computer_car.current_point == 0

    def test_calculate_angle(self, computer_car):
        computer_car.x = 100
        computer_car.y = 100
        computer_car.angle = 90
        computer_car.current_point = 1
        computer_car.calculate_angle()
        expected_angle = 95
        assert computer_car.angle == expected_angle
