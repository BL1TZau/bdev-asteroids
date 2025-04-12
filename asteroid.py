from circleshape import *

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, 'red', self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)   # both from parent circleshape
        
    def split(self):
        self.kill()