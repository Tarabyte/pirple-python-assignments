"""
Pick any library that come with Python (https://docs.python.org/3/library/) that we haven't covered in the course already.

Learn how to use the library extensively, then prepare a code sample that showcases what you've learned.
This can take any form you wish.
You could create an application with the library, or just show examples of how to use its methods.
"""
# I've decided to pick itertools
import itertools as I
# That provides a bunch of primitives to work with iterators
# and operator that provides functions for math operations
import operator as op

# Let's try local imports :)
from factorial import factorial
from zip_with import zip_with
from user import User


# Now we could use iter tools to work with iterator
first_ten = list(I.islice(factorial(), 0, 10))

print(first_ten)

# also we could use itertools.accumulate over range to make factorial generator out of ints
factorials = I.accumulate(I.count(1), func=op.mul)
first_ten = list(I.islice(factorials, 0, 10))

print(first_ten)

# lets make a list of users
users = list(zip_with(['Jim', 'Alice', 'Bob', 'Eve'], [35, 23, 30, 18], [
    'US', 'Canada', 'France', 'US'], func=User))

print(*users, sep='\n')

# lets count users from US
print(f'Users from US: {sum(map(lambda user: user.country == "US", users))}')

# print users elder than 30
print('\nElder or equal to 30', *
      I.filterfalse(lambda user: user.age < 30, users), sep='\n')

# Also it provides a way to make permutations

print(*I.permutations('ACTG', 2))
print(*I.permutations('ABC', 2))

# And combinations
print(*I.combinations('ABC', 2))
