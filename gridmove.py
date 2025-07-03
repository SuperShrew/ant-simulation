import pygame
import random
import sys

# --- Config ---
CELL_SIZE = 40
GRID_WIDTH = 10
GRID_HEIGHT = 10
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

# Colors
BG_COLOR = (30, 30, 30)
GRID_COLOR = (50, 50, 50)
PLAYER_COLOR = (0, 200, 255)
AI_COLOR = (255, 100, 100)

# --- Init ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# --- Grid Entities ---
player_pos = [5, 5]
ai_pos = [0, 0]

# --- Helper Functions ---
def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)

def draw_entity(pos, color):
    rect = pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

def move_random(pos):
    # Randomly pick a direction: up, down, left, right, or stay
    directions = [(0,0), (1,0), (-1,0), (0,1), (0,-1)]
    dx, dy = random.choice(directions)
    new_x = max(0, min(GRID_WIDTH - 1, pos[0] + dx))
    new_y = max(0, min(GRID_HEIGHT - 1, pos[1] + dy))
    pos[0], pos[1] = new_x, new_y

# --- Game Loop ---
while True:
    # --- Events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- Input ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 1
    elif keys[pygame.K_RIGHT] and player_pos[0] < GRID_WIDTH - 1:
        player_pos[0] += 1
    elif keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= 1
    elif keys[pygame.K_DOWN] and player_pos[1] < GRID_HEIGHT - 1:
        player_pos[1] += 1

    # --- AI Movement (random every frame) ---
    move_random(ai_pos)

    # --- Render ---
    screen.fill(BG_COLOR)
    draw_grid()
    draw_entity(player_pos, PLAYER_COLOR)
    draw_entity(ai_pos, AI_COLOR)
    pygame.display.flip()
    clock.tick(5)  # Slow down the loop a bit for visibility
