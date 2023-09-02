# 화면크기 600*600
# 배경색: 자유
# 공: 원 그리기 이용, 색깔 자유
# 게임이 시작되면, 공이 화면 중간에서 나타나고, 키보드 조작 없이
# 직선으로 움직인다. 화면 끝에 닿으면 튕겨서 다른 곳으로 간다.
import pygame
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
pygame.display.set_caption("공게임")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

x = SCREEN_WIDTH//2
y = SCREEN_HEIGHT//2
dx=random.randint(1,10)
dy=random.randint(1,10)

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, [x, y], 10)
    x += dx
    y += dy
    if x>SCREEN_WIDTH or x<0:
        dx *= -1
    if y>SCREEN_HEIGHT or y<0:
        dy *= -1
    pygame.display.flip()
    clock.tick(60)
pygame.quit()