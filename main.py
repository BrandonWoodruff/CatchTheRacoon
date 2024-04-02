import pygame
import random
import sys
import asyncio

# Initialize pygame
pygame.init()

# Constants
WIDTH = 1000
HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class DisplayGame:
    def create_screen(self, width, height):
        screen = pygame.display.set_mode((width, height))
        pygame.display.flip()
        return screen

    def background(self, screen):
        background = pygame.image.load('background.jpg')
        screen.blit(background, (0, 0))

    def title(self):
        pygame.display.set_caption('Catch the Raccoon')
        icon = pygame.image.load('dabr.jpg')
        pygame.display.set_icon(icon)

    def score(self, score, screen):
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

    def countdown(self, start, screen):
        font = pygame.font.Font(None, 36)
        countdown_text = font.render("Countdown: " + str(start // 1000), True, WHITE)
        screen.blit(countdown_text, (700, 10))

    def start_game(self, screen):
        font = pygame.font.Font(None, 72)
        instructions_font = pygame.font.Font(None, 36)
        title_text = font.render("Catch the Raccoon", True, BLACK)
        instructions_text = instructions_font.render("Press Space to start the game", True, BLACK)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()

    def game_over(self, screen, score):
        font = pygame.font.Font(None, 64)
        game_over_text = font.render("Game Over", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
        score_text = font.render("Score: " + str(score), True, BLACK)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()

class Racket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('racket.png')
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    def racket_display(self, screen):
        screen.blit(self.image, self.rect)

    def racket_movement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
        return True

class Raccoon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('racoon.png')
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    def raccoon_display(self, screen):
        screen.blit(self.image, self.rect)

async def main():
    clock = pygame.time.Clock()
    game = DisplayGame()
    screen = game.create_screen(WIDTH, HEIGHT)
    game.title()
    game.start_game(screen)

    racket = Racket()
    raccoon = Raccoon()
    score = 0
    start = 30000

    running = False
    while not running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    while running:
        screen.fill(BLACK)
        game.background(screen)
        racket.racket_display(screen)
        raccoon.raccoon_display(screen)
        game.score(score, screen)
        game.countdown(start, screen)

        start -= clock.get_time()
        if start <= 0:
            running = False

        pygame.display.update()
        clock.tick(100)

    game.game_over(screen, score)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    await main()
                elif event.type == pygame.QUIT:
                    asyn
                    pygame.quit()
                    sys.exit()

asyncio.run(main())
