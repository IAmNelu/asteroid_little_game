import pygame
from utils import load_sprite, get_random_position
from models import Spaceship, Asteroid

import os

clear = lambda: os.system('cls')


MIN_ASTEROID_DISTANCE = 250
class RockDestryer:
  def __init__(self):
    self._init_pygame()
    self.screen = pygame.display.set_mode((800, 600))
    self.background = load_sprite("space", type="jpg", with_alpha=False)
    self.clock = pygame.time.Clock()
    
    self.asteroids = []
    self.bullets = []
    self.spaceship = Spaceship((400, 300), self.bullets.append)  
    
    for _ in range(6):
      while True:
        position = get_random_position(self.screen)
        if (position.distance_to(self.spaceship.position) > MIN_ASTEROID_DISTANCE):
          break
      self.asteroids.append(Asteroid(position))

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
      elif (self.spaceship and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
        self.spaceship.shoot()
    is_key_pressed = pygame.key.get_pressed()
    if self.spaceship:
      if is_key_pressed[pygame.K_RIGHT]:
        self.spaceship.rotate(clockwise=True)
      elif is_key_pressed[pygame.K_LEFT]:
        self.spaceship.rotate(clockwise=False)
      if is_key_pressed[pygame.K_UP]:
        self.spaceship.accelerate()
      

  def _process_game_logic(self):
    for game_object in self._get_game_objects():
      game_object.move(self.screen)
    
    if self.spaceship:
      for asteroid in self.asteroids:
        if asteroid.collides_with(self.spaceship):
          self.spaceship = None
          break
    
    for bullet in self.bullets[:]:
      for asteroid in self.asteroids[:]:
        if asteroid.collides_with(bullet):
          self.asteroids.remove(asteroid)
          self.bullets.remove(bullet)
          break
          
    for bullet in self.bullets[:]:
      if not self.screen.get_rect().collidepoint(bullet.position):
        self.bullets.remove(bullet)

  def _draw(self):
    # self.screen.fill((0, 0, 255))
    self.screen.blit(self.background, (0, 0))
    for game_object in self._get_game_objects():
      game_object.draw(self.screen)

    pygame.display.flip()
    self.clock.tick(60)

  def _get_game_objects(self):
    game_objs = [*self.bullets, *self.asteroids]
    if self.spaceship:
      game_objs.append(self.spaceship)
    return game_objs