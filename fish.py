import pygame
import os
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

WHITE = (255, 255, 255)
SEA = (80, 180, 220)
GROUND = (140, 120, 40)
DARK_GROUND = (70, 60, 20)

current_path = os.path.dirname(__name__)
assets_path = os.path.join(current_path, "assets")

class Fish():
    def __init__(self):
        self.image = pygame.image.load(os.path.join(assets_path, "fish.png"))
        self.sound = pygame.mixer.Sound(os.path.join(assets_path, "swim.wav"))
        self.rect = self.image.get_rect()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.reset()
    
    def reset(self):
        self.rect.x = 250
        self.rect.y = 250
        self.dx = 0
        self.dy = 0

    def swim(self):
        self.dy = -10
        self.sound.play()
    
    def update(self):
        self.dy += 0.5
        self.rect.y += self.dy

        # 물고기가 화면 위로 올라갔을 때
        if self.rect.y <= 0:
            self.rect.y = 0
        # 물고기가 화면 아래로 내려왔을 때
        if self.rect.y > SCREEN_HEIGHT-self.height:
            self.rect.y = SCREEN_HEIGHT-self.height
            self.dy = 0
        
        if self.dy>20:
            self.dy = 20

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
class Pipe():
    def __init__(self):
        self.lpipe = pygame.image.load(os.path.join(assets_path, "pipe01.png"))
        self.lpipe_rect = self.lpipe.get_rect()
        self.lpipe_width = self.lpipe.get_rect().width
        self.lpipe_height = self.lpipe.get_rect().height

        spipes = ["pipe02.png", "pipe03.png", "pipe04.png", "pipe05.png", "pipe06.png"]
        self.spipe = pygame.image.load(os.path.join(assets_path, random.choice(spipes)))
        self.spipe_rect = self.spipe.get_rect()
        self.spipe_width = self.spipe.get_rect().width
        self.spipe_height = self.spipe.get_rect().height

        self.set_pos()
    
    # 파이프의 위치 설정
    def set_pos(self):
        self.random_pipe = random.randint(0, 1)
        # 긴 파이프 위에
        if self.random_pipe == 1:
            self.lpipe_rect.x = SCREEN_WIDTH
            self.lpipe_rect.y = -2
            self.spipe_rect.x = SCREEN_WIDTH
            self.spipe_rect.y = SCREEN_HEIGHT - self.spipe_height + 2
        # 긴 파이프가 아래에
        else:
            self.lpipe_rect.x = SCREEN_WIDTH
            self.lpipe_rect.y = SCREEN_HEIGHT - self.lpipe_height + 2
            self.spipe_rect.x = SCREEN_WIDTH
            self.spipe_rect.y = -2
    
    def update(self):
        self.lpipe_rect.x -= 4
        self.spipe_rect.x -= 4

    def out_of_screen(self):
        if self.spipe_rect.x + self.spipe_width <=0:
            return True
        return False
    
    def check_crash(self, fish):
        if self.lpipe_rect.colliderect(fish.rect):
            return True
        elif self.spipe_rect.colliderect(fish.rect):
            return True
        else:
            return False
    
    def draw(self, screen):
        screen.blit(self.lpipe, self.lpipe_rect)
        screen.blit(self.spipe, self.spipe_rect)

class Game():
    def __init__(self):
        pygame.mixer.music.load(os.path.join(assets_path, "bgm.mp3"))
        self.font = pygame.font.SysFont("malgungothic", 40, True, False)
        self.fish = Fish()
        self.pipes = []
        self.pipes.append(Pipe())
        self.pipes_pos = 0
        self.score = 0
        self.menu_on = True
    
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if self.menu_on == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.play(-1)
                        self.score = 0
                        self.menu_on = False
                        self.fish.reset()
                        self.pipes = []
                        self.pipes.append(Pipe())
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.fish.swim()
        return True
    
    def run_logic(self):
        for pipe in self.pipes:
            if pipe.spipe_rect.x == self.pipes_pos:
                self.pipes.append(Pipe())
                self.score += 1
            if pipe.out_of_screen():
                del self.pipes[0]
                self.pipe_pos = random.randrange(200, 400, 4)
            if pipe.check_crash(self.fish):
                pygame.mixer_music.stop()
                self.menu_on = True
    
    def draw_text(self, screen, text, font, x, y, main_color):
        text_obj = font.render(text, True, main_color)
        text_rect = text_obj.get_rect()
        text_rect.center = x, y
        screen.blit(text_obj, text_rect)

    def display_menu(self, screen):
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        rect = (center_x-220, center_y-50, 440, 100)
        pygame.draw.rect(screen, GROUND, rect)
        pygame.draw.rect(screen, DARK_GROUND, rect, 4)
        self.draw_text(screen, "Press SpaceKey to Play", self.font, center_x, center_y, DARK_GROUND)

    def display_frame(self, screen):
        screen.fill(SEA)
        pygame.draw.rect(screen, GROUND, (0, SCREEN_HEIGHT-50, SCREEN_WIDTH, 50))
        pygame.draw.rect(screen, DARK_GROUND, (0, SCREEN_HEIGHT-50, SCREEN_WIDTH, SCREEN_HEIGHT - 50), 4)
        self.fish.update()
        self.fish.draw(screen)
        for pipe in self.pipes:
            pipe.update()
            pipe.draw(screen)
        self.draw_text(screen, "점수: "+str(self.score), self.font, 100, 50, WHITE)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('날아라 물고기')
    clock = pygame.time.Clock()

    game = Game()

    running = True
    
    while running:
        running = game.process_events()
        if game.menu_on:
            game.display_menu(screen)
        else:
            game.run_logic()
            game.display_frame(screen)
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

main()