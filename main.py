import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x,y)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps = pygame.time.Clock()
    dt = 0

    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        black = (0,0,0)
        screen.fill(black, rect=None, special_flags=0)

        for method in updatable:
            method.update(dt)
        
        for method in drawable:
            method.draw(screen)

        for method in asteroids:
            if method.check_collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if method.check_collision(shot):
                    method.split()
                    shot.kill()

        pygame.display.flip()
        dt = fps.tick(60)/1000

if __name__ == "__main__":
    main()