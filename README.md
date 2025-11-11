# Tetris Game

A classic Tetris game implementation built with Python and Pygame, featuring single-player and two-player modes, high score tracking, and progressive difficulty levels.

## Features

- 🎮 **Single Player Mode** - Classic Tetris gameplay
- 👥 **Two Player Mode** - Compete side-by-side with a friend
- 🏆 **High Score System** - Track and display top 10 scores
- 📈 **Progressive Difficulty** - Speed increases as you level up
- 🎨 **Classic Tetrominoes** - All 7 standard pieces (I, O, T, S, Z, J, L)
- 👻 **Ghost Piece Preview** - Visual guide showing where pieces will land
- 🎯 **Wall Kick Mechanics** - Smooth rotation near walls
- ⚡ **Hard Drop** - Instantly drop pieces to the bottom

## Requirements

- Python 3.7 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer
- Pygame 2.5.0 or higher

## Installation

1. Install `uv` (if not already installed):
```bash
# On Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repository:
```bash
git clone <repository-url>
cd tetris
```

3. Install dependencies from `pyproject.toml`:
```bash
uv pip install -e .
```

This will install the project and all dependencies (including pygame) defined in `pyproject.toml`.

## How to Run

Run the game using `uv run`:
```bash
uv run main.py
```

`uv run` automatically manages the virtual environment and ensures all dependencies are available.

## Controls

### Player 1 (Single Player Mode)
- **←** / **→** - Move left/right
- **↓** - Hard drop (instant drop to bottom)
- **↑** - Rotate piece
- **SPACE** - Hard drop (alternative)

### Player 2 (Two Player Mode)
- **A** / **D** - Move left/right
- **S** - Hard drop (instant drop to bottom)
- **W** - Rotate piece
- **Q** - Hard drop (alternative)

### Menu Navigation
- **↑** / **↓** - Navigate menu options
- **ENTER** / **SPACE** - Select option
- **ESC** - Return to menu (from rankings or game over screen)

## Game Rules

- Clear horizontal lines to score points
- Each level requires clearing 10 lines to advance
- Game speed increases with each level
- Score multiplier increases with level
- Game ends when pieces reach the top of the board

### Scoring System
- **1 line cleared**: 100 × level points
- **2 lines cleared**: 200 × level points
- **3 lines cleared**: 300 × level points
- **4 lines cleared (Tetris)**: 400 × level points

## Project Structure

```
tetris/
├── app/
│   ├── __init__.py
│   ├── config.py          # Game configuration and constants
│   ├── game.py            # Main game logic
│   ├── menu.py            # Menu system
│   ├── player.py          # Player state management
│   ├── ranking.py         # High score system
│   ├── tetromino.py       # Tetromino piece definitions
│   └── ui.py              # User interface rendering
├── main.py                # Entry point
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Project metadata
└── high_scores.json       # High score storage (auto-generated)
```

## Game Modes

### Single Player
Play solo and try to beat your high score. Your best scores are automatically saved to the rankings.

### Two Player
Compete against a friend on the same screen. Each player has their own board and controls. See who can last longer or score higher!

## High Scores

The game automatically tracks your top 10 high scores, including:
- Final score
- Level reached
- Lines cleared

View rankings from the main menu or after completing a single-player game.

## Technical Details

- **Screen Resolution**: 1200×800 pixels
- **Board Size**: 10×20 cells
- **Frame Rate**: 60 FPS
- **Initial Fall Speed**: 500ms per cell
- **Speed Reduction**: 50ms per level
- **Minimum Fall Speed**: 50ms per cell

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Acknowledgments

Built with [Pygame](https://www.pygame.org/) - a cross-platform set of Python modules designed for writing video games.

