import pygame
import os

# 화면크기
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 320
# 색
LAND = (160,120,40)
# 초기화
pygame.init()
# 창 이름
pygame.display.set_caption("이미지")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 화면업데이트 속도
clock = pygame.time.Clock()

# 그림 불러오기
current_path = os.path.dirname(__file__) # 현재 작업중인 폴더위치
assets_path = os.path.join(current_path, 'assets')
background_image = pygame.image.load(os.path.join(assets_path, 'terrain.png'))
mushroom1 = pygame.image.load(os.path.join(assets_path, 'mushroom1.png'))
mushroom2 = pygame.image.load(os.path.join(assets_path, 'mushroom2.png'))
mushroom3 = pygame.image.load(os.path.join(assets_path, 'mushroom3.png'))

# 게임반복구간
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(LAND)
    screen.blit(background_image, background_image.get_rect())
    screen.blit(mushroom1, [100, 50])
    screen.blit(mushroom2, [250, 130])
    screen.blit(mushroom3, [550, 130])
    screen.blit(mushroom3, [450, 130])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

