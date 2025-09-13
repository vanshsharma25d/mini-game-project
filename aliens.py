import pygame
from pygame.sprite import Sprite

class Alien(Sprite):



    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load(r'C://Users//anubhav//OneDrive//Desktop//python//alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.direction_y = 1  





    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        self.y += self.settings.alien_bounce_speed * self.direction_y
        self.rect.y = self.y
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            self.direction_y = -1 
        elif self.rect.top <= 0:
            self.direction_y = 1 




    def check_edge(self):
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0
