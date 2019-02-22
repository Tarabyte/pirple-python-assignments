from termcolor import colored, cprint
import sys
"""
Project #1: A Simple Game
In this project, your task is create a Connect 4 game in Python.
"""
import os
from colorama import init
from termcolor import colored

# enable coloring on windows
init()
os.system('color 0')


def _matrix(n, m, value=None):
    """Utility function to create n x m matrix of a given value"""
    el = value if callable(value) else lambda i, j: value

    matrix = []
    for i in range(n):
        row = []
        matrix.append(row)
        for j in range(m):
            row.append(el(i, j))

    return matrix


def _index_of(elements, value):
    """Get index of value in iterable. Defaults to -1 if not found"""

    for index, item in enumerate(elements):
        if item == value:
            return index
    return -1


def draw_board(columns, first='X', second='O', empty=' '):
    """
    Prints a connect 4 game board using columns config and player marks.
    """
    cols_number = len(columns)
    rows_number = len(columns[0])
    top = '┌─' + '─┬─'.join('─'*cols_number) + '─┐'
    header = '| ' + \
        ' | '.join([str(i) for i in range(1, cols_number + 1)]) + ' |'
    separator = '├─' + '─┼─'.join('─'*cols_number) + '─┤'
    bottom = '└─' + '─┴─'.join('─'*cols_number) + '─┘'

    print(top)
    print(header)
    print(separator)

    # convert columns to rows
    def transpose(i, j): return columns[j][rows_number - i - 1]
    rows = _matrix(rows_number, cols_number, value=transpose)

    # print symbol by cell value
    def symbol(value):
        if value == None:
            return empty
        if value == 1:
            return second
        return first

    # print rows
    for index, row in enumerate(rows):
        if index:
            print(separator)

        print('|' + '|'.join([f' {symbol(cell)} ' for cell in row]) + '|')

    print(bottom)


def move(column, player):
    """Apply player move to the given column"""
    index = _index_of(column, None)

    if index < 0:
        print('Entire column is occupied')
        return False

    column[index] = player
    return True


def get_winner(columns):
    """Check if columns has winner and return one."""
    cols_count = len(columns)
    rows_count = len(columns[0])

    def _same(a, b, c, d):
        return a != None and a == b and b == c and c == d

    # check vertical
    for col in range(cols_count):
        for row in range(rows_count - 3):
            if _same(columns[col][row], columns[col][row + 1], columns[col][row + 2], columns[col][row + 3]):
                return columns[col][row]

    # check horizontal
    for col in range(cols_count - 3):
        for row in range(rows_count):
            if _same(columns[col][row], columns[col + 1][row], columns[col + 2][row], columns[col + 3][row]):
                return columns[col][row]

    # check diagonal ltr
    for col in range(cols_count - 3):
        for row in range(rows_count - 3):
            if _same(columns[col][row], columns[col + 1][row + 1], columns[col + 2][row + 2], columns[col + 3][row + 3]):
                return columns[col][row]

    # check diagonal rtl
    for col in range(3, cols_count):
        for row in range(rows_count - 3):
            if _same(columns[col][row], columns[col - 1][row + 1], columns[col - 2][row + 2], columns[col - 3][row + 3]):
                return columns[col][row]

    return None


def game():
    """
    Game Loop
    """
    print('Welcome to Connect 4 Game', )
    player = 0
    columns = _matrix(7, 6)
    player1 = colored(u'\u2B24', 'red')
    player2 = colored(u'\u2B24', 'green')

    def redraw():
        return draw_board(columns, first=player1, second=player2)

    players = [
        input(f'Player I: '),
        input(f'Player II: ')
    ]

    while True:
        redraw()
        command = input(f'Player {players[player]} enter column: ')

        if command == 'quit' or command == 'q':
            print('Bye!')
            break

        column = int(command)
        if column < 1 or column > len(columns):
            print('Please select correct column number')
            continue

        if move(columns[column - 1], player):
            winner = get_winner(columns)

            if winner != None:
                redraw()
                print(f'Player {players[player]} wins!')

                return

            # change player
            player = [1, 0][player]


game()
