def chess_board(x: int, y: int) -> list:
    matrix = []
    for i in range(y):
        row = []
        for j in range(x):
            if x * y >= 100:
                row.append("___")
            elif 100 > x * y >= 10:
                row.append("__")
            else:
                row.append("_")
        matrix.append(row)
    return matrix


def boarder_chess_board(matrix: list) -> list:
    num_cells = len(matrix) * len(matrix[0])

    for i in range(len(matrix)):
        matrix[i].insert(0, str(len(matrix) - i) + "|")
        matrix[i].append("|")
    if num_cells >= 100:
        matrix.append(["  " + str(i) for i in range(1, len(matrix[0]) - 1)])
        matrix[len(matrix) - 1].insert(0, "  ")
        boarder_length = (len(matrix[0]) - 2) * 4 + 3
    elif 100 > num_cells >= 10:
        matrix.append([" " + str(i) for i in range(1, len(matrix[0]) - 1)])
        matrix[len(matrix) - 1].insert(0, "  ")
        boarder_length = (len(matrix[0]) - 2) * 3 + 3
    else:
        matrix.append([str(i) for i in range(1, len(matrix[0]) - 1)])
        matrix[len(matrix) - 1].insert(0, "  ")
        boarder_length = (len(matrix[0]) - 2) * 2 + 3

    matrix.insert(0, " " + boarder_length * "-")
    matrix.insert(-1, " " + boarder_length * "-")

    return matrix


def valid_dimensions() -> (int, int):
    invalid_input = False
    while not invalid_input:
        try:
            x, y = map(int, input("Enter your board dimensions: ").split())
            if x < 0 or y < 0:
                print("Invalid dimensions!")
                continue
            else:
                invalid_input = True
        except ValueError:
            print("Invalid dimensions!")

    return x, y


def valid_position(matrix: list) -> (int, int):
    x = len(matrix[0])
    y = len(matrix)
    invalid_input = False
    while not invalid_input:
        try:
            num1, num2 = map(int, input("Enter the knight's starting position: ").split())
            if num1 not in range(1, x + 1) or num2 not in range(1, y + 1):
                print("Invalid position!")
                continue
            else:
                invalid_input = True
        except ValueError:
            print("Invalid position!")

    return num1, num2


def move_directions(x: int, y: int, matrix: list):
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    landing_position = []
    for i, j in moves:
        move_x = x + i
        move_y = y + j
        if 0 < move_x <= len(matrix[0]) and 0 < move_y <= len(matrix):
            landing_position.append([move_x, move_y])

    return landing_position


def main():
    dimension1, dimension2 = valid_dimensions()
    board = chess_board(dimension1, dimension2)
    start_position1, start_position2 = valid_position(board)

    if dimension1 * dimension2 >= 100:
        board[- start_position2][start_position1 - 1] = "  X"
    elif 100 > dimension1 * dimension2 >= 10:
        board[- start_position2][start_position1 - 1] = " X"
    else:
        board[- start_position2][start_position1 - 1] = "X"

    moves = move_directions(start_position1, start_position2, board)
    # print(moves)
    for h, v in moves:
        if dimension1 * dimension2 >= 100:
            board[-v][h - 1] = "  0"
        elif 100 > dimension1 * dimension2 >= 10:
            board[-v][h - 1] = " 0"
        else:
            board[-v][h - 1] = "0"

    knight_move = boarder_chess_board(board)
    print("\nHere are the possible moves:")
    for row in knight_move:
        if isinstance(row, str):
            print(row)
        else:
            print(*row)


if __name__ == "__main__":
    main()
