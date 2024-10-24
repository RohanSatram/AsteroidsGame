from circleshape import *
import pygame
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0.0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        white = (255,255,255)
        pygame.draw.polygon(screen, white, self.triangle(), width = 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        new_shot =  Shot(self.position.x, self.position.y, SHOT_RADIUS)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-PLAYER_TURN_SPEED * dt)
        if keys[pygame.K_d]:
            self.rotate(PLAYER_TURN_SPEED * dt)
        if keys[pygame.K_w]:
            self.move(PLAYER_SPEED * dt)
        if keys[pygame.K_s]:
            self.move(-PLAYER_SPEED * dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_timer <= 0:
                self.shoot()
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
    