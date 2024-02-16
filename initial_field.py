import pygame

class InitialField():
    def __init__(self, GRASS, TRACK, TRACK_BORDER, FINISH, FINISH_POSITION):
        self.grass = GRASS
        self.track = TRACK
        self.track_border = TRACK_BORDER
        self.track_border_mask = pygame.mask.from_surface(TRACK_BORDER)
        self.finish = FINISH
        self.finish_mask = pygame.mask.from_surface(FINISH)
        self.finish_position = FINISH_POSITION
        self.width = TRACK.get_width()
        self.height = TRACK.get_height()
