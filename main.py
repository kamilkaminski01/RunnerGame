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

SMALL_OBSTACLE = [pygame.image.load(os.path.join("images/Obstacle", "SmallCactus1.png")),
                  pygame.image.load(os.path.join("images/Obstacle", "SmallCactus2.png")),
                  pygame.image.load(os.path.join("images/Obstacle", "SmallCactus3.png"))]

LARGE_OBSTACLE = [pygame.image.load(os.path.join("images/Obstacle", "LargeCactus1.png")),
                  pygame.image.load(os.path.join("images/Obstacle", "LargeCactus2.png")),
                  pygame.image.load(os.path.join("images/Obstacle", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("images/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("images/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("images/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("images/Other", "Track.png"))

START = pygame.image.load(os.path.join("images/Runner", "RunnerStart.png"))

GAME_OVER = pygame.image.load(os.path.join("images/Other", "GameOver.png"))


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
        self.x = SCREEN_WIDTH + random.randint(500, 1000)
        self.y = random.randint(10, 15)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(500, 1000)
            self.y = random.randint(10, 15)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class smallObstacle(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class largeObstacle(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Runner()
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 375
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 25)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("POINTS: " + str(points), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        SCREEN.blit(text, text_rect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg - 10 <= -image_width:
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

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(smallObstacle(SMALL_OBSTACLE))
            elif random.randint(0, 2) == 1:
                obstacles.append(largeObstacle(LARGE_OBSTACLE))
            elif random.randint(0 ,2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.runner_rect.colliderect(obstacle.rect):
                # pygame.draw.rect(SCREEN, (255,0,0), player.runner_rect, 2)
                SCREEN.blit(GAME_OVER, (360, 100))
                background()
                score()
                pygame.display.update()
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        background()
        cloud.draw(SCREEN)
        cloud.update()
        score()
        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((204,255,255))
        SCREEN.blit(BG, (0, 375))
        font = pygame.font.Font('freesansbold.ttf', 25)

        if death_count == 0:
            text = font.render("NACISNIJ DOWOLNY PRZYCISK ABY ROZPOCZAC", True, (0,0,0))
        elif death_count > 0:
            text = font.render("NACISNIJ DOWOLNY PRZYCISK ABY ROZPOCZAC", True, (0, 0, 0))
            score = font.render("TWOJE PUNKTY: " + str(points), True, (0,0,0))
            score_rect = score.get_rect()
            score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, score_rect)
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, text_rect)
        SCREEN.blit(START, (SCREEN_WIDTH // 2 - 45, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count = 0)