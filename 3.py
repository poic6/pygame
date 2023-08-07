import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
RED = (255,0,0)
GREEN = (0, 255, 0)

pygame.init()
pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

color = BLACK

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                color = RED
        elif event.type==pygame.KEYUP:
            color = BLACK
    screen.fill(WHITE)
    rect = pygame.Rect(400,300,100,100)
    pygame.draw.rect(screen, color, rect, 0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()