# 1.This section has input validation functions that check user input and prevent invalid data
# Checks if the user has entered a valid chessboard coordinate (a3, d4) therefore ensures the program only accepts real chessboard positions
def is_valid_position(coord):
    if len(coord) != 2:
        return False
    col = coord[0]
    row = coord[1]
    return col in "abcdefgh" and row in "12345678"

#2. This section has coordinate converters that switch between chess and grid formats
# Convert chess coordinates like a1 to numerical indices like (0,0) used in an 8x8 gird
# This makes it easy for the program to do math with board positions of d4, h8, c2 since arrays use numbers and not letters.
def coordinate_to_indices(coord):
    col = ord(coord[0]) - ord('a')  # a=0, b=1, etc.
    row = 8 - int(coord[1])  # 8=0, 7=1, etc. (top to bottom)
    return (row, col)

# This returns the list of valid piece types
# It also checks that the user typed a real chess piece eg pawn instead of pown
def get_valid_pieces():
    return ["pawn", "rook", "knight", "bishop", "queen", "king"]

# This one makes user input easy to handle therefore it separates the piece name and its position for validation like knight b4 
def parse_piece_input(user_input):
    parts = user_input.lower().split()
    if len(parts) != 2:
        return None, None
    piece = parts[0]
    coord = parts[1]
    return piece, coord

# It check if piece and coordinate are valid therefore preventing bad input that could confuse the program.
def validate_piece_input(piece, coord):
    if piece not in get_valid_pieces():
        return False
    if not is_valid_position(coord):
        return False
    return True

# This section handles piece movement functions that define how each piece moves
# These get functions determine which squares a piece can attack based on its movement rules. 
# Calculates all potential attack squares for pawns.
# White pawns attack diagonally upward
def get_pawn_targets(row, col):
    targets = []
    if row > 0:
        if col > 0:
            targets.append((row - 1, col - 1))
        if col < 7:
            targets.append((row - 1, col + 1))
    return targets

# This return positions a rook can attack
# Helps identify any black piece in the same row or column.
def get_rook_targets(row, col):
    targets = []
# Horizontal and vertical lines
    for i in range(8):
        if i != col:
            targets.append((row, i))
        if i != row:
            targets.append((i, col))
    return targets

# Detects all positions a knight could capture from.
# Return positions a knight can attack
def get_knight_targets(row, col):
    targets = []
    # Knight moves in an L-shaped way; 2 squares in one direction, 1 in perpendicular
    moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            targets.append((new_row, new_col))
    return targets

# This one moves diagonally
# Checks all diagonal lines for targets.
# Return positions a bishop can attack
def get_bishop_targets(row, col):
    targets = []
# Diagonal lines
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        while 0 <= new_row < 8 and 0 <= new_col < 8:
            targets.append((new_row, new_col))
            new_row += dr
            new_col += dc
    return targets

# Queen combines rook + bishop movements. 
# Simplifies queen logic using the other two functions.
def get_queen_targets(row, col):
# Return positions a queen can attack (rook + bishop)
    return get_rook_targets(row, col) + get_bishop_targets(row, col)

# King moves one step in any direction.
def get_king_targets(row, col):
# Return positions a king can attack
    targets = []
# King moves one square in any direction
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                targets.append((new_row, new_col))
    return targets

#4. This section handles the attacks and finds capturable pieces
# Gets all positions a piece can attack
# Calls the right attack function depending on the piece.
def get_attack_positions(piece, row, col):
    if piece == "pawn":
        return get_pawn_targets(row, col)
    elif piece == "rook":
        return get_rook_targets(row, col)
    elif piece == "knight":
        return get_knight_targets(row, col)
    elif piece == "bishop":
        return get_bishop_targets(row, col)
    elif piece == "queen":
        return get_queen_targets(row, col)
    elif piece == "king":
        return get_king_targets(row, col)
    return []

# Converts numerical indices back to chessboard notation like a5
def indices_to_coordinate(row, col):
    """Convert array indices back to chess coordinate"""
    coord_col = chr(ord('a') + col)
    coord_row = str(8 - row)
    return coord_col + coord_row

# Main program
print("=== Chess Piece Capture Analyzer ===\n")

# Get white piece
while True:
# Keeps asking until valid input is given and defines the attacking piece
    white_input = input("Enter white piece and position (e.g., 'knight a5'): ")
    white_piece, white_coord = parse_piece_input(white_input)
    
    if white_piece is None or white_coord is None:
        print("Error: Invalid format. Please use 'piece coordinates'.\n")
        continue
    
    if not validate_piece_input(white_piece, white_coord):
        print(f"Error: Invalid piece or coordinates. Valid pieces: {', '.join(get_valid_pieces())}\n")
        continue
    
    break

white_row, white_col = coordinate_to_indices(white_coord)
occupied_positions = set()
occupied_positions.add((white_row, white_col))

# Get black pieces
# This one allows multiple black pieces to be added, checks for duplicates, and validates input.
black_pieces = []

print("\nAdd black pieces (type 'done' when finished, minimum 1 piece required):\n")

while True:
    black_input = input(f"Enter black piece {len(black_pieces) + 1} (or 'done' to finish): ")
    
    if black_input.lower() == "done":
        if len(black_pieces) < 1:
            print("Error: You must add at least one black piece.\n")
            continue
        break
    
    black_piece, black_coord = parse_piece_input(black_input)
    
    if black_piece is None or black_coord is None:
        print("Error: Invalid format. Please use 'piece coordinates'.\n")
        continue
    
    if not validate_piece_input(black_piece, black_coord):
        print(f"Error: Invalid piece or coordinates.\n")
        continue
    
    black_row, black_col = coordinate_to_indices(black_coord)
    
    if (black_row, black_col) in occupied_positions:
        print("Error: A piece already exists at that position.\n")
        continue
    
    occupied_positions.add((black_row, black_col))
    black_pieces.append((black_piece, black_coord, black_row, black_col))
    print(f"Added {black_piece} at {black_coord}\n")

# Find capturable pieces
print("\n=== Analysis ===\n")

# Calculates all squares the white piece can attack and compares them to black piece positions.
# This determines which black pieces can be captured.
attack_positions = get_attack_positions(white_piece, white_row, white_col)
capturable = []

for black_piece, black_coord, black_row, black_col in black_pieces:
    if (black_row, black_col) in attack_positions:
        capturable.append((black_piece, black_coord))

#5. This section handles the display results
# This shows the result of the analysis clearly
if len(capturable) == 0:
    print("No black pieces can be captured.")
else:
    print(f"The white {white_piece} at {white_coord} can capture:")
    for piece, coord in capturable:
        print(f"  - {piece} at {coord}")

print("\n=== Game Over ===")

