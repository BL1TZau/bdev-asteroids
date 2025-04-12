from circleshape import *
# from random import uniform
import random
from constants import *

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, 'red', self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)   # both from parent circleshape
        
    def split(self):
        self.kill() # removes asteroid from group
        if self.radius <= ASTEROID_MIN_RADIUS: return   # end if smallest asteroid
        angle = random.uniform(20, 50)  # generate rand between 20 - 50
        first_split = self.velocity.rotate(angle)   # create new vec, rotate rand ang
        second_split = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS  # large > med > small
        first_ast = Asteroid(self.position.x, self.position.y, new_radius)  # create first split
        first_ast.velocity += (first_split * 1.6)   # accelerate the splits
        second_ast = Asteroid(self.position.x, self.position.y, new_radius)
        second_ast.velocity += (second_split * 1.6)
        