import pygame
import time  

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

        
        self.time_created = time.time()  

    def update(self):
    
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        if time.time() - self.time_created >= self.settings.bullet_lifetime:
            self.kill()  

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
