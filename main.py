import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--debug", action="store_true", help="Enable debug mode")
args = parser.parse_args()

DEBUG = args.debug

def main():
    pygame.init()   # pygame initialisation
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # setting display px
    dt = 0
    clock = pygame.time.Clock()
    
    # Group Creation
    group_updateable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    group_shots = pygame.sprite.Group()
    
    # Adding containers to Groups
    Player.containers = (group_drawable, group_updateable)
    Asteroid.containers = (group_drawable, group_updateable, group_asteroids)
    AsteroidField.containers = (group_updateable)
    Shot.containers = (group_shots, group_updateable, group_drawable)
    
    # Creating player object
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    # pygame.Surface.convert() with no arguments, to create a copy that will draw more quickly on the screen.
    BACKGROUND_DIR = './data/backgrounds/custom.png'
    background = pygame.image.load(BACKGROUND_DIR).convert() 
    background = pygame.transform.scale(background, (1280, 720))
    
    while True:
        # admin - x close window
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                return
            
        screen.blit(background, (0, 0))
        
        for updateables in group_updateable:
            updateables.update(dt)       # update positions
            
        for asteroid in group_asteroids:
            for bullet in group_shots:
                if bullet.collision(asteroid) == True:
                    bullet.kill()   # inbuilt pygame feature removing obj from all groups
                    asteroid.split()
            if asteroid.collision(player1) == True:
                print('Game Over Bud')
                sys.exit()
        
        group_drawable.draw(screen) # render drawables
        
        if DEBUG:
            # draws hitboxes
            for sprite in group_drawable:
                pygame.draw.circle(screen, "red", sprite.position, sprite.radius, 1)
        
        pygame.display.flip()   # refresh screen
        delta_time = clock.tick(60) # 60fps , pauses game look until arg
        dt = delta_time / 1000  # converting miliseconds to s
        
        
    
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

if __name__ == "__main__":
    main()