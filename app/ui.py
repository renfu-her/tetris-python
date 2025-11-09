"""
UI rendering functions for Tetris game
Handles drawing game boards, pieces, scores, and rankings
"""

import pygame
from .config import *


class UI:
    """UI rendering class"""
    
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.Font(None, FONT_SIZE_LARGE)
        self.font_medium = pygame.font.Font(None, FONT_SIZE_MEDIUM)
        self.font_small = pygame.font.Font(None, FONT_SIZE_SMALL)
    
    def draw_board(self, player, x, y, width=None, height=None):
        """Draw a player's game board"""
        if width is None:
            width = BOARD_WIDTH * CELL_SIZE
        if height is None:
            height = BOARD_HEIGHT * CELL_SIZE
        
        # Draw board background
        board_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, BOARD_BG, board_rect)
        pygame.draw.rect(self.screen, BOARD_BORDER, board_rect, 2)
        
        # Draw grid
        cell_w = width // BOARD_WIDTH
        cell_h = height // BOARD_HEIGHT
        
        for i in range(BOARD_WIDTH + 1):
            pygame.draw.line(
                self.screen,
                BOARD_GRID,
                (x + i * cell_w, y),
                (x + i * cell_w, y + height)
            )
        
        for i in range(BOARD_HEIGHT + 1):
            pygame.draw.line(
                self.screen,
                BOARD_GRID,
                (x, y + i * cell_h),
                (x + width, y + i * cell_h)
            )
        
        # Draw placed blocks
        for by in range(BOARD_HEIGHT):
            for bx in range(BOARD_WIDTH):
                if player.board[by][bx] != 0:
                    rect = pygame.Rect(
                        x + bx * cell_w + 1,
                        y + by * cell_h + 1,
                        cell_w - 2,
                        cell_h - 2
                    )
                    pygame.draw.rect(self.screen, player.board[by][bx], rect)
        
        # Draw current piece
        if player.current_piece:
            self._draw_piece(
                player.current_piece,
                x, y, cell_w, cell_h
            )
    
    def _draw_piece(self, piece, board_x, board_y, cell_w, cell_h):
        """Draw a tetromino piece"""
        blocks = piece.get_blocks()
        for bx, by in blocks:
            x = board_x + (piece.x + bx) * cell_w + 1
            y = board_y + (piece.y + by) * cell_h + 1
            
            rect = pygame.Rect(x, y, cell_w - 2, cell_h - 2)
            pygame.draw.rect(self.screen, piece.color, rect)
            pygame.draw.rect(self.screen, WHITE, rect, 1)
    
    def draw_next_piece(self, piece, x, y):
        """Draw next piece preview"""
        label = self.font_small.render("Next:", True, WHITE)
        self.screen.blit(label, (x, y))
        
        preview_y = y + 30
        if piece:
            blocks = piece.get_blocks()
            for bx, by in blocks:
                rect = pygame.Rect(
                    x + bx * CELL_SIZE,
                    preview_y + by * CELL_SIZE,
                    CELL_SIZE - 2,
                    CELL_SIZE - 2
                )
                pygame.draw.rect(self.screen, piece.color, rect)
                pygame.draw.rect(self.screen, WHITE, rect, 1)
    
    def draw_player_info(self, player, x, y):
        """Draw player information (score, level, lines)"""
        info_y = y
        
        # Player label
        label = self.font_medium.render(f"Player {player.player_id}", True, WHITE)
        self.screen.blit(label, (x, info_y))
        info_y += 35
        
        # Score
        score_text = self.font_small.render(f"Score: {player.score}", True, WHITE)
        self.screen.blit(score_text, (x, info_y))
        info_y += 25
        
        # Level
        level_text = self.font_small.render(f"Level: {player.level}", True, WHITE)
        self.screen.blit(level_text, (x, info_y))
        info_y += 25
        
        # Lines cleared
        lines_text = self.font_small.render(f"Lines: {player.lines_cleared}", True, WHITE)
        self.screen.blit(lines_text, (x, info_y))
    
    def draw_ranking(self, players, x, y, is_game_over=False):
        """Draw ranking display"""
        if len(players) == 0:
            return
        
        # Title
        if len(players) > 1:
            title = "Ranking"
            title_text = self.font_medium.render(title, True, WHITE)
            self.screen.blit(title_text, (x, y))
            y += 35
            
            # Sort players by score
            ranked = sorted(players, key=lambda p: p.score, reverse=True)
            
            for i, player in enumerate(ranked):
                rank = i + 1
                color = WHITE if not is_game_over else (255, 215, 0) if rank == 1 else WHITE
                
                rank_text = f"{rank}. Player {player.player_id}: {player.score}"
                text = self.font_small.render(rank_text, True, color)
                self.screen.blit(text, (x, y))
                y += 25
        else:
            # Single player - show current score prominently with background box
            title = "Current Score"
            title_text = self.font_medium.render(title, True, WHITE)
            title_rect = title_text.get_rect()
            
            # Draw background box for current score
            box_width = max(title_rect.width, 120)
            box_height = 80
            box_rect = pygame.Rect(x - 5, y - 5, box_width + 10, box_height)
            pygame.draw.rect(self.screen, (200, 0, 0), box_rect)  # Red background
            pygame.draw.rect(self.screen, WHITE, box_rect, 2)  # White border
            
            self.screen.blit(title_text, (x, y))
            y += 35
            
            player = players[0]
            score_text = f"{player.score}"
            text = self.font_small.render(score_text, True, WHITE)
            self.screen.blit(text, (x, y))
    
    def draw_high_scores(self, high_scores, x, y):
        """Draw high scores list"""
        title = self.font_medium.render("High Scores", True, WHITE)
        self.screen.blit(title, (x, y))
        y += 35
        
        for i, entry in enumerate(high_scores[:5]):
            score_text = f"{i+1}. {entry['score']} (Lv{entry['level']}, {entry['lines']} lines)"
            text = self.font_small.render(score_text, True, WHITE)
            self.screen.blit(text, (x, y))
            y += 25
    
    def draw_rankings_screen(self, ranking_system):
        """Draw full rankings screen"""
        self.screen.fill(BLACK)
        
        # Title
        title = self.font_large.render("RANKINGS", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.screen.blit(title, title_rect)
        
        # Get top scores
        high_scores = ranking_system.get_top_scores(10)
        
        if not high_scores:
            # No scores yet
            no_scores = self.font_medium.render("No scores yet!", True, GRAY)
            no_scores_rect = no_scores.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(no_scores, no_scores_rect)
        else:
            # Draw rankings table
            start_y = 150
            spacing = 40
            
            # Header
            header_y = start_y
            headers = ["Rank", "Score", "Level", "Lines"]
            header_x_positions = [
                SCREEN_WIDTH // 2 - 300,
                SCREEN_WIDTH // 2 - 100,
                SCREEN_WIDTH // 2 + 100,
                SCREEN_WIDTH // 2 + 250
            ]
            
            for i, header in enumerate(headers):
                header_text = self.font_medium.render(header, True, (255, 255, 0))
                self.screen.blit(header_text, (header_x_positions[i], header_y))
            
            # Draw separator line
            pygame.draw.line(
                self.screen,
                GRAY,
                (SCREEN_WIDTH // 2 - 350, header_y + 35),
                (SCREEN_WIDTH // 2 + 350, header_y + 35),
                2
            )
            
            # Draw scores
            for i, entry in enumerate(high_scores):
                rank = i + 1
                y = start_y + spacing + (i * spacing)
                
                # Highlight top 3
                if rank <= 3:
                    color = (255, 215, 0) if rank == 1 else (192, 192, 192) if rank == 2 else (205, 127, 50)
                else:
                    color = WHITE
                
                # Rank
                rank_text = self.font_small.render(f"{rank}.", True, color)
                self.screen.blit(rank_text, (header_x_positions[0], y))
                
                # Score
                score_text = self.font_small.render(str(entry['score']), True, color)
                self.screen.blit(score_text, (header_x_positions[1], y))
                
                # Level
                level_text = self.font_small.render(f"Lv{entry['level']}", True, color)
                self.screen.blit(level_text, (header_x_positions[2], y))
                
                # Lines
                lines_text = self.font_small.render(str(entry['lines']), True, color)
                self.screen.blit(lines_text, (header_x_positions[3], y))
        
        # Instructions
        instruction = self.font_small.render("Press ESC to return to menu", True, GRAY)
        instruction_rect = instruction.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        self.screen.blit(instruction, instruction_rect)
    
    def draw_game_over(self, players, ranking_system):
        """Draw game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game Over text
        game_over_text = self.font_large.render("GAME OVER", True, WHITE)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        self.screen.blit(game_over_text, text_rect)
        
        # Final rankings
        y = SCREEN_HEIGHT // 2 - 20
        ranked = sorted(players, key=lambda p: p.score, reverse=True)
        
        for i, player in enumerate(ranked):
            rank = i + 1
            color = (255, 215, 0) if rank == 1 else WHITE
            
            rank_text = f"{rank}. Player {player.player_id}: {player.score} points"
            text = self.font_medium.render(rank_text, True, color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y))
            self.screen.blit(text, text_rect)
            y += 40
        
        # Press any key to continue
        continue_text = self.font_small.render("Press ESC to return to menu", True, GRAY)
        text_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        self.screen.blit(continue_text, text_rect)
    
    def draw_1player_game(self, player, ranking_system):
        """Draw single player game screen"""
        self.screen.fill(BLACK)
        
        # Calculate board position (centered)
        board_width = BOARD_WIDTH * CELL_SIZE
        board_height = BOARD_HEIGHT * CELL_SIZE
        board_x = SCREEN_WIDTH // 2 - board_width // 2 - 150
        board_y = SCREEN_HEIGHT // 2 - board_height // 2
        
        # Draw board
        self.draw_board(player, board_x, board_y)
        
        # Draw player info (left side)
        info_x = board_x - 200
        info_y = board_y
        self.draw_player_info(player, info_x, info_y)
        
        # Draw next piece (right side, aligned with left side and moved down)
        next_x = board_x + board_width + 50
        next_y = board_y + 30  # Move down to align with left side player info
        self.draw_next_piece(player.next_piece, next_x, next_y)
        
        # Draw current score (right side, below next piece with more spacing)
        ranking_y = next_y + 200  # Increased spacing from next piece (add one blank line space)
        self.draw_ranking([player], next_x, ranking_y)
        
        # Draw high scores (right side, below current score with more spacing)
        high_scores = ranking_system.get_top_scores(5)
        if high_scores:
            # Add more spacing to avoid overlap with red box (80px box height + 20px margin)
            self.draw_high_scores(high_scores, next_x, ranking_y + 120)
    
    def draw_2player_game(self, player1, player2, ranking_system):
        """Draw two player split-screen game"""
        self.screen.fill(BLACK)
        
        # Calculate board dimensions for split screen
        board_width = BOARD_WIDTH * CELL_SIZE
        board_height = BOARD_HEIGHT * CELL_SIZE
        margin = 50
        
        # Player 1 (left side)
        p1_board_x = margin
        p1_board_y = SCREEN_HEIGHT // 2 - board_height // 2
        
        self.draw_board(player1, p1_board_x, p1_board_y)
        
        # Player 1 info
        p1_info_x = p1_board_x
        p1_info_y = p1_board_y - 100
        self.draw_player_info(player1, p1_info_x, p1_info_y)
        
        # Player 1 next piece
        p1_next_x = p1_board_x + board_width + 20
        p1_next_y = p1_board_y
        self.draw_next_piece(player1.next_piece, p1_next_x, p1_next_y)
        
        # Player 2 (right side)
        p2_board_x = SCREEN_WIDTH - margin - board_width
        p2_board_y = SCREEN_HEIGHT // 2 - board_height // 2
        
        self.draw_board(player2, p2_board_x, p2_board_y)
        
        # Player 2 info
        p2_info_x = p2_board_x
        p2_info_y = p2_board_y - 100
        self.draw_player_info(player2, p2_info_x, p2_info_y)
        
        # Player 2 next piece
        p2_next_x = p2_board_x - 100
        p2_next_y = p2_board_y
        self.draw_next_piece(player2.next_piece, p2_next_x, p2_next_y)
        
        # Ranking (center top)
        ranking_x = SCREEN_WIDTH // 2 - 100
        ranking_y = 20
        self.draw_ranking([player1, player2], ranking_x, ranking_y)
        
        # VS text
        vs_text = self.font_medium.render("VS", True, WHITE)
        vs_rect = vs_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(vs_text, vs_rect)

