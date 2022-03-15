import pygame
import os
import random

pygame.init()

# GLOBALNE STAŁE
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1110
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("images/Runner", "RunnerRun1.png")),
           pygame.image.load(os.path.join("images/Runner", "RunnerRun2.png"))]

JUMPING = pygame.image.load(os.path.join("images/Runner", "RunnerJump.png"))

DUCKING = [pygame.image.load(os.path.join("images/Runner", "RunnerDuck1.png")),
           pygame.image.load(os.path.join("images/Runner", "RunnerDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("images/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("images/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("images/Cactus", "SmallCactus3.png"))]

LARGE_CACTUS = [pygame.image.load(os.path.join("images/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("images/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("images/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("images/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("images/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("images/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("images/Other", "Track.png"))


class Runner:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 330
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.runner_duck = False
        self.runner_run = True
        self.runner_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.runner_rect = self.image.get_rect()
        self.runner_rect.x = self.X_POS
        self.runner_rect.y = self.Y_POS

    def update(self, input):
        if self.runner_duck:
            self.duck()
        if self.runner_run:
            self.run()
        if self.runner_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if input[pygame.K_UP] and not self.runner_jump:
            self.runner_duck = False
            self.runner_run = False
            self.runner_jump = True
        elif input[pygame.K_DOWN] and not self.runner_jump:
            self.runner_duck = True
            self.runner_run = False
            self.runner_jump = False
        elif not (self.runner_jump or input[pygame.K_DOWN]):
            self.runner_duck = False
            self.runner_run = True
            self.runner_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.runner_rect = self.image.get_rect()
        self.runner_rect.x = self.X_POS
        self.runner_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.runner_rect = self.image.get_rect()
        self.runner_rect.x = self.X_POS
        self.runner_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.runner_jump:
            self.runner_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.runner_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.runner_rect.x, self.runner_rect.y))

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(500, 1000)
            self.y = random.randint(10, 15)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x,self.y))

def main():
    global game_speed, x_pos_bg, y_pos_bg, points
    run = True
    clock = pygame.time.Clock()
    player = Runner()
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 375
    points = 0
    font = pygame.font.Font('freesansbold.ttf',25)

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("POINTS: " + str(points), True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000,40)
        SCREEN.blit(text, text_rect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg - 20 <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((204, 255, 255))
        input = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(input)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()


main()
