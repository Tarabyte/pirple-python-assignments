"""
Create a function that takes in two parameters: rows, and columns, both of which are integers.
The function should then proceed to draw a playing board (as in the examples from the lectures)
the same number of rows and columns as specified.

After drawing the board, your function should return True.

Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping.

If someone passes a value greater than either maximum, your function should return Talse.
"""
import os

# get terminal dimensions
MAX_COLUMNS, MAX_LINES = os.get_terminal_size()


def draw_board(rows,  columns=None):
    """Draws playing board of given size

    rows - integer Number of rows in a board
    columns - integer Number of columns in a board (Equals rows by default)

    Returns True if drawing was successful else False
    """
    # set board to be square if only one number provided
    columns = columns if columns != None else rows

    # calculate total rows and columns including separators
    columns_to_draw = 2 * columns - 1
    rows_to_draw = 2 * rows - 1

    # check max dimensions
    if columns_to_draw > MAX_COLUMNS or rows_to_draw > MAX_LINES:
        print('{}x{} is too large to fit the screen'.format(rows, columns))
        return False

    for row in range(rows_to_draw):
        # odd rows are separators
        if row % 2:
            print('-'*columns_to_draw)
            continue
        # even rows contains fields and vertical separators
        for column in range(columns_to_draw):
            print('|' if column % 2 else ' ', end='')
        # print end of line
        print('')

    return True


"""
Testing
"""
print('Testing\n')
print('{} should be True\n'.format(draw_board(3)))
print('{} should be True\n'.format(draw_board(3, 7)))

print('{} should be True\n'.format(draw_board(5)))

# Large boards
print('{} should be False\n'.format(draw_board((MAX_LINES + 1)//2 + 1, 1)))
print('{} should be False\n'.format(draw_board(1, (MAX_COLUMNS + 1)//2 + 1)))
