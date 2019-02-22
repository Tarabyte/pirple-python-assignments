"""
Homework Assignment #8: Input and Output (I/O)


Create a note-taking program. When a user starts it up, it should prompt them for a filename.

If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file.
After they enter the text, it should save the file and exit.

If they enter a file name that already exists, it should ask the user if they want:

A) Read the file

B) Delete the file and start over

C) Append the file

If the user wants to read the file it should simply show the contents of the file on the screen.
If the user wants to start over then the file should be deleted and another empty one made in its place.
If a user elects to append the file, then they should be able to enter more text, and that text should be
added to the existing text in the file.

Allow the user to select a 4th option:

D) Replace a single line

If the user wants to replace a single line in the file, they will then need to be prompted for 2 bits of information:

1) The line number they want to update.

2) The text that should replace that line.
"""
import os

# Logic
DIR = 'notes'
# create a directory
if not os.path.exists(DIR):
    os.mkdir(DIR)


def get_file_path(note):
    """Get note file path by note name"""
    return os.path.join(DIR, note)


def get_note_name(file):
    """Get note name from file path"""
    _, name = os.path.split(file)
    return name


def collect_lines(file_descriptor):
    """Collects user input lines and writes it to a file"""
    while True:
        line = input('Enter text line: \n')
        if not line:
            break

        file_descriptor.write(line)
        file_descriptor.write('\n')


def create_note(file_name):
    """
    Prompt user to enter file contents line by line

    file_name - string, file name to be created
    """
    with open(file_name, 'w') as note:
        print('Enter note line by line (or press enter to quit)')
        collect_lines(note)

    # should quit
    return False


def print_help():
    """Prints available operations"""
    operation_help = '{:<10} - {}'
    print(operation_help.format('(R)ead', 'Read the file'))
    print(operation_help.format('(D)elete', 'Delete the file and start over'))
    print(operation_help.format('(A)ppend', 'Append the file'))
    print(operation_help.format('(L)ine', 'Replace a single line'))


def read_note(file_name):
    """Prints file contents on a screen"""
    with open(file_name) as note:
        print('Note: {}'.format(get_note_name(file_name)))
        for line in note:
            print(' ', line, end='')
    return True


def remove_note(file_name):
    """Removes file after user confirmation"""
    while True:
        answer = input(
            'Are you sure you want to delete {}? (yes/no): '.format(get_note_name(file_name))).lower()

        if answer == 'no':
            return True
        if answer == 'yes':
            os.remove(file_name)
            # recreate a note
            return create_note(file_name)

        print('Please answer yes/no')


def edit_note(file_name):
    """Adds more text to existing note"""
    with open(file_name, 'a') as note:
        print('Enter more notes line by line (or press enter to quit)')
        collect_lines(note)
    return True


def replace_line(file_name):
    """Replace line by line number"""
    line_number = int(input('Enter line number: '))

    # assuming the file is small
    # read it to memory
    lines = []
    with open(file_name) as note:
        lines += note

    if line_number > len(lines):
        print('There is no line {}'.format(line_number))
    else:
        line_content = input('Enter text line\n')
        # replace line by number (assuming user lines are one based)
        lines[line_number - 1] = line_content + '\n'

        # write new contents
        with open(file_name, 'w') as note:
            note.write(''.join(lines))

    return True


operations = {
    "read": read_note,
    "r": read_note,
    "delete": remove_note,
    "d": remove_note,
    "append": edit_note,
    "a": edit_note,
    "line": replace_line,
    "l": replace_line
}


def run_operation(operation, file_name):
    """
    Run operation on file based on operation name
    """
    if operation in operations:
        return operations[operation](file_name)

    print('Unknown operation: {}'.format(operation))
    return False


# Program loop
print('Welcome to notes\n')
while True:
    note_name = input('Please enter note name: ')

    if not note_name:
        break

    file_name = get_file_path(note_name)
    exists = os.path.isfile(file_name)

    # Should we keep running
    keep_running = True

    # Handle existing note
    if exists:
        print('{} already exists. What do you want to do to it?'.format(file_name))
        print_help()

        # get the operation name
        operation = input('> ').lower()

        # run the operation and continue
        keep_running = run_operation(operation,  file_name)
    else:
        keep_running = create_note(file_name)

    if not keep_running:
        break
