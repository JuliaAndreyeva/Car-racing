# from pygame import *
from utils import *
# from abstract_car import *
from computer_car import *
from initial_field import InitialField
import argparse
from game_info import *
from pygame import mixer
pygame.font.init()
MAIN_FONT = pygame.font.SysFont("comicsans", 44)

parser = argparse.ArgumentParser(description="Choose your settings")
parser.add_argument("-m", "--map", choices=['map1', 'map2'], help="Choose your map", type=str)
parser.add_argument("-a", "--acceleration", choices=['easy', 'medium', 'hard'],
                    help="Choose your acceleration", type=str)
args = parser.parse_args()

mixer.init()
mixer.music.load("music/Dua Lipa - Levitating.mp3")
mixer.music.play()
mixer.music.set_volume(0.03)


def parse_setting(args):
    try:
        if args.map == 'map1':
            track = scale_image(pygame.image.load("imgs/track.png"), 0.9)
            track_border = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
            finish_position = (130, 250)
            finish = pygame.image.load("imgs/finish.png")
            car_position = (180, 200)
            grass = scale_image(pygame.image.load("imgs/grass2.jpg"), 2.5)
            path1 = [(167, 109), (67, 105), (57, 193), (57, 294), (57, 376), (61, 466), (108, 535), (172, 590),
                     (217, 642), (272, 694), (350, 726), (407, 607), (412, 528), (491, 488), (562, 493), (595, 560),
                     (606, 644), (605, 706), (724, 726), (738, 608), (744, 492), (732, 401), (689, 367), (583, 369),
                     (457, 366), (419, 359), (418, 264), (484, 261), (574, 267), (606, 254), (694, 260), (733, 128),
                     (644, 72), (536, 53), (413, 65), (301, 82), (276, 201), (285, 287), (278, 378), (191, 397),
                     (176, 305), (173, 259)]

            initial_field_ = InitialField(grass, track, track_border, finish, finish_position, car_position, path1)
        elif args.map == 'map2':
            track2 = scale_image(pygame.image.load("imgs/track2-2.png"), 1.4)
            track_border2 = scale_image(pygame.image.load("imgs/track-border2-2.png"), 1.4)
            finish2 = scale_image(pygame.image.load("imgs/finish.png"), 0.6)
            finish_position2 = (856, 400)
            car_position2 = (860, 360)
            grass = scale_image(pygame.image.load("imgs/grass2.jpg"), 2.5)
            path2 = [(853, 303), (756, 280), (648, 275), (575, 268), (495, 204), (429, 144), (322, 113), (231, 101),
                     (140, 110), (97, 138), (81, 211), (114, 254), (200, 277), (300, 273), (366, 281), (415, 332),
                     (462, 378), (521, 424), (553, 495), (506, 549), (403, 525), (327, 531), (234, 525), (194, 472),
                     (151, 437), (97, 453), (76, 509), (100, 571), (127, 622), (152, 656), (287, 659), (396, 656),
                     (491, 663), (577, 666), (640, 630), (695, 537), (775, 496), (853, 468), (886, 407)]

            initial_field_ = InitialField(grass, track2, track_border2, finish2, finish_position2, car_position2, path2)
        else:
            raise ValueError("Invalid map value: {}".format(args.map))
    except ValueError as e:
        print("Error:", e)
    return initial_field_


field = parse_setting(args)
pygame.font.init()
pygame.init()


WIN = pygame.display.set_mode((field.width, field.height))
pygame.display.set_caption("CAR RACING!")

FPS = 60
# MAIN_FONT = pygame.font.SysFont("comicsans", 44)


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


def handle_collision(player_car, computer_car, game_info):
    if player_car.collide(field.track_border_mask) != None:
        player_car.bounce()

    computer_finish_poi_collide = computer_car.collide(
        field.finish_mask, *field.finish_position)
    if computer_finish_poi_collide != None:
        blit_text_center(WIN, MAIN_FONT, "You lost!")
        pygame.display.update()
        pygame.time.wait(5000)
        game_info.reset()
        player_car.reset()
        # computer_car.reset()
        computer_car.first_level()
        # computer_car.current_point = 0

    player_finish_poi_collide = player_car.collide(field.finish_mask, *field.finish_position)
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            game_info.next_level()
            player_car.reset()
            computer_car.next_level(game_info.level)


run = True
clock = pygame.time.Clock()
images = [(field.grass, (0, 0)), (field.track, (0, 0)),
          (field.finish, field.finish_position), (field.track_border, (0, 0))]

player_car = PlayerCar(4, 4, field.car_position, 0.1)
computer_car = ComputerCar(1.3, 4, field.path, field.car_position, 0.5)
game_info = GameInfo()

# player_car = PlayerCar(4, 4, (860, 450))
# computer_car = ComputerCar(4, 4, PATH1, (860, 450))

# player_car = PlayerCar(4, 4, (890, 450))
# computer_car = ComputerCar(4, 4, PATH1, (860, 450))

# player_car = PlayerCar(4, 4, (890, 360))
# computer_car = ComputerCar(4, 4, PATH1, (860, 360))

while run:
    clock.tick(FPS)

    draw(WIN, images, player_car, computer_car, field, game_info)

    while not game_info.started:
        blit_text_center(
            WIN, MAIN_FONT, f"Press any key to start level {game_info.level}!")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == pygame.KEYDOWN:
                game_info.start_level()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    move_player(player_car)
    computer_car.move()

    handle_collision(player_car, computer_car, game_info)

    if game_info.game_finished():
        blit_text_center(WIN, MAIN_FONT, "You won the game!")
        pygame.time.wait(5000)
        game_info.reset()
        player_car.reset()
        computer_car.reset()


# print(computer_car.path)
pygame.quit()
