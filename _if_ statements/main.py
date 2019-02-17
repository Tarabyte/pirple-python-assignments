"""Homework Assignment #3: "If" Statements

Create a function that accepts 3 parameters and checks for equality between any two of them.
"""


def hasEqual(a, b, c):
    # convert arguments to ints
    a = int(a)
    b = int(b)
    c = int(c)

    # This could be a one liner return a == b or b == c or a == c

    # compare all pairs
    if a == b or a == c or b == c:
        return True
    # no pairs found
    return False


# Testing
print(hasEqual(1, 2, 3), False)
print(hasEqual(1, 1, 3), True)
print(hasEqual(1, 2, 1), True)
print(hasEqual(1, 2, 2), True)

print(hasEqual('1', '2', '3'), False)
print(hasEqual(1, '1', 3), True)
print(hasEqual(1, 2, '1'), True)
print(hasEqual(1, '2', 2), True)
