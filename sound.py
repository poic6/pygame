import pygame
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("사운드")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")
background_image = pygame.image.load(os.path.join(assets_path, "equalizer.png"))
pygame.mixer.music.load(os.path.join(assets_path, "bgm.wav"))
pygame.mixer.music.play(-1)
sound = pygame.mixer.Sound(os.path.join(assets_path, "sound.wav"))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound.play()
    
    screen.fill(BLACK)
    screen.blit(background_image, background_image.get_rect())
    pygame.display.flip()
    clock.tick(60)
pygame.quit()