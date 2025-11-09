"""
Configuration file for Tetris game
Contains all game constants, colors, and settings
"""

import pygame

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
CELL_SIZE = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
LIGHT_GRAY = (192, 192, 192)

# Tetromino colors
COLORS = {
    'I': (0, 255, 255),      # Cyan
    'O': (255, 255, 0),      # Yellow
    'T': (128, 0, 128),      # Purple
    'S': (0, 255, 0),        # Green
    'Z': (255, 0, 0),        # Red
    'J': (0, 0, 255),        # Blue
    'L': (255, 165, 0),      # Orange
    'GHOST': (100, 100, 100) # Gray for ghost piece
}

# Board colors
BOARD_BG = (20, 20, 20)
BOARD_GRID = (40, 40, 40)
BOARD_BORDER = (60, 60, 60)

# Game settings
FPS = 60
INITIAL_FALL_SPEED = 500  # milliseconds
LEVEL_SPEED_REDUCTION = 50  # milliseconds per level
MIN_FALL_SPEED = 50  # minimum milliseconds

# Scoring
SCORE_SINGLE = 100
SCORE_DOUBLE = 300
SCORE_TRIPLE = 500
SCORE_TETRIS = 800
SCORE_SOFT_DROP = 1
SCORE_HARD_DROP = 2

# Lines per level
LINES_PER_LEVEL = 10

# Controls - Player 1
P1_LEFT = pygame.K_LEFT
P1_RIGHT = pygame.K_RIGHT
P1_DOWN = pygame.K_DOWN
P1_ROTATE = pygame.K_UP
P1_HARD_DROP = pygame.K_SPACE

# Controls - Player 2
P2_LEFT = pygame.K_a
P2_RIGHT = pygame.K_d
P2_DOWN = pygame.K_s
P2_ROTATE = pygame.K_w
P2_HARD_DROP = pygame.K_q

# Font sizes
FONT_SIZE_LARGE = 48
FONT_SIZE_MEDIUM = 32
FONT_SIZE_SMALL = 24

