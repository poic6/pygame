import pygame
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GRAY = (200,200,200)

pygame.init()
pygame.display.set_caption("키보드")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")
keyboard_image = pygame.image.load(os.path.join(assets_path, "keyboard.png"))
keyboard_x = int(SCREEN_WIDTH/2)
keyboard_y = int(SCREEN_HEIGHT/2)
keyboard_dx = 0
keyboard_dy = 0

done = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyboard_dx = -5
            elif event.key == pygame.K_RIGHT:
                keyboard_dx = 5
            elif event.key == pygame.K_UP:
                keyboard_dy = -5
            elif event.key == pygame.K_DOWN:
                keyboard_dy = 5
        elif event.type == pygame.KEYUP:
            keyboard_dx = 0
            keyboard_dy = 0
    screen.fill(GRAY)
    keyboard_x += keyboard_dx
    keyboard_y += keyboard_dy
    screen.blit(keyboard_image, [keyboard_x, keyboard_y])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()