import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()   # pygame initialisation
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # setting display px
    dt = 0
    clock = pygame.time.Clock()
    
    group_updateable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    
    Player.containers = (group_drawable, group_updateable)
    Asteroid.containers = (group_drawable, group_updateable, group_asteroids)
    AsteroidField.containers = (group_updateable)
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    
    
    while True:
        # makes x close window
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # showing colour on screen  
    
        for updateables in group_updateable:
            updateables.update(dt)       # update positions
            
        for asteroid in group_asteroids:
            if asteroid.collision(player1) == True:
                print('Game Over Bud')
                sys.exit()
        
        for drawable in group_drawable:
            drawable.draw(screen)   # render p1 onto screen
        
        pygame.display.flip()   # refresh screen
        delta_time = clock.tick(60) # 60fps , pauses game look until arg
        dt = delta_time / 1000  # converting miliseconds to s
        
        
    
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

if __name__ == "__main__":
    main()