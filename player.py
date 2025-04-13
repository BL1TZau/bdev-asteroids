from circleshape import *
from constants import *
from shot import *
import sys

class Player(CircleShape):
    containers = ()
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)   #
        self.rotation = 0
        self.icd = 0    # init icd
        self.health = 4

        # Load the image
        self.image_link = './data/ships/main-ship/main-ship-bases/pngs/main_4hp.png'
        self.original_image = pygame.image.load(self.image_link).convert_alpha()
        self.original_image = pygame.transform.flip(self.original_image, False, True)
        self.image = self.original_image
        # Positioning
        self.position = pygame.Vector2(x, y)
        self.rect = self.image.get_rect(center=(self.position))
        self.radius = self.image.get_width() / 2  # optional if still using radius elsewhere
    
    def take_damage(self):
        self.health -= 1
        print('damage taken')
        
        if self.health == 0:
            print('Game Over Bud')
            sys.exit()
        
        self.ship_damage()
    
    def ship_damage(self):
        loc = './data/ships/main-ship/main-ship-bases/pngs/main_'
        # empty str to easily index with hp beneath
        ship_damage_stages = [
            '',
            loc+'1hp.png',
            loc+'2hp.png',
            loc+'3hp.png',
            loc+'4hp.png',
        ]
        # admin
        self.original_image = pygame.image.load(ship_damage_stages[self.health]).convert_alpha()
        self.original_image = pygame.transform.flip(self.original_image, False, True)
        self.image = self.original_image
        # keeps rotation of player when hit
        self.image = pygame.transform.rotate(self.original_image, -self.rotation)

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