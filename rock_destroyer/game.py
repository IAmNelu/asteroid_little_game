import pygame
from utils import load_sprite
from models import Spaceship
import os

clear = lambda: os.system('cls')


class RockDestryer:

  def __init__(self):
    self._init_pygame()
    self.screen = pygame.display.set_mode((800, 600))
    self.background = load_sprite("space", type="jpg", with_alpha=False)
    self.spaceship = Spaceship((400, 300))
    self.clock = pygame.time.Clock()

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
    
    is_key_pressed = pygame.key.get_pressed()
    
    if is_key_pressed[pygame.K_RIGHT]:
      self.spaceship.rotate(clockwise=True)
    elif is_key_pressed[pygame.K_LEFT]:
      self.spaceship.rotate(clockwise=False)
    if is_key_pressed[pygame.K_UP]:
      self.spaceship.accelerate()
      

  def _process_game_logic(self):
    self.spaceship.move(self.screen)

  def _draw(self):
    # self.screen.fill((0, 0, 255))
    self.screen.blit(self.background, (0, 0))
    self.spaceship.draw(self.screen)
    pygame.display.flip()
    self.clock.tick(60)
