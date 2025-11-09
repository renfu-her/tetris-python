"""
Main entry point for Tetris game
Initializes pygame and coordinates game flow
"""

import pygame
import sys
from app.config import *
from app.game import Game
from app.menu import Menu
from app.ui import UI
from app.ranking import RankingSystem


def main():
    """Main game loop"""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    
    menu = Menu(screen)
    ranking_system = RankingSystem()
    ui = UI(screen)
    
    current_game = None
    game_mode = None
    showing_game_over = False
    showing_rankings = False
    
    running = True
    
    while running:
        dt = clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if showing_rankings:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    showing_rankings = False
            elif showing_game_over:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    showing_game_over = False
                    current_game = None
                    game_mode = None
            elif current_game:
                # Handle game input
                current_game.handle_input(event)
            else:
                # Handle menu input
                selected = menu.handle_input(event)
                if selected == 0:  # Quit
                    running = False
                elif selected == 3:  # Rankings
                    showing_rankings = True
                elif selected in [1, 2]:  # Start game
                    game_mode = selected
                    current_game = Game(num_players=selected)
                    showing_game_over = False
        
        # Update game state
        if current_game and not showing_game_over:
            current_game.update(dt)
            
            if current_game.is_game_over():
                showing_game_over = True
                # Save high scores for single player
                if game_mode == 1:
                    player = current_game.players[0]
                    if ranking_system.is_high_score(player.score):
                        ranking_system.add_score(
                            player.score,
                            player.level,
                            player.lines_cleared
                        )
        
        # Draw
        if showing_rankings:
            ui.draw_rankings_screen(ranking_system)
        elif showing_game_over and current_game:
            ui.draw_game_over(current_game.players, ranking_system)
        elif current_game:
            if game_mode == 1:
                ui.draw_1player_game(current_game.players[0], ranking_system)
            elif game_mode == 2:
                ui.draw_2player_game(
                    current_game.players[0],
                    current_game.players[1],
                    ranking_system
                )
        else:
            menu.draw()
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

