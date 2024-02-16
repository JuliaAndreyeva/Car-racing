# from pygame import *
from utils import *
# from abstract_car import *
from computer_car import *
from initial_field import InitialField
import argparse


parser = argparse.ArgumentParser(description="Choose your settings")
parser.add_argument("-m", "--map", choices=['map1', 'map2'], help="Choose your map", type=str)
parser.add_argument("-a", "--acceleration", choices=['easy', 'medium', 'hard'], help="Choose your acceleration", type=str)
args = parser.parse_args()


def parse_setting(args):
    try:
        if args.map == 'map1':
            track = scale_image(pygame.image.load("imgs/track.png"), 0.9)
            track_border = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
            finish_position = (130, 250)
            finish = pygame.image.load("imgs/finish.png")
            car_position = (180, 200)
            grass = scale_image(pygame.image.load("imgs/grass2.jpg"), 2.5)
            initial_field_ = InitialField(grass, track, track_border, finish, finish_position, car_position)
        elif args.map == 'map2':
            track2 = scale_image(pygame.image.load("imgs/track2-2.png"), 1.4)
            track_border2 = scale_image(pygame.image.load("imgs/track-border2-2.png"), 1.4)
            finish2 = scale_image(pygame.image.load("imgs/finish.png"), 0.6)
            finish_position2 = (856, 400)
            car_position2 = (860, 360)
            grass = scale_image(pygame.image.load("imgs/grass2.jpg"), 2.5)
            initial_field_ = InitialField(grass, track2, track_border2, finish2, finish_position2, car_position2)
        else:
            raise ValueError("Invalid map value: {}".format(args.map))
    except ValueError as e:
        print("Error:", e)
    return initial_field_




TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)
TRACK2 = scale_image(pygame.image.load("imgs/track2-2.png"), 1.4)
TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
TRACK_BORDER2 = scale_image(pygame.image.load("imgs/track-border2-2.png"), 1.4)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
TRACK_BORDER_MASK2 = pygame.mask.from_surface(TRACK_BORDER2)


#FINISH = pygame.image.load("imgs/finish.png")
FINISH = scale_image(pygame.image.load("imgs/finish.png"), 0.6)
FINISH_MASK = pygame.mask.from_surface(FINISH)
# FINISH_POSITION = (130, 250)
# FINISH_POSITION = (860, 500)
FINISH_POSITION = (856, 400)


CAR = scale_image(pygame.image.load("imgs/convertible.png"), 0.5)

field = parse_setting(args)
pygame.font.init()
pygame.init()


#TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)
#TRACK2 = scale_image(pygame.image.load("imgs/track2.png"), 1.4)
#TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
#TRACK_BORDER2 = scale_image(pygame.image.load("imgs/track-border2.png"), 1.4)
#TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
#TRACK_BORDER_MASK2 = pygame.mask.from_surface(TRACK_BORDER2)
#FINISH1 = pygame.image.load("imgs/finish.png")
#FINISH2 = scale_image(pygame.image.load("imgs/finish.png"), 0.6)
#FINISH_MASK = pygame.mask.from_surface(FINISH2)
#FINISH_POSITION = (130, 250)
#FINISH_POSITION = (860, 500)
#WIDTH, HEIGHT = TRACK2.get_width(), TRACK2.get_height()


WIN = pygame.display.set_mode((field.width, field.height))
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
    if player_car.collide(field.track_border_mask) != None:
        player_car.bounce()

    computer_finish_poi_collide = computer_car.collide(
        field.finish_mask, *field.finish_position)
    if computer_finish_poi_collide != None:
        player_car.reset()
        computer_car.reset()

    player_finish_poi_collide = player_car.collide(
        field.finish_mask, *field.finish_position)
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            player_car.reset()
            computer_car.reset()


run = True
clock = pygame.time.Clock()
images = [(field.grass, (0, 0)), (field.track, (0, 0)),
          (field.finish, field.finish_position), (field.track_border, (0, 0))]

player_car = PlayerCar(4, 4, field.car_position, 0.1)
computer_car = ComputerCar(4, 4, PATH1, field.car_position, 0.5)

#player_car = PlayerCar(4, 4, (860, 450))
#computer_car = ComputerCar(4, 4, PATH1, (860, 450))

# player_car = PlayerCar(4, 4, (890, 450))
# computer_car = ComputerCar(4, 4, PATH1, (860, 450))

# player_car = PlayerCar(4, 4, (890, 360))
# computer_car = ComputerCar(4, 4, PATH1, (860, 360))

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
