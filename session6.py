# Nested Loops

""""
black_square = "\u25A1"
white_square = "\u25A0"

# print(black_square)
# print(white_square)

for i in range(0, 8): # 0, 1, and 3
    # print("i is:", i)

    for j in range(0, 8): # 0, 1, 2, 3, 4
        # print(j, end=" # ")

        if i % 2 == 0:
            # print(j%2, end=" ")
            if j%2 == 0:
                print(black_square, end=" ")
            else:
                print(white_square, end=" ")
        else:
            # print((j+1)%2, end=" ")
            if (j+1)%2 == 0:
                print(black_square, end=" ")
            else:
                print(white_square, end=" ")

    print()
"""
"""
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
"""

# HW: Place King and Queen on their right positions
#     Place Knights


black_square = "\u25A1"  # Unicode for white square (□)
white_square = "\u25A0"  # Unicode for black square (■)

# Unicode chess piece symbols
pieces = {
    'R': "\u2656", 'N': "\u2658", 'B': "\u2657", 'Q': "\u2655", 'K': "\u2654", 'P': "\u2659",  # White pieces
    'r': "\u265C", 'n': "\u265E", 'b': "\u265D", 'q': "\u265B", 'k': "\u265A", 'p': "\u265F"   # Black pieces
}

# Initial positions for pieces on the chessboard
initial_positions = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

for i in range(8):  # Outer loop for rows (0 to 7)
    for j in range(8):  # Inner loop for columns (0 to 7)
        piece = initial_positions[i][j]
        
        # Print the chessboard pattern and pieces
        if piece:  # If a piece is assigned
            print(pieces[piece], end=" ")
        else:
            if i % 2 == 0:  # For even rows (0, 2, 4, 6)
                if j % 2 == 0:
                    print(black_square, end=" ")  # Print white square
                else:
                    print(white_square, end=" ")  # Print black square
            else:  # For odd rows (1, 3, 5, 7)
                if j % 2 == 0:
                    print(white_square, end=" ")  # Print black square
                else:
                    print(black_square, end=" ")  # Print white square
    print()  # Newline after each row



