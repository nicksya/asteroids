import pygame # pyright: ignore[reportMissingImports]
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MAX_RADIUS
from logger import log_state
from player import Player # pyright: ignore[reportMissingImports]
from asteroid import Asteroid # pyright: ignore[reportMissingImports]
from asteroidfield import AsteroidField # pyright: ignore[reportMissingImports]

def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    #pygame.display.set_mode() 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = Asteroid(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, ASTEROID_MAX_RADIUS)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
