"""
Main menu system for Tetris game
Handles mode selection (1-player vs 2-player)
"""

import pygame
from .config import *


class Menu:
    """Main menu class"""
    
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.Font(None, FONT_SIZE_LARGE)
        self.font_medium = pygame.font.Font(None, FONT_SIZE_MEDIUM)
        self.font_small = pygame.font.Font(None, FONT_SIZE_SMALL)
        self.selected_option = 0
        self.options = [
            ("1 Player", 1),
            ("2 Players", 2),
            ("Rankings", 3),
            ("Quit", 0)
        ]
    
    def handle_input(self, event):
        """Handle menu input"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                return self.options[self.selected_option][1]
        return None
    
    def draw(self):
        """Draw menu screen"""
        self.screen.fill(BLACK)
        
        # Title
        title = self.font_large.render("TETRIS", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
        self.screen.blit(title, title_rect)
        
        # Menu options
        start_y = SCREEN_HEIGHT // 2 - 50
        for i, (text, _) in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected_option else WHITE
            option_text = self.font_medium.render(text, True, color)
            option_rect = option_text.get_rect(center=(SCREEN_WIDTH // 2, start_y + i * 60))
            self.screen.blit(option_text, option_rect)
        
        # Instructions
        instructions = [
            "Use UP/DOWN arrows to navigate",
            "Press ENTER or SPACE to select"
        ]
        inst_y = SCREEN_HEIGHT - 100
        for i, inst in enumerate(instructions):
            inst_text = self.font_small.render(inst, True, GRAY)
            inst_rect = inst_text.get_rect(center=(SCREEN_WIDTH // 2, inst_y + i * 25))
            self.screen.blit(inst_text, inst_rect)

