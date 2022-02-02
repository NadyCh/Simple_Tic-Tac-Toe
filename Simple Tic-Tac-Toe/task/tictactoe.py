def print_cells(cells):
    print('-' * 9)
    for i in range(0, 3):
        print('|' + ' ' + cells[i][0] + ' ' + cells[i][1] + ' ' + cells[i][2] + ' ' + '|')
    print('-' * 9)
    return True


def check_input(y, x, cells):
    if not x.isdigit() or not y.isdigit():
        print("You should enter numbers!")
        return False
    if x not in ['1', '2', '3'] or y not in ['1', '2', '3']:
        print("Coordinates should be from 1 to 3!")
        return False
    if cells[int(y) - 1][int(x) - 1] == 'X' or cells[int(y) - 1][int(x) - 1] == 'O':
        print("This cell is occupied! Choose another one!")
        return False
    return True


def input_cell(y, x, symb, cells):
    cells[y - 1][x - 1] = symb


def check_row(cells, symb):
    for i in range(0, 3):
        if all([cell == symb for cell in cells[i]]):
            return True
        else:
            return False


def check_diag(cells, symb):
    diag1 = [cells[0][0], cells[1][1], cells[2][2]]
    diag2 = [cells[0][2], cells[1][1], cells[2][0]]

    if all([cell == symb for cell in diag1]) or all([cell == symb for cell in diag2]):
        return True
    else:
        return False


def check_end(cells):
    if any([cell == ' ' for cell in cells[0]]) or \
            any([cell == ' ' for cell in cells[1]]) or \
            any([cell == ' ' for cell in cells[2]]):
        return False
    else:
        return True


cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print_cells(cells)
symb = "X"

while True:
    coord = input("Enter the coordinates: ").split()
    if check_input(coord[0], coord[1], cells):
        input_cell(int(coord[0]), int(coord[1]), symb, cells)
        print_cells(cells)

    if check_row(cells, symb) or check_diag(cells, symb):
        print(symb + ' wins')
        break

    if check_end(cells):
        print('Draw')
        break
    symb = ("O" if symb == "X" else "X")
