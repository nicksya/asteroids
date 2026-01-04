import pygame, random # pyright: ignore[reportMissingImports]
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            rotation_vector = self.velocity.rotate(angle)
            shard_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            shard_1.velocity = rotation_vector * 1.2
            shard_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            shard_2.velocity = - rotation_vector * 1.2

            