# Chess Piece Capture Analyzer
A Python program that analyzes chess positions and determines which black pieces can be captured by a white piece based on standard chess movement rules.
The program accepts user input, validates it, converts positions between grid/chess notation, and outputs all black pieces that are in the attack range of the white piece.


## Features
* Validates chess coordinates like `a3`, `d4`, `h8`
* Validates chess piece names to prevent bad input
* Converts chess positions (e.g., `a1`) to numeric grid indices for calculations

* Implements full movement logic for:
  * Pawn
  * Rook
  * Knight
  * Bishop
  * Queen
  * King
* Supports adding multiple black pieces with duplicate-position protection
* Returns all black pieces that can be captured by the chosen white piece


## How It Works
### 1. **Input Validation**
The program ensures:
* Coordinates follow real chessboard format (`a–h` and `1–8`)
* Piece names are valid chess pieces (e.g., `knight`, not `kight`)
* User input format is correct (e.g., `"rook a4"`)

Key functions:
* `is_valid_position(coord)`
* `get_valid_pieces()`
* `validate_piece_input(piece, coord)`
* `parse_piece_input(user_input)`


### 2. **Coordinate Conversion**
Chess notation → Array indices
Array indices → Chess notation

Used so movement rules can be calculated using numbers.

Functions:
* `coordinate_to_indices(coord)`
* `indices_to_coordinate(row, col)`


### 3. **Piece Movement Logic**
Each chess piece has its own movement definition:

| Piece  | Function             | Movement Handled            |
| ------ | -------------------- | --------------------------- |
| Pawn   | `get_pawn_targets`   | Diagonal captures           |
| Rook   | `get_rook_targets`   | Horizontal + vertical lines |
| Knight | `get_knight_targets` | L-shaped jumps              |
| Bishop | `get_bishop_targets` | Diagonal sliding            |
| Queen  | `get_queen_targets`  | Rook + Bishop combined      |
| King   | `get_king_targets`   | One step in any direction   |

The function:
get_attack_positions(piece, row, col)
automatically picks the correct movement rules.


### 4. **Capture Detection**
The program:
* Computes all attackable squares of the white piece
* Compares them with all black piece coordinates
* Lists every black piece that can be captured

## Example Usage
When you run the program, it will:
1. Ask for a white piece position

   Enter white piece and position (e.g., 'knight a5'):
   
2. Ask for black pieces (any number)

   Enter black piece 1 (or 'done'):
   
3. Show the results
   The white knight at a5 can capture:
     – pawn at b7
     – bishop at c4


## Project Structure
│-- chess.py
│-- README.md

## Running the Program
Make sure you are in the project folder, then run
python chess.py

##  Future Improvements
* Add a real chessboard visualizer
* Add support for blocked squares (piece obstruction)
* Add a GUI version
* Add unit tests for all movement functions

## License
This project is free to use, modify, and learn from.

