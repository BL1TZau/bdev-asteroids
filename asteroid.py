from circleshape import *
# from random import uniform
import random
from constants import *

class Asteroid(CircleShape):
    containers = ()
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Load the image
        img = './data/backgrounds/Foozle_2DS0015_Void_EnvironmentPack/Asteroids/PNGs/Asteroid 01 - Base.png'
        self.image = pygame.image.load(img).convert_alpha()
        
        # position - create center
        self.position = pygame.Vector2(x, y)
        
        # scale sprite - rad*multi because PNG is square not circle
        self.image = pygame.transform.scale(self.image, ((self.radius * ASTEROID_SPRITE_SIZE_MULTIPLIER, 
                                                        self.radius * ASTEROID_SPRITE_SIZE_MULTIPLIER)))
        # set rect to center after scaling
        self.rect = self.image.get_rect(center=(self.position))
    
    def update(self, dt):
        self.position += (self.velocity * dt)   # both from parent circleshape
        self.rect.center = self.position    # drawing image
        
    def split(self):
        # kill to remove from group
        self.kill() # removes asteroid from group
        if self.radius <= (ASTEROID_MIN_RADIUS*HITBOX_MULTIPLIER): return   # end if smallest asteroid
        
        # split asteroid var creation
        angle = random.uniform(20, 50)  # generate rand between 20 - 50
        first_split = self.velocity.rotate(angle)   # create new vec, rotate rand ang
        second_split = self.velocity.rotate(-angle)
        # rad - (one step down in size)
        new_radius = (self.radius - (ASTEROID_MIN_RADIUS *HITBOX_MULTIPLIER)) # large > med > small
        
        # creating split asteroids
        first_ast = Asteroid(self.position.x, self.position.y, new_radius)  # create first split
        first_ast.velocity += (first_split * 1.6)   # accelerate the splits
        second_ast = Asteroid(self.position.x, self.position.y, new_radius)
        second_ast.velocity += (second_split * 1.6)
        