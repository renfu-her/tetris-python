"""
Tetromino piece definitions and rotation logic
Contains all 7 standard Tetris pieces
"""

from .config import COLORS

# Tetromino shapes defined as 4x4 grids
SHAPES = {
    'I': [
        ['.....',
         '..#..',
         '..#..',
         '..#..',
         '..#..'],
        ['.....',
         '.....',
         '####.',
         '.....',
         '.....'],
    ],
    'O': [
        ['.....',
         '.....',
         '.##..',
         '.##..',
         '.....'],
    ],
    'T': [
        ['.....',
         '.....',
         '.#...',
         '###..',
         '.....'],
        ['.....',
         '.....',
         '.#...',
         '.##..',
         '.#...'],
        ['.....',
         '.....',
         '.....',
         '###..',
         '.#...'],
        ['.....',
         '.....',
         '.#...',
         '##...',
         '.#...'],
    ],
    'S': [
        ['.....',
         '.....',
         '.##..',
         '##...',
         '.....'],
        ['.....',
         '.....',
         '.#...',
         '.##..',
         '..#..'],
    ],
    'Z': [
        ['.....',
         '.....',
         '##...',
         '.##..',
         '.....'],
        ['.....',
         '.....',
         '..#..',
         '.##..',
         '.#...'],
    ],
    'J': [
        ['.....',
         '.....',
         '.#...',
         '.#...',
         '##...'],
        ['.....',
         '.....',
         '.....',
         '###..',
         '..#..'],
        ['.....',
         '.....',
         '.##..',
         '.#...',
         '.#...'],
        ['.....',
         '.....',
         '#....',
         '###..',
         '.....'],
    ],
    'L': [
        ['.....',
         '.....',
         '.#...',
         '.#...',
         '.##..'],
        ['.....',
         '.....',
         '.....',
         '..#..',
         '###..'],
        ['.....',
         '.....',
         '##...',
         '.#...',
         '.#...'],
        ['.....',
         '.....',
         '###..',
         '#....',
         '.....'],
    ],
}


class Tetromino:
    """Represents a Tetromino piece"""
    
    def __init__(self, shape_type):
        self.shape_type = shape_type
        self.color = COLORS[shape_type]
        self.rotations = SHAPES[shape_type]
        self.rotation_index = 0
        self.x = 0
        self.y = 0
    
    def get_shape(self):
        """Get current rotation of the piece"""
        return self.rotations[self.rotation_index]
    
    def rotate(self, clockwise=True):
        """Rotate the piece"""
        if clockwise:
            self.rotation_index = (self.rotation_index + 1) % len(self.rotations)
        else:
            self.rotation_index = (self.rotation_index - 1) % len(self.rotations)
    
    def get_blocks(self):
        """Get list of (x, y) positions relative to piece position"""
        shape = self.get_shape()
        blocks = []
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell == '#':
                    blocks.append((x, y))
        return blocks
    
    def get_absolute_blocks(self):
        """Get list of (x, y) positions in board coordinates"""
        blocks = self.get_blocks()
        return [(self.x + bx, self.y + by) for bx, by in blocks]
    
    def copy(self):
        """Create a copy of this tetromino"""
        new = Tetromino(self.shape_type)
        new.rotation_index = self.rotation_index
        new.x = self.x
        new.y = self.y
        return new

