import pygame
from utils import scale_image

GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("imgs/grass.jpg"), 0.9)
TRACK_BORDER = scale_image(pygame.image.load("imgs/grass.jpg"), 0.9)
CAR = scale_image(pygame.image.load("imgs/grass.jpg"), 0.5)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CAR RACING!")

FPS = 60

run = True
clock = pygame.time.Clock()
images = [(GRASS(0, 0)), (TRACK(0, 0))]


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    moved = False

pygame.quit()

