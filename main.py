import sys
import pygame
from player import Player
from obstacle import Rock


class Game:
    def __init__(self):
        player_sprite = Player((screen_width / 2, screen_height - 5), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.obstacles = pygame.sprite.Group()
        self.obstacle_amount = 3
        self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(screen_width / 6, 450, *self.obstacle_x_positions)

    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.obstacles.draw(screen)

    def create_multiple_obstacles(self, x_start, y_start, *offset):
        for offset_x in offset:
            new_obstacle = Rock((x_start + offset_x,
                                 y_start))
            self.obstacles.add(new_obstacle)


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        game.run()

        pygame.display.flip()
        clock.tick(60)
