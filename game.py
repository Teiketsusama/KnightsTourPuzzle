def valid_dimensions() -> (int, int):
    invalid_input = False
    while not invalid_input:
        try:
            dim_x, dim_y = map(int, input("Enter your board dimensions: ").split())
            if dim_x <= 0 or dim_y <= 0:
                print("Invalid dimensions!")
                continue
            else:
                invalid_input = True
        except ValueError:
            print("Invalid dimensions!")

    return dim_x, dim_y


def input_position_to_board_position(input_position, dim_y):
    return input_position[0] - 1, dim_y - input_position[1]


def valid_position(dim_x: int, dim_y: int) -> (int, int):
    invalid_input = False
    while not invalid_input:
        try:
            input_x, input_y = map(int, input("Enter the knight's starting position: ").split())
            input_x, input_y = input_position_to_board_position((input_x, input_y), dim_y)
            if input_x not in range(0, dim_x) or input_y not in range(0, dim_y):
                print("Invalid position!")
                continue
            else:
                invalid_input = True
        except ValueError:
            print("Invalid position!")

    return input_x, input_y


# The knight moves in an L-shape, so it has to move 2 squares horizontally and 1 square vertically,
# or 2 squares vertically and 1 square horizontally.
# Check all 8 possible moving directions from the starting position.
def generate_possible_move_positions(input_x: int, input_y: int, dim_x: int, dim_y: int, visited_positions: list) -> list:
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    positions = []
    for i, j in moves:
        move_x = input_x + i
        move_y = input_y + j
        if 0 <= move_x < dim_x and 0 <= move_y < dim_y:
            positions.append((move_x, move_y))

    possible_positions = []
    for p in positions:
        if p not in visited_positions:
            possible_positions.append(p)

    return possible_positions


def explore_board(current_position: tuple, dim_x: int, dim_y: int, visited_positions: list):
    visited_positions.append(current_position)
    possible_moves = generate_possible_move_positions(current_position[0], current_position[1], dim_x, dim_y, visited_positions)

    if len(visited_positions) == dim_x * dim_y:
        return visited_positions

    for move in possible_moves:
        if explore_board(move, dim_x, dim_y, visited_positions):
            return visited_positions

    visited_positions.pop()
    return False


def print_chess_board(dim_x: int, dim_y: int, current_position: tuple, visited_positions: list,
                      possible_move_positions: list, show_move_order=False):
    num_cells = dim_x * dim_y

    if num_cells >= 100:
        boarder_length = dim_x * 4 + 3
        cell_length = 3
    elif 100 > num_cells >= 10:
        boarder_length = dim_x * 3 + 3
        cell_length = 2
    else:
        boarder_length = dim_x * 2 + 3
        cell_length = 1

    print(" " + boarder_length * "-")

    for y in range(dim_y):
        board_x_strs = [str(dim_y - y) + "|"]
        for x in range(dim_x):
            if (x, y) == current_position:
                board_x_strs.append(((cell_length - 1) * " ") + "X")
            elif (x, y) in visited_positions:
                if show_move_order:
                    move_order = visited_positions.index((x, y)) + 1
                    board_x_strs.append(str(move_order).rjust(cell_length, " "))
                else:
                    board_x_strs.append(((cell_length - 1) * " ") + "*")
            elif (x, y) in possible_move_positions:
                next_possible_move_positions = generate_possible_move_positions(x, y, dim_x, dim_y, visited_positions)
                board_x_strs.append(((cell_length - 1) * " ") + str(len(next_possible_move_positions) - 1))

            else:
                board_x_strs.append(cell_length * "_")
        board_x_strs.append("|")

        print(*board_x_strs)

    print(" " + boarder_length * "-")

    board_x_strs = [(" " * (cell_length - 1)) + str(i) for i in range(1, dim_x + 1)]
    board_x_strs.insert(0, "  ")
    print(*board_x_strs)


def valid_move(dim_x: int, dim_y: int, visited_positions: list, possible_move_positions: list) -> (int, int):
    invalid_input = False
    while not invalid_input:
        try:
            move_x, move_y = map(int, input("Enter your next move: ").split())
            move_x, move_y = input_position_to_board_position((move_x, move_y), dim_y)
            if move_x not in range(0, dim_x) or move_y not in range(0, dim_y):
                print("Invalid move!", end=" ")
                continue
            elif (move_x, move_y) in visited_positions:
                print("Invalid move!", end=" ")
                continue
            elif (move_x, move_y) not in possible_move_positions:
                print("Invalid move!", end=" ")
                continue
            else:
                invalid_input = True
        except ValueError:
            print("Invalid move!", end=" ")

    return move_x, move_y


def play_knight_moves(input_x: int, input_y: int, dim_x: int, dim_y: int, visited_positions: list):

    while True:
        possible_move_positions = generate_possible_move_positions(input_x, input_y, dim_x, dim_y, visited_positions)

        left_positions = dim_x * dim_y - len(visited_positions)
        if left_positions > 0:
            if not possible_move_positions:
                print("No more possible moves!")
                print("Your knight visited {} squares!".format(len(visited_positions)))
                break
        elif left_positions == 0:
            print("What a great tour! Congratulations!")
            break

        next_x, next_y = valid_move(dim_x, dim_y, visited_positions, possible_move_positions)
        current_position = (next_x, next_y)
        next_possible_move_positions = generate_possible_move_positions(next_x, next_y, dim_x, dim_y, visited_positions)
        print_chess_board(dim_x, dim_y, current_position, visited_positions, next_possible_move_positions, False)

        input_x, input_y = next_x, next_y
        visited_positions.append((input_x, input_y))


def main():
    dim_x, dim_y = valid_dimensions()
    input_x, input_y = valid_position(dim_x, dim_y)
    current_position = (input_x, input_y)
    visited_positions = []

    invalid_input = False
    while not invalid_input:
        user_input = input("Do you want to try the puzzle? (y/n): ")
        if user_input not in ("y", "n"):
            print("Invalid input!")
            continue
        else:
            invalid_input = True

    if user_input == "y":
        if not explore_board(current_position, dim_x, dim_y, visited_positions):
            print("No solution exists!")
        else:
            visited_positions = []
            possible_move_positions = generate_possible_move_positions(current_position[0], current_position[1], dim_x,
                                                                       dim_y, visited_positions)
            print_chess_board(dim_x, dim_y, current_position, visited_positions, possible_move_positions, False)
            visited_positions.append(current_position)
            play_knight_moves(input_x, input_y, dim_x, dim_y, visited_positions)
    else:
        if not explore_board(current_position, dim_x, dim_y, visited_positions):
            print("No solution exists!")
        else:
            visited_positions = []
            solution = explore_board(current_position, dim_x, dim_y, visited_positions)
            print("Here's the solution!")
            print_chess_board(dim_x, dim_y, (), solution, [], True)


if __name__ == "__main__":
    main()
