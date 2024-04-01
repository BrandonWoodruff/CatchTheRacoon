import pygame
import random
import sys

# Initialize pygame
pygame.init()

class DisplayGame:

    def create_screen(self, width, height):
        #create the screen
        screen = pygame.display.set_mode((width, height))
        pygame.display.flip()
        return screen, width, height

    def background(self, screen):
        #Create the Background
        background = pygame.image.load('background.jpg')
        screen.blit(background, (0, 0))

    def title(self):
        #Title and Icon
        pygame.display.set_caption('Catch the Raccoon')
        icon = pygame.image.load('dabr.jpg')
        pygame.display.set_icon(icon)

    def score(self, score, screen):    
        font = pygame.font.Font(None, 36)  # Define a font for the score display
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))  # Render the score text
        screen.blit(score_text, (10, 700))  # Display the score text on the screen
        racmove = 0

    def countdown(self, start, screen):
        font = pygame.font.Font(None, 36)
        countdown_text = font.render("Countdown: " + str(start // 1000), True, (255, 255, 255))
        screen.blit(countdown_text, (700, 700))

    def start_game(self, screen, width, height):
        start_font = pygame.font.Font(None, 72)
        instructions_font = pygame.font.Font(None, 36)
        title_text = start_font.render("Catch the Raccoon", True, (0, 0, 0))
        instructions_text = instructions_font.render("Press Space to start the game", True, (0,0,0))
        title_rect = title_text.get_rect(center=(width // 2, height // 2))
        instructions_rect = instructions_text.get_rect(center=(width // 2, height // 2 + 50))
        background = pygame.image.load('background.jpg')
        screen.blit(background, (0, 0))
        icon = pygame.image.load('dabr.jpg')
        icon = pygame.transform.scale(icon, (200, 200))
        icon_rect = icon.get_rect(center=(width // 2, height // 2 - 140))
        screen.blit(icon, icon_rect)
        screen.blit(title_text, title_rect)
        screen.blit(instructions_text, instructions_rect)
        pygame.display.update()
        
        

    def game_over(self, screen, score, width, height):
        background = pygame.image.load('background.jpg')
        screen.blit(background, (0, 0))  

        # Display the game over message
        font = pygame.font.Font(None, 64)
        game_over_text = font.render("Game Over", True, (0, 0, 0))
        text_rect = game_over_text.get_rect(center=(width // 2, height // 2 -50))
        screen.blit(game_over_text, text_rect)

        # Display the score
        score_text = font.render("Score: " + str(score), True, (0, 0, 0))
        score_rect = score_text.get_rect(center=(width // 2, height // 2))
        screen.blit(score_text, score_rect)

        # Display the play again message
        play_again_text = font.render("Press SPACE to Play Again", True, (0, 0, 0))
        play_again_rect = play_again_text.get_rect(center=(width // 2, height // 2 + 50))
        screen.blit(play_again_text, play_again_rect)

        icon = pygame.image.load('dabr.jpg')
        icon = pygame.transform.scale(icon, (200, 200))
        icon_rect = icon.get_rect(center=(width // 2, height // 2 - 200))
        screen.blit(icon, icon_rect)
        

        pygame.display.flip() 

class Racket(pygame.sprite.Sprite):

    def __init__(self, width, height, running, moving):
        super().__init__()
        self._image = pygame.image.load('racket.png')
        self._rect = self._image.get_rect()
        self._rect.center = width//2, height//2
        self._running = running
        self._moving = moving



    def racket_display(self, screen):
        screen.blit(self._image, self._rect)

    def racket_movement_setup(self):
        #Racket movement set up
        self._image.convert()
        return self._image, self._rect
    
    def racket_movement(self, score, raccoon1):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                self._moving = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if self._rect.collidepoint(event.pos):
                    self._moving = True
                    if raccoon1._rect.collidepoint(event.pos):
                        score += 25
            elif event.type == pygame.MOUSEMOTION and self._moving:
                self._rect.move_ip(event.rel)
            
        return self._running, self._moving, score
    

class Raccoon(pygame.sprite.Sprite):

    def __init__(self, width, height, running, moving):
        super().__init__()
        self._image = pygame.image.load('racoon.png')
        self._rect = self._image.get_rect()
        self._rect.center = width//2, height//2
        self._image = pygame.transform.scale(self._image, (200, 200))
        self._running = running
        self._moving = moving
        self._speed = 5

    def raccoon_display(self, screen):
        screen.blit(self._image, self._rect)


    
class Trash(pygame.sprite.Sprite):

    def __init__(self, running, moving):
        super().__init__()
        self._image = pygame.image.load('trash.png')
        self._rect = self._image.get_rect()
        self._image = pygame.transform.scale(self._image, (300, 300))
        self._running = running
        self._moving = moving

    def trash_display(self, screen):
        screen.blit(self._image, self._rect)

    def trash_movement(self):
        pass






def main():

    clock = pygame.time.Clock()

    game = DisplayGame()

    width = 1000
    height = 800
    screen = ''


    

    screen, width, height = game.create_screen(width, height)

    game.title()
    game.start_game(screen, width, height)

    start_game = False
    while not start_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    start = 30000
    racmove = 1

    
    
    score = 0

    #Racket movement set up
    #Game Loop
    running = True 
    moving = False
    racket1 = Racket(width, height, running, moving)

    trash_instances = []


    # Calculate the gap between trash instances
    gap_x = width // 4
    gap_y = height // 4

    # Calculate the starting x position for centering
    start_x = (width -1* gap_x) // 2

    # Create the first row of trash instances
    for i in range(3):
        trash = Trash(running, moving)
        trash._rect.x = start_x + i * gap_x - trash._rect.width // 2
        trash._rect.y = 1.5 * gap_y - trash._rect.height // 2
        trash_instances.append(trash)

    # Create the second row of trash instances
    for i in range(3):
        trash = Trash(running, moving)
        trash._rect.x = start_x + i * gap_x - trash._rect.width // 2
        trash._rect.y = 3 * gap_y - trash._rect.height // 2
        trash_instances.append(trash)

    raccoon1 = Raccoon(width, height, running, moving)


    gameover = True
    while gameover == True:

        while running == True:

        
            

            racket1.racket_movement_setup()

            running, moving, score = racket1.racket_movement(score, raccoon1)





            #Create the Background
            game.background(screen)

            for trash in trash_instances:
                trash.trash_display(screen)

            raccoon1.raccoon_display(screen)
            
            racket1.racket_display(screen)

            game.score(score, screen)


            racmove -= 1
            if racmove == 0:
                random_trash = random.choice(trash_instances)
                raccoon1._rect.center = random_trash._rect.center
                racmove = 30




            start -= clock.get_time()
            if start <= 0:
                running = False
            
            
            game.countdown(start, screen)

            # Update the GUI pygame
            pygame.display.update()
            clock.tick(100)

        if running == False:

            

            game.game_over(screen, score, width, height)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = True
                        score = 0
                        start = 30000
                        racmove = 30
                        racket1._rect.center = width//2, height//2
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit(0)

    
    # Quit the GUI game
    pygame.quit()


if __name__ == '__main__':
    main()



#<a href="https://www.freepik.com/free-vector/city-landfill-with-pile-garbage-plastic-trash_35026750.htm#query=trash%20yard&position=11&from_view=search&track=ais">Image by upklyak</a> on Freepik
#<a href="https://www.freepik.com/free-vector/raccoon-dancing-animal-cartoon-sticker_22301864.htm#query=racoon&position=1&from_view=search&track=sph">Image by brgfx</a> on Freepik
#<a href="https://www.freepik.com/free-vector/trash-can-filled-with-garbage-bags-glasses-wine-plastic-bottles-banana-peels_9641595.htm#query=trash%20can&position=22&from_view=search&track=ais">Image by frimufilms</a> on Freepik
#<a href="https://www.freepik.com/free-vector/cute-raccoon-dabbing-cartoon-vector-icon-illustration-animal-nature-icon-concept-isolated-premium-vector-flat-cartoon-style_16305709.htm#query=racoon&position=42&from_view=search&track=sph">Image by catalyststuff</a> on Freepik
#<a href="https://www.flaticon.com/free-icons/ping-pong" title="ping pong icons">Ping pong icons created by Freepik - Flaticon</a>
