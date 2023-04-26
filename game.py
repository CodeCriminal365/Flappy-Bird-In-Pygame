import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Set up the game clock
clock = pygame.time.Clock()

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Define the player's properties
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 30
player_x = 50
player_y = 250
player_velocity = 0
GRAVITY = 0.75
JUMP_VELOCITY = -10

# Define the pipe's properties
PIPE_WIDTH = 60
PIPE_GAP = 150
pipe_x = WINDOW_WIDTH
pipe_y = random.randint(PIPE_GAP, WINDOW_HEIGHT - PIPE_GAP)
pipe_velocity = -5

# Define a function to draw the player
def draw_player():
    pygame.draw.rect(game_window, BLUE, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

# Define a function to move the player
def move_player():
    global player_y, player_velocity
    player_velocity += GRAVITY
    player_y += player_velocity
    if player_y >= WINDOW_HEIGHT - PLAYER_HEIGHT:
        player_y = WINDOW_HEIGHT - PLAYER_HEIGHT
        player_velocity = 0
    elif player_y < 0:
        player_y = 0
        player_velocity = 0

# Define a function to draw the pipes
def draw_pipes():
    pygame.draw.rect(game_window, GREEN, (pipe_x, 0, PIPE_WIDTH, pipe_y))
    bottom_pipe_y = pipe_y + PIPE_GAP
    bottom_pipe_height = WINDOW_HEIGHT - bottom_pipe_y
    pygame.draw.rect(game_window, GREEN, (pipe_x, bottom_pipe_y, PIPE_WIDTH, bottom_pipe_height))

# Define a function to move the pipes
def move_pipes():
    global pipe_x, pipe_y
    pipe_x += pipe_velocity
    if pipe_x < -PIPE_WIDTH:
        pipe_x = WINDOW_WIDTH
        pipe_y = random.randint(PIPE_GAP, WINDOW_HEIGHT - PIPE_GAP)

# Define a function to check for collisions
def check_collision():
    if player_x + PLAYER_WIDTH >= pipe_x and player_x <= pipe_x + PIPE_WIDTH:
        if player_y <= pipe_y or player_y + PLAYER_HEIGHT >= pipe_y + PIPE_GAP:
            return True
    return False

# Main game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_velocity = JUMP_VELOCITY

    # Move the player
    move_player()

    # Move the pipes
    move_pipes()

    # Check for collisions
    if check_collision():
        game_over = True

    # Draw the game objects
    game_window.fill(WHITE)
    draw_player()
    draw_pipes()
    pygame.display.update()

    # Set the game clock
    clock.tick(60)

# Quit Pygame
pygame.quit()
