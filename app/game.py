"""
Core game logic for Tetris
Handles game state, input processing, and game loop
"""

import pygame
from .config import *
from .player import Player


class Game:
    """Main game class"""
    
    def __init__(self, num_players=1):
        self.num_players = num_players
        self.players = []
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialize players
        for i in range(num_players):
            player = Player(i + 1, BOARD_WIDTH, BOARD_HEIGHT)
            self.players.append(player)
    
    def handle_input(self, event):
        """Handle keyboard input"""
        if event.type != pygame.KEYDOWN:
            return
        
        # Player 1 controls
        if self.num_players >= 1:
            p1 = self.players[0]
            if event.key == P1_LEFT:
                p1.move(-1, 0)
            elif event.key == P1_RIGHT:
                p1.move(1, 0)
            elif event.key == P1_DOWN:
                # Down key = hard drop (直接到底)
                p1.hard_drop()
            elif event.key == P1_ROTATE:
                p1.rotate_piece()
            elif event.key == P1_HARD_DROP:
                # Space key also works as hard drop
                p1.hard_drop()
        
        # Player 2 controls
        if self.num_players >= 2:
            p2 = self.players[1]
            if event.key == P2_LEFT:
                p2.move(-1, 0)
            elif event.key == P2_RIGHT:
                p2.move(1, 0)
            elif event.key == P2_DOWN:
                # Down key = hard drop (直接到底)
                p2.hard_drop()
            elif event.key == P2_ROTATE:
                p2.rotate_piece()
            elif event.key == P2_HARD_DROP:
                # Q key also works as hard drop
                p2.hard_drop()
    
    def update(self, dt):
        """Update game state"""
        for player in self.players:
            player.update(dt)
        
        # Check if game should end
        if any(player.game_over for player in self.players):
            self.running = False
    
    def is_game_over(self):
        """Check if game is over"""
        return not self.running or any(player.game_over for player in self.players)
    
    def get_ranking(self):
        """Get current ranking of players by score"""
        ranked_players = sorted(
            self.players,
            key=lambda p: p.score,
            reverse=True
        )
        return ranked_players

