import pygame
import time
import random

# Initialize the pygame
pygame.init()

# Set display dimensions
game_width, game_height = 800, 500
score_area_height = 60
total_height = game_height + score_area_height
win = pygame.display.set_mode((game_width, total_height))
pygame.display.set_caption('Snake Game')

# Define colors
white = (255, 255, 255)
black = (21, 21, 21)
grey = (28, 28, 28)
red = (169, 29, 58)
green = (0, 255, 0)
blue = (0, 128, 255)

# Snake attributes
snake_block = 10
snake_speed = 10

# Initialize the clock
clock = pygame.time.Clock()

# Define fonts for score and message
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def score_display(score):
    """Displays the current score on the screen."""
    value = score_font.render("Your Score: " + str(score), True, red)
    win.fill(grey, rect=[0, 0, game_width, score_area_height])  # Fill the score area with black
    win.blit(value, [10, 10])

def our_snake(snake_block, snake_list):
    """Draws the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(win, blue, [x[0], x[1] + score_area_height, snake_block, snake_block])

def message(msg, color):
    """Displays a message on the screen."""
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [game_width / 6, total_height / 3])

def gameLoop():
    """Main function that runs the game loop."""
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = game_width / 2
    y1 = game_height / 2

    # Initial movement direction
    x1_change = 0
    y1_change = 0

    # Snake initial attributes
    snake_List = []
    Length_of_snake = 1

    # Initial position of food
    foodx = round(random.randrange(0, game_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, game_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            win.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            score_display(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= game_width or x1 < 0 or y1 >= game_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        win.fill(black, rect=[0, score_area_height, game_width, game_height])  # Clear the game area
        pygame.draw.rect(win, green, [foodx, foody + score_area_height, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        score_display(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, game_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, game_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()
