import pygame

# 게임창의 크기
SCREEN_WIDTH = 800 # 가로길이
SCREEN_HEIGHT = 600 # 세로길이

# 색깔
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# 초기화
pygame.init()
# 창 이름
pygame.display.set_caption("pygame")
# 창 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 게임화면 업데이트 속도
clock = pygame.time.Clock()
# 게임종료여부
done = False
# 게임반복구간
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # 게임로직구간
    # 화면삭제구간
    # 스크린채우기
    screen.fill(WHITE)
    # 화면 그리기 구간
    # 화면 업데이트
    pygame.display.flip()
    # 초당 60프레임으로 업데이트
    clock.tick(60)
pygame.quit()