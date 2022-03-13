import pygame
import os

pygame.init()

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
    x = 80
    y = 310

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.runner_duck = False
        self.runner_run = True
        self.runner_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.runner_rect = self.image.get_rect()
        self.runner_rect.x = self.x
        self.runner_rect.y = self.y

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
        pass

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.runner_rect = self.image.get_rect()
        self.runner_rect.x = self.x
        self.runner_rect.y = self.y
        self.step_index += 1

    def jump(self):
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.runner_rect.x, self.runner_rect.y))


def main():
    run = True
    clock = pygame.time.Clock()
    player = Runner()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((204, 255, 255))
        input = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(input)

        clock.tick(30)
        pygame.display.update()


main()
