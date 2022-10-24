def get_player_choice(player, rows):

    def is_choice_valid(choice, rows):
        valid = True
        if choice + 1 < 1 or choice > rows or board[0][choice] is not None:
            valid = False
        return valid

    choice = int(input(f'Player {player}, please choose a column\n')) - 1
    while not is_choice_valid(choice, rows):
        print("Invalid choice!")
        choice = int(input(f'Player {player}, please choose a column\n')) - 1
    return choice


def apply_player_choice(board, player, choice):

    row_idx = 0
    for r in range(len(board)):
        if board[r][choice] is None:
            row_idx = r
        else:
            break

    board[row_idx][choice] = player

    return row_idx


def check_win_condition(board, player, row, col, count):
    win_condition = [player] * count

    won = False

    def get_right_path(board, row, col, count):
        right_path = []
        for c in range(col, col + count):
            try:
                right_path.append(board[row][c])
            except IndexError:
                break
        return right_path

    def get_left_path(board, row, col, count):
        left_path = []
        for c in range(col, col - count, -1):
            try:
                if c < 0:
                    break
                left_path.append(board[row][c])
            except IndexError:
                break
        return left_path

    def get_up_path(board, row, col, count):
        up_path = []
        for r in range(row, row - count, -1):
            try:
                if r < 0:
                    break
                up_path.append(board[r][col])
            except IndexError:
                break
        return up_path

    def get_down_path(board, row, col, count):
        down_path = []
        for r in range(row, row + count):
            try:
                down_path.append(board[r][col])
            except IndexError:
                break
        return down_path

    def get_left_up_diagonal(board, row, col, count):
        diagonal = []

        c = col
        for r in range(row, row - count, -1):
            try:
                if r < 0 or c < 0:
                    break
                diagonal.append(board[r][c])
                c -= 1
            except IndexError:
                break

        return diagonal

    def get_right_up_diagonal(board, row, col, count):
        diagonal = []

        c = col
        for r in range(row, row - count, -1):
            try:
                if r < 0:
                    break
                diagonal.append(board[r][c])
                c += 1
            except IndexError:
                break

        return diagonal

    def get_right_down_diagonal(board, row, col, count):
        diagonal = []

        c = col
        for r in range(row, row + count):
            try:
                diagonal.append(board[r][c])
                c += 1
            except IndexError:
                break

        return diagonal

    def get_left_down_diagonal(board, row, col, count):
        diagonal = []

        c = col
        for r in range(row, row + count):
            try:
                if c < 0:
                    break
                diagonal.append(board[r][c])
                c -= 1
            except IndexError:
                break

        return diagonal

    right_path = get_right_path(board, row, col, count)
    left_path = get_left_path(board, row, col, count)
    up_path = get_up_path(board, row, col, count)
    down_path = get_down_path(board, row, col, count)
    left_up_diagonal = get_left_up_diagonal(board, row, col, count)
    right_up_diagonal = get_right_up_diagonal(board, row, col, count)
    right_down_diagonal = get_right_down_diagonal(board, row, col, count)
    left_down_diagonal = get_left_down_diagonal(board, row, col, count)

    paths = (right_path, left_path, up_path, down_path, left_down_diagonal, left_up_diagonal, right_up_diagonal, right_down_diagonal)

    for path in paths:
        if path == win_condition:
            won = True
            break

    return won


def board_creation():
    n = 6
    m = 7
    matrix = []
    for i in range(n):
        matrix.append([None]*m)

    return matrix


def print_board(board):
    def get_value(value):
        if value is None:
            return 0
        else:
            return value

    for row in board:
        print([get_value(x) for x in row])


def play(board):
    current_player, other_player = 1, 2
    win_count = 4
    rows = len(board)

    while True:
        player_choice = get_player_choice(current_player, rows)
        row_idx = apply_player_choice(board, current_player, player_choice)
        success = check_win_condition(board, current_player, row_idx, player_choice, win_count)

        print_board(board)

        if success:
            print(f"The winner is player {current_player}")
            break
        current_player, other_player = other_player, current_player


another_game = "y"

while another_game == "y":
    board = board_creation()
    play(board)

    another_game = input("Another game? y/n\n")
