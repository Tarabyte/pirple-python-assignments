"""
Write a program that prints the numbers from 1 to 100.

But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz".

Instead of only printing "fizz", "buzz", and "fizzbuzz", add a fourth print statement: "prime".
"""

from math import floor, sqrt


def _is_prime(num):
    """Utility function to test number is prime"""
    for test in range(2, floor(sqrt(num)) + 1):
        if num % test == 0:
            return False

    # 1 is not prime
    return num > 1


"""
Print fizz buzz prime or number
"""
for num in range(1, 101):
    output = ''

    # assuming prime is more important than fizz and buzz
    # because both 3 and 5 are primes
    if _is_prime(num):
        output = 'Prime'
    else:
        if num % 3 == 0:
            output += 'Fizz'
        if num % 5 == 0:
            output += 'Buzz'

    # print output if available or num
    print(output if len(output) else num)
