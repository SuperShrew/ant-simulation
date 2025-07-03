# this was programmed by an ai to help me understand the code for pygame
import pygame
import random
import sys

# --- Configurable Constants ---
CELL_SIZE = 40  # Size of each grid square in pixels
GRID_WIDTH = 20  # Number of columns
GRID_HEIGHT = 20  # Number of rows
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

# --- RGB Color Definitions ---
BG_COLOR = (30, 30, 30)        # Background color (dark gray)
GRID_COLOR = (50, 50, 50)      # Grid line color (slightly lighter gray)
PLAYER_COLOR = (0, 200, 255)   # Cyan for player
AI_COLOR = (255, 100, 100)     # Light red for AI

# --- Initialize Pygame ---
pygame.init()  # Set up all internal Pygame modules
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create a window
clock = pygame.time.Clock()  # Create a clock to control framerate

# --- Entity Positions on the Grid ---
player_pos = [5, 5]  # [x, y] position of player
ai_pos = [0, 0]      # [x, y] position of simple AI

# --- Function to Draw Grid Lines on the Screen ---
def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            # Create a rectangle for each cell
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            # Draw the rectangle border (grid lines)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)

# --- Function to Draw a Player or AI as a Colored Square ---
def draw_entity(pos, color):
    # Convert grid position to pixel coordinates
    rect = pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

# --- Simple AI Movement Function ---
def move_ai_towards_player():
    # Move the AI 1 cell closer to the player (greedy movement)
    dx = player_pos[0] - ai_pos[0]
    dy = player_pos[1] - ai_pos[1]
    
    # Prioritize horizontal movement if dx is larger
    if abs(dx) > abs(dy):
        ai_pos[0] += 1 if dx > 0 else -1
    elif dy != 0:
        ai_pos[1] += 1 if dy > 0 else -1

# --- Main Game Loop ---
while True:
    # --- Handle Events (like closing the window) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Shut down Pygame
            sys.exit()     # Exit the Python script

    # --- Handle Keyboard Input ---
    keys = pygame.key.get_pressed()  # Get state of all keyboard keys

    # Each direction: move player and then move AI once
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 1
        move_ai_towards_player()
    if keys[pygame.K_RIGHT] and player_pos[0] < GRID_WIDTH - 1:
        player_pos[0] += 1
        move_ai_towards_player()
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= 1
        move_ai_towards_player()
    if keys[pygame.K_DOWN] and player_pos[1] < GRID_HEIGHT - 1:
        player_pos[1] += 1
        move_ai_towards_player()

    # --- Drawing / Rendering ---
    screen.fill(BG_COLOR)         # Fill background with dark color
    draw_grid()                   # Draw the grid lines
    draw_entity(player_pos, PLAYER_COLOR)  # Draw player
    draw_entity(ai_pos, AI_COLOR)          # Draw AI

    pygame.display.flip()         # Update the display with all drawn content
    clock.tick(10)                # Limit to 10 frames per second (to slow it down)
