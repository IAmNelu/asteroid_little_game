import pygame
from utils import load_sprite


class RockDestryer:

    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", type="jpg", with_alpha=False)

    def main_loop(self):

        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Rock Destroyer")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
                                             event.key == pygame.K_ESCAPE):
                quit()

    def _process_game_logic(self):
        pass

    def _draw(self):
        # self.screen.fill((0, 0, 255))
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
