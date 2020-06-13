from game import *

print("-------------Start-------------")

if not check_initial_state_is_valid():
    quit('Something wrong with the initial configuration.')

command = input('solve (s) or game (g)?\n')
if command == 's':
    if solve_sudoku():
        print('Solution:')
        print_sudoku()
    else:
        print('Impossible to solve.')
elif command == 'g':
    while True:
        play_sudoku()
else:
    quit('Invalid command. Exit...')

print("-------------END-------------")
