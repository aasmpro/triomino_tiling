import random


def draw_board(square_size, table=dict()):
    if len(table) == 0:
        for row in range(square_size):
            for column in range(square_size):
                table[row, column] = [0, False]
    for column in range(square_size):
        print(" _", end="")
    print()
    for row in range(square_size):
        for column in range(square_size):
            if table[row, column][0] == 0 or table[row, column][0] == 201 \
                    or table[row, column][0] == 211 or table[row, column][0] == 220 \
                    or table[row, column][0] == 222 or table[row, column][0] == 232:
                print("|_", end="")
            elif table[row, column][0] == 200 or table[row, column][0] == 210 \
                    or table[row, column][0] == 230:
                print("| ", end="")
            elif table[row, column][0] == 202 or table[row, column][0] == 212 \
                    or table[row, column][0] == 231:
                print(" _", end="")
            elif table[row, column][0] == 221:
                print("  ", end="")
            elif table[row, column][0] == 1:
                print("|#", end="")
        print("|")
    print()


def solve(n):
    square_size = 2 ** n
    table = dict()
    for row in range(square_size):
        for column in range(square_size):
            table[row, column] = [0, False]
    marked_square_row = random.randrange(square_size)
    marked_square_column = random.randrange(square_size)
    table[marked_square_row, marked_square_column] = [1, True]
    draw_board(square_size, table)
    recursive_solve([0, square_size - 1], [0, square_size - 1], square_size, table)
    draw_board(square_size, table)


def recursive_solve(rows, columns, square_size, table):
    if rows[1] - rows[0] == 1:
        if table[rows[0], columns[0]][1]:
            table[rows[0], columns[1]][0] = 200
            table[rows[1], columns[0]][0] = 201
            table[rows[1], columns[1]][0] = 202
        elif table[rows[0], columns[1]][1]:
            table[rows[0], columns[0]][0] = 210
            table[rows[1], columns[0]][0] = 211
            table[rows[1], columns[1]][0] = 212
        elif table[rows[1], columns[0]][1]:
            table[rows[0], columns[0]][0] = 220
            table[rows[0], columns[1]][0] = 221
            table[rows[1], columns[1]][0] = 222
        elif table[rows[1], columns[1]][1]:
            table[rows[0], columns[0]][0] = 230
            table[rows[0], columns[1]][0] = 231
            table[rows[1], columns[0]][0] = 232
        # draw_board(square_size, table) # uncomment to see how each 2x2 sub-square is solved
        # input()
        return

    max_row_number = rows[1]
    min_row_number = rows[0]
    max_column_number = columns[1]
    min_column_number = columns[0]
    sub_max_row = min_row_number + (max_row_number - min_row_number) // 2
    sub_min_row = sub_max_row + 1
    sub_max_column = min_column_number + (max_column_number - min_column_number) // 2
    sub_min_column = sub_max_column + 1
    f1 = False
    f2 = False
    f3 = False
    f4 = False
    for row in range(min_row_number, max_row_number + 1):
        for column in range(min_column_number, max_column_number + 1):
            if row <= sub_max_row and column <= sub_max_column:
                if table[row, column][1]:
                    f1 = True
            elif row <= sub_max_row and column > sub_max_column:
                if table[row, column][1]:
                    f2 = True
            elif row > sub_max_row and column <= sub_max_column:
                if table[row, column][1]:
                    f3 = True
            elif row > sub_max_row and column > sub_max_column:
                if table[row, column][1]:
                    f4 = True
    if f1:
        table[sub_max_row, sub_min_column] = [200, True]
        table[sub_min_row, sub_max_column] = [201, True]
        table[sub_min_row, sub_min_column] = [202, True]
    elif f2:
        table[sub_max_row, sub_max_column] = [210, True]
        table[sub_min_row, sub_max_column] = [211, True]
        table[sub_min_row, sub_min_column] = [212, True]
    elif f3:
        table[sub_max_row, sub_max_column] = [220, True]
        table[sub_max_row, sub_min_column] = [221, True]
        table[sub_min_row, sub_min_column] = [222, True]
    elif f4:
        table[sub_max_row, sub_max_column] = [230, True]
        table[sub_max_row, sub_min_column] = [231, True]
        table[sub_min_row, sub_max_column] = [232, True]
    # draw_board(square_size, table) # uncomment to see each step in the solution
    # input()
    recursive_solve([min_row_number, sub_max_row], [min_column_number, sub_max_column], square_size, table)
    recursive_solve([min_row_number, sub_max_row], [sub_min_column, max_column_number], square_size, table)
    recursive_solve([sub_min_row, max_row_number], [min_column_number, sub_max_column], square_size, table)
    recursive_solve([sub_min_row, max_row_number], [sub_min_column, max_column_number], square_size, table)


if __name__ == "__main__":
    print("integer from 1 to ?: ", end="")
    n = input()
    if int(n) > 0:
        solve(int(n))
    else:
        print("{} is not possible".format(n))
