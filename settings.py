import pygame
from math import ceil
from random import randint

cell_number = 20
cell_size = 33

side_length = cell_number * cell_size + 1
surfaces_size = pygame.Vector2((cell_size-1, cell_size-1))
offset = pygame.Vector2((ceil(cell_size/2), ceil(cell_size/2)))

resolution = (side_length,side_length)
SNAKE_COLOR = "seagreen2"
FOOD_COLOR = "red"