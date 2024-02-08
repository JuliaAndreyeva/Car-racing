import pygame
from utils import scale_image
from abstract_car import PlayerCar

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
player_car = PlayerCar(4, 4)

while run:
    clock.tick(FPS)

    #add function draw

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()

    if not moved:
        player_car.reduce_speed()

pygame.quit()

