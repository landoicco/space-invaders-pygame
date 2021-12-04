import sys
import pygame
from player import Player
from obstacle import Rock
from enemy import Ufo, Alien
from random import choice, randint
from laser import Laser


class Game:
    def __init__(self):
        player_sprite = Player((screen_width / 2, screen_height - 5), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Obstacles setup
        self.obstacles = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(screen_width / 8, 650, *self.obstacle_x_positions)

        # Ufo setup
        self.ufos = pygame.sprite.Group()
        self.ufos_setup(3, 5, x_offset=50, y_offset=130)
        self.ufo_x_speed = 1
        self.ufo_lasers = pygame.sprite.Group()

        # Extra alien setup
        self.alien = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(40, 80)

    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)

        self.extra_alien_timer()

        self.ufos.update(self.ufo_x_speed)
        self.ufo_position_checker()
        self.ufos.draw(screen)
        self.ufo_lasers.update()
        self.ufo_lasers.draw(screen)

        self.obstacles.draw(screen)
        self.alien.draw(screen)
        self.alien.update()

    def create_multiple_obstacles(self, x_start, y_start, *offset):
        for offset_x in offset:
            new_obstacle = Rock((x_start + offset_x,
                                 y_start))
            self.obstacles.add(new_obstacle)

    def ufo_position_checker(self):
        all_ufos = self.ufos.sprites()
        for ufo in all_ufos:
            if ufo.rect.left <= 0 or ufo.rect.right >= screen_width:
                # Invert direction of ufo's
                self.ufo_x_speed *= -1
                self.ufo_move_down(3)

    def ufo_move_down(self, distance):
        if self.ufos:
            all_ufos = self.ufos.sprites()
            for ufo in all_ufos:
                ufo.rect.y += distance

    def ufo_shoot(self):
        if self.ufos.sprites():
            random_ufo = choice(self.ufos.sprites())
            laser_sprite = Laser(random_ufo.rect.center, 6, screen_height)
            self.ufo_lasers.add(laser_sprite)

    def ufos_setup(self, rows, cols, x_distance=120, y_distance=120, x_offset=120, y_offset=50):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                if row_index == 0:
                    ufo_sprite = Ufo('yellow', x, y)
                elif 1 <= row_index < 2:
                    ufo_sprite = Ufo('green', x, y)
                else:
                    ufo_sprite = Ufo('red', x, y)
                self.ufos.add(ufo_sprite)

    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.alien.add(Alien(choice(['right', 'left']), screen_width, 15))
            self.extra_spawn_time = randint(400, 800)


if __name__ == '__main__':
    pygame.init()
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    UFO_LASER = pygame.USEREVENT + 1
    pygame.time.set_timer(UFO_LASER, 800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == UFO_LASER:
                game.ufo_shoot()

        screen.fill((0, 0, 0))
        game.run()

        pygame.display.flip()
        clock.tick(60)
