"""
Clear Screen
"""
from os import system, name


def clear():
    """Clear screen based on current os"""
    system('cls' if name == 'nt' else 'clear')
