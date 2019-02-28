"""
For this assignment you can choose any of the homeworks or projects you've done so far.
Pick a function that you know is particularly problematic and add try/except/finally cases to it so that it can
handle the errors more gracefully.
"""
from math import floor, sqrt, pi


def _is_prime(num):
    """Utility function to test number is prime"""
    for test in range(2, floor(sqrt(num)) + 1):
        if num % test == 0:
            return False

    # 1 is not prime
    return num > 1


def fizz_buzz(start, end):
    """
    Returns fizz buzz prime or number.
    Starting in rande start to end (inclusive)

    start - integer. Should be greater than 1
    end - integer. Should be greater than or equal to start
    """
    def safe_int(val, default=0):
        try:
            return int(val)
        except ValueError as e:
            print(f'Unable to parse to int due to {e}')
            return default

    start = safe_int(start)
    end = safe_int(end)

    if start <= 0:
        return []

    if start > end:
        return []

    def convert(num):
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
        return output if len(output) else str(num)

    return [convert(num) for num in range(start, end + 1)]


# Testing
# Passing invalid arguments
print(fizz_buzz('hello', 2))
print(fizz_buzz('hello', 'world'))
print(fizz_buzz(1, 'world'))

# Passing floats
print(fizz_buzz(1.1, 2))
print(fizz_buzz(1, 2.6))
print(fizz_buzz(pi, 2 * pi))

# Passing values less than or equal to 0
print(fizz_buzz(0, 2))
print(fizz_buzz(-10, 2))
print(fizz_buzz(1, 0))
print(fizz_buzz(1, -10))


def replace_line(file_name, line_number, line_content):
    """
    Replace line in a file by number

    file_name - String. File to modify.
    line_number - integer. Valid line number.
    line_content - String. Replacement string.
    """

    try:
        line_number = int(line_number)
    except ValueError as e:
        print(f'Unable to parse line_number due to {e}')
        return False

    # assuming the file is small
    # read it to memory
    lines = []
    note = None
    try:
        note = open(file_name, 'r')
        lines += note
    except IOError as e:
        print(f'I/O error {e.errno}: {e.strerror}')
        return False
    except Exception as e:
        print(f'Unable to read file due to {e}')
        return False
    finally:
        if note != None:
            note.close()

    try:
        # replace line by number (assuming user lines are one based)
        lines[line_number - 1] = line_content + '\n'

        note = open(file_name, 'w')

        note.write(''.join(lines))
    except IndexError:
        print(f'Invalid line number {line_number} of {len(lines)}')
        return False
    except IOError as e:
        print(f'I/O error {e.errno}: {e.strerror}')
        return False
    except Exception as e:
        print(f'Unable to write file due to {e}')

        return False
    finally:
        if note != None:
            note.close()

    return True


# Testing
# invalid line number
print(replace_line('errors/exists.txt', 'Invalid Line Number', 'Second'))
# invalid file name
print(replace_line([], 2, 'Second'))
# file does not exist
print(replace_line('errors/not_exists.txt', 2, 'Second'))
# index out of bound
print(replace_line('errors/exists.txt', 20, 'Second'))

# should work
print(replace_line('errors/exists.txt', 2, 'Second'))
