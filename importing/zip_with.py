"""
Zip With
"""
from itertools import starmap


def zip_with(*iterables, func):
    return starmap(func, zip(*iterables))
