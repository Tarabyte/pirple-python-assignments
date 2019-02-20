"""
Homework Assignment #7: Dictionaries and Sets
Return to your first homework assignments, when you described your favorite song.
Refactor that code so all the variables are held as dictionary keys and value.
Then refactor your print statements so that it's a single loop that passes through each item in the dictionary
and prints out it's key and then it's value.

Create a function that allows someone to guess the value of any key in the dictionary,
and find out if they were right or wrong.
This function should accept two parameters: Key and Value.
If the key exists in the dictionary and that value is the correct value, then the function should return true.
In all other cases, it should return false.
"""
import os

song = {
    'title': 'Yesterday',
    'artist': 'The Beatles',
    'album': 'Help!',
    'label': 'Capitol',
    'record_date': '14 June, 1965',
    'release_date': '13 September, 1965'
}

for key in song.keys():
    print('{}: {}'.format(key.replace('_', ' ').capitalize(), song[key]))


def guess(key, value):
    """Guess if given song attribute has the value specified"""
    return key in song and song[key] == value


"""
Test Game Loop
"""
columns, rows = os.get_terminal_size()
center = '\n{:^' + str(columns) + '}\n'  # centering a message

print(center.format('Welcome to guess game.'))
print('* enter ":quit" to quit the game\n\n')
while True:
    attribute = input('Which attribute do you want to guess?\n')
    if attribute == ':quit':  # special command
        break

    value = input('Guess {} value?\n'.format(attribute))

    if guess(attribute, value):
        print('\n\n', center.format('Congratulations!'))
        print('You are right! {} is {}\n\n'.format(
            attribute.capitalize(), value))
    else:
        print('Nope. Try again.\n\n')
