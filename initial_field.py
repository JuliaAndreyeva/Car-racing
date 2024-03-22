import pygame


class InitialField():
    def __init__(self, grass, track, track_border, finish, finish_position, car_position, path):
        self.grass = grass
        self.track = track
        self.track_border = track_border
        self.track_border_mask = pygame.mask.from_surface(track_border)
        self.finish = finish
        self.finish_mask = pygame.mask.from_surface(finish)
        self.finish_position = finish_position
        self.width = track.get_width()
        self.height = track.get_height()
        self.car_position = car_position
        self.path = path
