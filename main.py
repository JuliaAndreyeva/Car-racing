import pygame
from utils import *
from abstract_car import *
from computer_car import *
pygame.font.init()

GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)

TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)
TRACK2 = scale_image(pygame.image.load("imgs/track2.png"), 1.4)
TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
TRACK_BORDER2 = scale_image(pygame.image.load("imgs/track-border2.png"), 1.4)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
TRACK_BORDER_MASK2 = pygame.mask.from_surface(TRACK_BORDER2)


#FINISH = pygame.image.load("imgs/finish.png")
FINISH = scale_image(pygame.image.load("imgs/finish.png"), 0.6)
FINISH_MASK = pygame.mask.from_surface(FINISH)
#FINISH_POSITION = (130, 250)
FINISH_POSITION = (860, 500)

CAR = scale_image(pygame.image.load("imgs/convertible.png"), 0.5)

WIDTH, HEIGHT = TRACK2.get_width(), TRACK2.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CAR RACING!")

FPS = 60
PATH1 = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
        (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]


MAIN_FONT = pygame.font.SysFont("comicsans", 44)


def move_player(player_car):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()

    if not moved:
        player_car.reduce_speed()


def handle_collision(player_car, computer_car):
    if player_car.collide(TRACK_BORDER_MASK2) != None:
        player_car.bounce()

    computer_finish_poi_collide = computer_car.collide(
        FINISH_MASK, *FINISH_POSITION)
    if computer_finish_poi_collide != None:
        player_car.reset()
        computer_car.reset()

    player_finish_poi_collide = player_car.collide(
        FINISH_MASK, *FINISH_POSITION)
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            player_car.reset()
            computer_car.reset()


run = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK2, (0, 0)),
          (FINISH, FINISH_POSITION), (TRACK_BORDER2, (0, 0))]

#player_car = PlayerCar(4, 4, (180, 200))
#computer_car = ComputerCar(4, 4, PATH1, (180, 200))

player_car = PlayerCar(4, 4, (900, 450))
computer_car = ComputerCar(4, 4, PATH1, (860, 450))

while run:
    clock.tick(FPS)

    draw(WIN, images, player_car, computer_car)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    move_player(player_car)
    computer_car.move()

    handle_collision(player_car, computer_car)


print(computer_car.path)
pygame.quit()
