from configuration import *


def check_initial_state_is_valid():
    if len(SUDOKU) != EXPECTED_ROW_COUNT:
        return False
    for i in range(len(SUDOKU)):
        if len(SUDOKU[i]) != EXPECTED_COLUMN_COUNT:
            return False
    for i in range(len(SUDOKU)):
        for j in range(len(SUDOKU[i])):
            if SUDOKU[i][j] > MAXIMUM_POSSIBLE_VALUE or SUDOKU[i][j] < MINIMUM_POSSIBLE_VALUE:
                if SUDOKU[i][j] != EMPTY_FIELD_MARKER:
                    return False
    return True


def print_sudoku():
    print('-------------------------------------')
    for i in range(len(SUDOKU)):
        print('|  ', end='')
        for j in range(len(SUDOKU[i])):
            print(SUDOKU[i][j], end='  ')
            if j != 0 and (j+1) % 3 == 0:
                print('|  ', end='')
        if i != 0 and (i + 1) % 3 == 0:
            print()
            print('-------------------------------------', end='')
        print()


def play_sudoku():
    if __check_is_table_filled():
        quit('YOU WIN!')
    print('Next turn...')
    print_sudoku()
    try:
        row = int(input('Give me a row number: '))
        column = int(input('Give me a column number: '))
        value = int(input('Give me the value: '))
    except ValueError:
        print('\033[91m' + 'Error! Use numbers as values.' + '\033[0m')
        print('Table not updated!')
        return
    if __check_given_value_is_possible(row, column, value):
        __update_table(row, column, value)
        print('Table updated!')
    else:
        print('Table not updated!')


def solve_sudoku():
    """
    #     Backtracking approach..
    #     """
    print('Current state:')
    print_sudoku()
    if __check_is_table_filled():
        return True
    else:
        row, column = __get_next_empty_field()
        for value in range(MINIMUM_POSSIBLE_VALUE, MAXIMUM_POSSIBLE_VALUE + 1):
            if __check_given_value_is_possible(row, column, value):
                __update_table(row, column, value)
                if solve_sudoku():
                    return True
                __delete_updated_value(row, column)
        return False


def __check_given_value_is_possible(row, column, value):
    if value > MAXIMUM_POSSIBLE_VALUE:
        print('Wrong value!')
        return False
    if row >= len(SUDOKU) or row < 0 or column >= len(SUDOKU) or column < 0:
        print('Wrong index!')
        return False
    if SUDOKU[row][column] != EMPTY_FIELD_MARKER:
        print('Area already filled!')
        return False
    if value in SUDOKU[row]:
        print('Duplicated element in row!')
        return False
    for i in range(len(SUDOKU)):
        if SUDOKU[i][column] == value:
            print('Duplicated element in column!')
            return False
    return True


def __get_next_empty_field():
    for i in range(len(SUDOKU)):
        for j in range(len(SUDOKU[i])):
            if SUDOKU[i][j] == EMPTY_FIELD_MARKER:
                return i, j


def __update_table(row, column, value):
    SUDOKU[row][column] = value


def __delete_updated_value(row, column):
    SUDOKU[row][column] = 0


def __check_is_table_filled():
    for i in range(len(SUDOKU)):
        for j in range(len(SUDOKU[i])):
            if SUDOKU[i][j] == EMPTY_FIELD_MARKER:
                return False
    return True
