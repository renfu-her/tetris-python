"""
Player class to manage individual game state
Each player has their own board, score, level, etc.
"""

import random
from .tetromino import Tetromino


class Player:
    """Represents a player in the game"""
    
    def __init__(self, player_id, board_width, board_height):
        self.player_id = player_id
        self.board_width = board_width
        self.board_height = board_height
        self.board = [[0 for _ in range(board_width)] for _ in range(board_height)]
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.current_piece = None
        self.next_piece = None
        self.game_over = False
        self.fall_time = 0
        self.fall_speed = 500  # milliseconds
        
        
        # Initialize with first pieces
        self.next_piece = self._get_random_piece()
        self.spawn_piece()
    
    def _get_random_piece(self):
        """Generate a random tetromino"""
        shapes = ['I', 'O', 'T', 'S', 'Z', 'J', 'L']
        return Tetromino(random.choice(shapes))
    
    def spawn_piece(self):
        """Spawn a new piece at the top of the board"""
        self.current_piece = self.next_piece
        self.next_piece = self._get_random_piece()
        
        # Set starting position (centered at top)
        self.current_piece.x = self.board_width // 2 - 2
        self.current_piece.y = 0
        
        # Check for game over
        if self._check_collision(self.current_piece):
            self.game_over = True
    
    def _check_collision(self, piece, dx=0, dy=0):
        """Check if piece collides with board boundaries or placed blocks"""
        blocks = piece.get_blocks()
        for bx, by in blocks:
            x = piece.x + bx + dx
            y = piece.y + by + dy
            
            # Check boundaries
            if x < 0 or x >= self.board_width or y >= self.board_height:
                return True
            
            # Check placed blocks (only check if y >= 0)
            if y >= 0 and self.board[y][x] != 0:
                return True
        
        return False
    
    def move(self, dx, dy):
        """Try to move the current piece"""
        if not self.current_piece or self.game_over:
            return False
        
        if not self._check_collision(self.current_piece, dx, dy):
            self.current_piece.x += dx
            self.current_piece.y += dy
            return True
        return False
    
    def rotate_piece(self):
        """Try to rotate the current piece"""
        if not self.current_piece or self.game_over:
            return False
        
        # 所有方块都按照自己的形状旋转
        self.current_piece.rotate()
        
        # Check collision
        if self._check_collision(self.current_piece):
            # Try wall kicks
            for dx in [-1, 1, -2, 2]:
                if not self._check_collision(self.current_piece, dx, 0):
                    self.current_piece.x += dx
                    return True
            
            # Rotation failed, revert
            self.current_piece.rotate(clockwise=False)
            return False
        
        return True
    
    def hard_drop(self):
        """Drop piece to bottom instantly"""
        if not self.current_piece or self.game_over:
            return 0
        
        drop_distance = 0
        while self.move(0, 1):
            drop_distance += 1
        
        self._lock_piece()
        return drop_distance
    
    def update(self, dt):
        """Update player state (falling pieces)"""
        if self.game_over or not self.current_piece:
            return
        
        self.fall_time += dt
        
        if self.fall_time >= self.fall_speed:
            self.fall_time = 0
            if not self.move(0, 1):
                self._lock_piece()
    
    def _lock_piece(self):
        """Lock current piece to board"""
        if not self.current_piece:
            return
        
        blocks = self.current_piece.get_absolute_blocks()
        for x, y in blocks:
            if 0 <= y < self.board_height and 0 <= x < self.board_width:
                self.board[y][x] = self.current_piece.color
        
        # Clear lines and update score
        lines_cleared = self._clear_lines()
        if lines_cleared > 0:
            self._update_score(lines_cleared)
            self._update_level()
        
        # Spawn next piece
        self.spawn_piece()
    
    def _clear_lines(self):
        """Clear completed lines and return number of lines cleared"""
        lines_to_clear = []
        
        for y in range(self.board_height):
            if all(self.board[y][x] != 0 for x in range(self.board_width)):
                lines_to_clear.append(y)
        
        # Remove cleared lines
        for y in lines_to_clear:
            del self.board[y]
            self.board.insert(0, [0 for _ in range(self.board_width)])
        
        return len(lines_to_clear)
    
    def _update_score(self, lines_cleared):
        """Update score based on lines cleared"""
        from .config import SCORE_SINGLE
        
        # 得分规则：消除的行数作为倍数
        # 消除1行：100分 × 1
        # 消除2行：100分 × 2
        # 消除3行：100分 × 3
        # 消除4行：100分 × 4
        base_score = SCORE_SINGLE * lines_cleared
        self.score += base_score * self.level
        self.lines_cleared += lines_cleared
    
    def _update_level(self):
        """Update level based on lines cleared"""
        from .config import LINES_PER_LEVEL, INITIAL_FALL_SPEED, LEVEL_SPEED_REDUCTION, MIN_FALL_SPEED
        
        new_level = (self.lines_cleared // LINES_PER_LEVEL) + 1
        if new_level > self.level:
            self.level = new_level
            self.fall_speed = max(
                INITIAL_FALL_SPEED - (self.level - 1) * LEVEL_SPEED_REDUCTION,
                MIN_FALL_SPEED
            )
    
    def add_score(self, points):
        """Add points to score (for soft/hard drop)"""
        self.score += points * self.level

