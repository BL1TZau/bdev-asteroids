import pygame
from constants import *
from player import *

def main():
    pygame.init()   # pygame initialisation
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # setting display px
    dt = 0
    
    clock = pygame.time.Clock()
    
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        # makes x close window
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # showing colour on screen     
        
        player1.update(dt)      # rotates player
        player1.draw(screen)    # render p1 onto screen
        
        pygame.display.flip()   # refresh screen
        delta_time = clock.tick(60) # 60fps , pauses game look until arg
        dt = delta_time / 1000  # converting miliseconds to s
        
        
    
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

if __name__ == "__main__":
    main()