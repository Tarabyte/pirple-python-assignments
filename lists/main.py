"""
Homework Assignment #4: Lists

Create a global variable called myUniqueList. It should be an empty list to start.

Next, create a function that allows you to add things to that list.
Anything that's passed to this function should get added to myUniqueList,
unless its value already exists in myUniqueList.
If the value doesn't exist already, it should be added and the function should return True.
If the value does exist, it should not be added, and the function should return False;
"""

myUniqueList = []


def _exists(item, list):
    """Utility function to check if item exists in list"""
    for element in list:
        if element == item:
            return True

    return False


def add_to_unique_list(value):
    """Check if value exists in myUniqueList

    If the value exists, returns False
    If the value does not exist, pushes it to myUniqueList and returns True
    """
    if _exists(value, myUniqueList):
        return False

    myUniqueList.append(value)
    return True


myLeftovers = []


def add_to_unique_list_tracking_rejects(value):
    """Adds unique values to myUniqueList.

    Tracks rejected values by adding it to myLeftovers list
    """
    if _exists(value, myUniqueList):
        myLeftovers.append(value)
        return False

    myUniqueList.append(value)
    return True


"""
Testing
"""
print('{:^50}'.format('Testing add_to_unique_list'))
print(myUniqueList)
print(add_to_unique_list(1), myUniqueList)
print(add_to_unique_list(2), myUniqueList)
print(add_to_unique_list(1), myUniqueList)
print(add_to_unique_list(2), myUniqueList)

print('\n')
print('{:^50}'.format('Testing add_to_unique_list_tracking_rejects'))
print(myUniqueList, myLeftovers)
print(add_to_unique_list_tracking_rejects(3), myUniqueList, myLeftovers)
print(add_to_unique_list_tracking_rejects(1), myUniqueList, myLeftovers)
print(add_to_unique_list_tracking_rejects(2), myUniqueList, myLeftovers)
print(add_to_unique_list_tracking_rejects(3), myUniqueList, myLeftovers)
