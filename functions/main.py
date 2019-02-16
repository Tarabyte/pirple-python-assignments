"""
Functions Assignment
"""

# Get Song Name


def title():
    return "Yesterday"


# Get Artist Name
def artist():
    return "The Beatles"


# Get Record Date
def recordedDate():
    return (14, 'June', 1965)


# Check if the song was released the same year
def isSameYear(year):
    if year == 1965 or year == 65:
        return True
    else:
        return False


"""
Testing
"""
print('{:^60}'.format('Song Info'))
print('Song Name: {:>30}'.format(title()))
print('Artist Name: {:>30}'.format(artist()))
# wow *something acts like spread punctuator :)
print('Recorded: {:>24} {}, {}'.format(*recordedDate()))

# playing with Booleans
print(isSameYear(1965), isSameYear(1966), isSameYear(65))
