import pygame
import unittest
from initial_field import InitialField

class TestInitialField(unittest.TestCase):
    def setUp(self):
        # Підготовка змінних для тесту
        grass_surface = pygame.Surface((100, 100))
        track_surface = pygame.Surface((200, 200))
        track_border_surface = pygame.Surface((200, 200))
        finish_surface = pygame.Surface((50, 50))
        finish_position = (25, 25)
        car_position = (50, 50)
        path = [(10, 10), (20, 20), (30, 30)]

        # Створення об'єкту InitialField для тестування
        self.initial_field = InitialField(grass_surface, track_surface, track_border_surface, finish_surface, finish_position, car_position, path)

    def test_initialization(self):
        # Перевірка правильності ініціалізації атрибутів
        self.assertEqual(self.initial_field.grass.get_size(), (100, 100))
        self.assertEqual(self.initial_field.track.get_size(), (200, 200))
        self.assertEqual(self.initial_field.track_border.get_size(), (200, 200))
        self.assertEqual(self.initial_field.finish.get_size(), (50, 50))
        self.assertEqual(self.initial_field.finish_position, (25, 25))
        self.assertEqual(self.initial_field.car_position, (50, 50))
        self.assertEqual(self.initial_field.path, [(10, 10), (20, 20), (30, 30)])