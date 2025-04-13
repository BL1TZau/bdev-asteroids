from circleshape import *
from constants import *
from random import randrange

class Shot(CircleShape):
    containers = ()
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        img = './data/ships/Main ship weapons/PNGs/single_bullet.png'
        self.image = pygame.image.load(img).convert_alpha()
        # Get the image's rect and place it at (x, y)
        # Positioning
        self.position = pygame.Vector2(x, y)
        self.rect = self.image.get_rect(center=(self.position))
        self.radius = self.image.get_width() / 2  # optional if still using radius elsewhere
        
    """def draw(self, screen):
        colour1 = randrange(0, 255)
        colour2 = randrange(0, 255)
        colour3 = randrange(0, 255)
        pygame.draw.circle(screen, (colour1, colour2, colour3), self.position, self.radius, 2)"""
    
    def update(self, dt):
        self.position += (self.velocity * dt)   # both from parent circleshape
        self.rect = self.image.get_rect(center=(self.position))

    # rotates player
    def rotate(self, player_facing):
        self.rotation = player_facing
        print(f'Bullet Rotation: {self.rotation}')
