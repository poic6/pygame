import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0,0,0)

pygame.init()
pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

x = SCREEN_WIDTH//2
y = SCREEN_HEIGHT//2
dx = 0
dy = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                dx = -5
            elif event.key==pygame.K_RIGHT:
                dx = 5
            elif event.key==pygame.K_UP:
                dy = -5
            elif event.key==pygame.K_DOWN:
                dy = 5
        elif event.type==pygame.KEYUP:
            dx = 0
            dy = 0

    screen.fill(WHITE)
    rect = pygame.Rect(0, 0, 20, 20)
    rect.center = (x, y)
    if rect.left <= 0:
        dx = 0
        x += 1
    elif rect.right >= SCREEN_WIDTH:
        dx = 0
        x -= 1
    
    if rect.top <= 0:
        dy = 0
        y += 1
    elif rect.bottom >= SCREEN_HEIGHT:
        dy = 0
        y -= 1
    
    x += dx
    y += dy
    
    pygame.draw.rect(screen, BLACK, rect, 0)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()