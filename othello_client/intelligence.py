import random

def is_valid_move(board, player, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    if board[row][col] != 0:
        return False

    opponent = -player

    for direction in directions:
        dr, dc = direction
        r, c = row + dr, col + dc
        found_opponent = False

        while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            r += dr
            c += dc
            found_opponent = True

        if found_opponent and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
            return True

    return False

def valid_moves(board, player):
    valid_moves = []
    for row in range(8):
        for col in range(8):
            if is_valid_move(board, player, row, col):
                valid_moves.append((row, col))

    return valid_moves

def AI_MOVE(board, player):
    # row = random.randint(0, 7)
    # col = random.randint(0, 7)
    _valid_moves = valid_moves(board, player)
    row, col = random.choice(_valid_moves)
    return (row, col)
