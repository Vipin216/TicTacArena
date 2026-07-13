def is_cell_empty(board, row, col):
    return board[row][col] == ""


def make_move(board, row, col, symbol):
    board[row][col] = symbol
    return board


def check_winner(board):

    # Rows
    for row in board:
        if row[0] != "" and row[0] == row[1] == row[2]:
            return row[0]

    # Columns
    for col in range(3):
        if (
            board[0][col] != ""
            and board[0][col] == board[1][col] == board[2][col]
        ):
            return board[0][col]

    # Main diagonal
    if (
        board[0][0] != ""
        and board[0][0] == board[1][1] == board[2][2]
    ):
        return board[0][0]

    # Secondary diagonal
    if (
        board[0][2] != ""
        and board[0][2] == board[1][1] == board[2][0]
    ):
        return board[0][2]

    return None



def is_draw(board):

    for row in board:
        for cell in row:
            if cell == "":
                return False

    return True