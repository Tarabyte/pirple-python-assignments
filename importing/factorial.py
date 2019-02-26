"""
Factorial Generator
"""


def factorial():
    """Lets make factorial iterator"""
    i = 1
    fact = 1
    while True:
        yield fact
        i += 1
        fact *= i
