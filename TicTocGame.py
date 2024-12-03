def check_winner(board):
    # check row
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return f"{row[0]} won"

    # check col
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return f"{board[0][col]} won"

    # check croner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return f"{board[0][0]} won"
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return f"{board[0][2]} won"

    # check due or not
    if all(cell != '' for row in board for cell in row):
        return 'Draw'

    return 'Game not finished'

# test
board = [['O', 'X', 'X'],
         ['X', 'X', 'O'],
         ['O', 'X', 'X']]

print(check_winner(board))