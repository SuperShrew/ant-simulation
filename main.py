# imports
import pygame
import random
import sys

# config variables
CELL_SIZE = 10
GRID_HEIGHT = 30
GRID_WIDTH = 60
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH

GRID_COLOR = (50, 50, 50)
ANT_COLOUR = (218, 147, 0)
BG_COLOR = (0, 150, 0)
BEETLE_COLOUR = (140, 0, 90)
FOOD_COLOUR = (250, 255, 90)
WALL_COLOUR = (130, 60, 40)
WATER_COLOUR = (0, 100, 255)

# initialisation
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

