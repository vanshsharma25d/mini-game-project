import sys
import time
import pygame
import settings
import ship
from bullet import Bullet
import gamestats 
import aliens
import scoreboard
class Game:





    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)   
        screen_rect = self.screen.get_rect()
        screen_width = screen_rect.width
        screen_height = screen_rect.height
        self.settings = settings.Settings()
        self.settings.screen_width = screen_width
        self.settings.screen_height = screen_height
        self.bg_image = pygame.image.load(r"C:\Users\anubhav\OneDrive\Desktop\python\bg.jpg")
        self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))
        pygame.display.set_caption("AI Gameji")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 25)

        self.stats = gamestats.gamestats(self)
        self.ship = ship.Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.game_active = True
        self.scoreboard = scoreboard.Scoreboard(self)
        self.win = False
        self.max_level = 3






    def _ship_hit(self):
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        self.ship.center_ship()
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

        else:
            self.game_active = False
            print("Game Over")
    




    def _create_fleet(self):
        sample_alien = aliens.Alien(self)
        alien_width, alien_height = sample_alien.rect.size


        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_per_row = available_space_x // (2 * alien_width)

        available_space_y = self.settings.screen_height - ( 3 * alien_height) - self.ship.rect.height
        number_of_rows = available_space_y // (2 * alien_height)

        print(f"Creating fleet: {number_of_rows} rows, {number_aliens_per_row} per row")
        for row in range(number_of_rows):
            for alien_num in range(number_aliens_per_row):
                self._create_alien(alien_num, row)






    def _create_alien(self, alien_number, row_number):
        alien = aliens.Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)




    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            ("Ship hit!!!")
        self._check_alien_bottom()






    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break
                
   
   
   
   
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    




    def run_game(self):
        print("Game started")
        while True:
            self._check_events()
            self.ship.update()
            if self.game_active:
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)






    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)





    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()







    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False






    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    



    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
    



    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += 100 * len(aliens)
                self.scoreboard.prep_score()
        if not self.aliens and collisions:
            self.bullets.empty()
            if self.stats.level < self.max_level:
                self.stats.level += 1
                self.scoreboard.prep_level()
                self.settings.alien_speed *= 1.2
                self._create_fleet()
            else:
                self.game_active = False
                self.win = True
            




    def _check_alien_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                alien.direction_y = -1  




    def _update_screen(self):
        self.screen.blit(self.bg_image,(0,0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.scoreboard.show_score()
        self.show_lives()
        if not self.game_active:
            if self.stats.ships_left <= 0:
                self._show_message("GAME OVER")
            elif self.win:
                self._show_message("YOU WIN")
        pygame.display.flip()
        self.clock.tick(60)
    
    def _show_message(self, message):
        font = pygame.font.SysFont(None, 100)
        text_image = font.render(message, True, (255, 0, 0))
        text_rect = text_image.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(text_image, text_rect)

    def show_lives(self):
        lives_text = f"Lives: {self.stats.ships_left}"
        font = pygame.font.SysFont(None, 30)
        text = font.render(lives_text, True, (0, 255,0 ))
        self.screen.blit(text, (10,40))  

    def show_game_over(self):
        if not self.game_active:
            font = pygame.font.SysFont(None, 72)
            text = font.render("GAME OVER", True, (255, 0, 0))  # Red text
            text_rect = text.get_rect(center=self.screen.get_rect().center)
            self.screen.blit(text, text_rect)
    

    def show_win(self):
        if self.win:
            font = pygame.font.SysFont(None, 80)
            text = font.render("YOU WIN!", True, (0, 200, 0))  
            text_rect = text.get_rect(center=self.screen.get_rect().center)
            self.screen.blit(text, text_rect)



