from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    containers = ()
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)   #
        self.rotation = 0
        self.icd = 0    # init icd

        # Load the image
        self.image_link = './data/ships/main-ship/main-ship-bases/pngs/main_full.png'
        self.original_image = pygame.image.load(self.image_link).convert_alpha()
        self.original_image = pygame.transform.flip(self.original_image, False, True)
        self.image = self.original_image
        # Positioning
        self.position = pygame.Vector2(x, y)
        self.rect = self.image.get_rect(center=(self.position))
        self.radius = self.image.get_width() / 2  # optional if still using radius elsewhere
        


    """# defining triangle shape
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # triangle appearance
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 3)"""

    # rotates player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.image = pygame.transform.rotate(self.original_image, -self.rotation)
        self.rect = self.image.get_rect(center=self.position)

    def update(self, dt):
        self.icd -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        # Rotate the image
        # self.image = pygame.transform.rotate(self.image, -self.rotation)

        # Re-center the rect after rotating
        # self.rect = self.image.get_rect(center=self.position)

    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt  
        self.rect.center = self.position  
    
    def shoot(self):
        if self.icd <= 0:   # icd ready (allowed to shoot)
            self.icd = 0.15  # reset icd
            bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            bullet.velocity = pygame.Vector2(0, 1)
            bullet.velocity.rotate_ip(self.rotation)
            bullet.velocity *= PLAYER_SHOOT_SPEED