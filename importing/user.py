"""
Helper User Class
"""


class User:
    """
    Helper class to hold user data
    """

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f'{self.name} from {self.country}, {self.age} years old'
