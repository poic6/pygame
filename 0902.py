import pygame
import os

# 스크린 크기(단위: px)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# 색 정의(RGB)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255, 0, 0)
SKYBLUE = (128,231,252)

#초기화
pygame.init()
pygame.display.set_caption("복습")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

#불러오기
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
image = pygame.image.load(os.path.join(assets_path, 'fish.png'))
x=SCREEN_WIDTH//2
y=SCREEN_HEIGHT//2
dx = 0
dy = 0

# 게임반복구간
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -5
            elif event.key == pygame.K_RIGHT:
                dx = 5
            elif event.key == pygame.K_UP:
                dy = -5
            elif event.key == pygame.K_DOWN:
                dy = 5
        elif event.type == pygame.KEYUP:
            dx = 0
            dy = 0
    x += dx
    y += dy
    screen.fill(WHITE)
    pygame.draw.line(screen, RED, [50,50], [300,300], 50)
    pygame.draw.line(screen, RED, [300,50], [50,300], 50)
    pygame.draw.rect(screen, GREEN, [200,200,50,50], 0)
    pygame.draw.circle(screen,BLACK, [300,300],10, 3)

    font = pygame.font.SysFont("Malgun Gothic", 30, False, False)
    font2 = pygame.font.SysFont("Malgun Gothic", 20, False, False)
    text = font.render("안녕 파이게임", True, BLACK)
    text2 = font2.render("9월 2일 토요일", True, BLACK)
    screen.blit(text, [10,10])
    screen.blit(text2, [10,50])
    screen.blit(image, [x, y])

    pygame.display.flip()
    clock.tick(60)
pygame.quit()