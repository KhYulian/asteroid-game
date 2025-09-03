import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y ,radius)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, ASTEROID_MIN_RADIUS)
        
    def update(self, dt): 
        self.position += self.velocity * dt