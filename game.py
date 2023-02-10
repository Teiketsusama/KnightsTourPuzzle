def chess_board():
    matrix = []
    for i in range(9):
        row = []
        if i <= 7:
            for j in range(10):
                if j == 0:
                    row.append(str(8 - i) + "|")
                elif j == 9:
                    row.append("|")
                else:
                    row.append("_")
        elif i == 8:
            for j in range(10):
                if j == 0:
                    row.append("  ")
                elif j == 9:
                    row.append("  ")
                else:
                    row.append(j)
        matrix.append(row)
    matrix.insert(0, " -------------------")
    matrix.insert(-1, " -------------------")

    return matrix


def valid_input():
    invalid_input = False
    while not invalid_input:
        try:
            num1, num2 = map(int, input("Enter the knight's starting position: ").split())
            if num1 not in range(1, 9) or num2 not in range(1, 9):
                print("Invalid dimensions!")
                continue
            else:
                invalid_input = True
        except ValueError:
            print("Invalid dimensions!")

    return num1, num2


def main():
    start_position1, start_position2 = valid_input()
    knight_move = chess_board()
    knight_move[- start_position2 - 2][start_position1] = "X"
    for row in knight_move:
        if isinstance(row, str):
            print(row)
        else:
            print(*row)


if __name__ == "__main__":
    main()
