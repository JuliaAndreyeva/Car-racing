import pygame
import pytest
from utils import scale_image, blit_rotate_center, blit_text_center
from unittest.mock import patch, MagicMock


@pytest.fixture
def sample_image():
    # Створення зображення для тестування
    return pygame.Surface((100, 100))  # Створюємо поверхню розміром 100x100 як зразок


def test_scale_image(sample_image):
    # Тест масштабування зображення
    scaled_image = scale_image(sample_image, 0.5)  # Масштабуємо зображення до половини розміру

    # Перевірка розмірів масштабованого зображення
    assert scaled_image.get_width() == 50
    assert scaled_image.get_height() == 50


@pytest.fixture
def window():
    return pygame.display.set_mode((800, 600))


def test_blit_rotate_center(window):
    test_image = pygame.Surface((50, 50))
    test_image.fill((255, 255, 255))
    top_left = (100, 100)
    angle = 45
    blit_rotate_center(window, test_image, top_left, angle)
    color_at_top_left = window.get_at(top_left)
    assert color_at_top_left != (0, 0, 0, 255)


@pytest.fixture
def mock_surface():
    return MagicMock()


@pytest.fixture
def mock_font():
    return MagicMock()


def test_blit_text_center(mock_surface, mock_font):
    text = "Test Text"
    blit_text_center(mock_surface, mock_font, text)
    mock_font.render.assert_called_once_with(text, 1, (200, 200, 200))
    expected_pos = (
        mock_surface.get_width() / 2 - mock_font.render().get_width() / 2,
        mock_surface.get_height() / 2 - mock_font.render().get_height() / 2
    )
    mock_surface.blit.assert_called_once_with(mock_font.render(), expected_pos)
