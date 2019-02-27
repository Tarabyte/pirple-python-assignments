"""
Project #2: Hangman

Have you ever played hangman? It's a children's game, normally played by kids when they're supposed to be doing homework instead. If you've never played here are the rules:

https://www.youtube.com/watch?v=cGOeiQfjYPk

https://www.wikihow.com/Play-Hangman

For this assignment, we want to play hangman in 2-player mode. The game should start by prompting player 1 to pick a word. Then the screen should clear itself so that player 2 can't see the word

hint: print(chr(27) + "[2J")

After the screen is clear, the "gallows" and the empty letter spaces should be drawn,
and player 2 should be allowed to guess letters until they either win, or lose.

As they choose correct letters, the letters should appear on the screen in place of the blank space (clear and redraw the whole screen).
As they choose wrong letters, the "man" himself should come end up being drawn, piece by piece.
How many guesses they get before losing is up to you (depending on how complicated of a man you want to draw).

Try finding a large list of dictionary words and embedding them in your application.
When the game starts, instead of player 1 choosing the word to play with, the computer should pick a random word from the dictionary.
This will allow you to play against the computer instead of only 2-player mode.
When the game starts, the user should be prompted to choose between 1-player or 2-player mode.
"""
from colorama import init, Back, Fore
from itertools import count, islice
from random import randrange
from utils.select import select
from utils.clear import clear

# enable console esc sequences on windows
init()


def _init_dictionary():
    """
    Run this function if you want to locally store some words from nltk coprus
    """
    from nltk.corpus import words  # local import generally this package is not needed

    def is_suitable(word):
        return len(word) > 6 and len(word) < 12

    with open('words.txt', 'w') as file:
        long_words = filter(is_suitable, words.words())
        file.write('\n'.join(long_words))


class Hangman:
    """
    Basic Hangman Game Class
    """
    hangman = (
        """
   _________
    |/
    |
    |
    |
    |
    |
    |___
    """,

        """
   _________
    |/   |
    |
    |
    |
    |
    |
    |___
    H""",

        """
   _________
    |/   |
    |   (_)
    |
    |
    |
    |
    |___
    HA""",

        """
   _________
    |/   |
    |   (_)
    |    |
    |    |
    |
    |
    |___
    HAN""",


        """
   _________
    |/   |
    |   (_)
    |   /|
    |    |
    |
    |
    |___
    HANG""",


        """
   _________
    |/   |
    |   (_)
    |   /|\\
    |    |
    |
    |
    |___
    HANGM""",



        """
   _________
    |/   |
    |   (_)
    |   /|\\
    |    |
    |   /
    |
    |___
    HANGMA""",


        """
   _________
    |/   |
    |   (_)
    |   /|\\
    |    |
    |   / \\
    |
    |___
    HANGMAN""")

    max_gallows = len(hangman) - 1

    def __init__(self):
        # save all letters
        self.abc = list(map(chr, islice(count(ord('a')), 26)))
        self.attempts = []
        self.used = set()
        self.gallows = 0
        self.word = self._get_word()
        self.notification = ''
        self.state = None

    def start(self):
        """Start main game loop"""
        while not self._done():
            self._draw_field()
            letter = input('Enter the letter: ').strip().lower()

            # handle commands
            command = self._handle_command(letter)

            # if it was command
            if command != None:
                # should we break the game loop
                if command:
                    break
                else:
                    continue

            # validate input is a single character
            if len(letter) != 1 or not (ord('a') <= ord(letter[0]) <= ord('z')):
                self.notification = 'Please only enter single letter'
                continue

            self._attempt(letter)

        self._draw_final()

    def _handle_command(self, command):
        """Check if input was a command and do navigation if required"""
        if command == 'quit' or command == ':q':
            confirm = input('Are you sure you want to quit? (yes/no) ')
            if confirm.lower() == 'yes':
                self.notification = 'Bye-bye!'
                return True
            else:
                return False

    def _draw_field(self):
        clear()

        if self.notification:
            print(self.notification)

        self._draw_word()
        self._draw_hangman()
        self._draw_abc()

    def _draw_hangman(self):
        """Print current state of hangman"""
        print(type(self).hangman[self.gallows])

    def _draw_abc(self):
        """Print ABC for user convenience"""
        word = self.word
        used = self.used

        for letter in self.abc:
            if letter in used:
                print(Back.GREEN if letter in word else Back.RED,
                      letter.upper(), Back.RESET, sep='', end='')
            else:
                print(letter.upper(), end='')
        print('\n')

    def _draw_final(self):
        clear()

        color = Fore.GREEN if self.state == 'win' else Fore.RED

        print(color, self.notification, Fore.RESET, sep='\n')

        print(f'The word was: ')
        self._draw_word(True)

        if self.state == 'lost':
            self._draw_hangman()

        print('Stats:')
        print(f'Total Attempts: {len(self.attempts)}')
        print(f'Wrong Attempts: {self.gallows}')

    def _draw_word(self, reveal=False):
        word = self.word
        attempts = self.attempts
        word_len = len(word)

        def symbol(letter):
            guessed = letter in attempts
            if reveal:
                color = Fore.GREEN if guessed else Fore.RED
                return f'{color}{letter.upper()}{Fore.RESET}'

            return letter.upper() if guessed else ' '

        print('┌─' + '─┬─'.join('─'*word_len) + '─┐')

        print('| ' + ' | '.join([symbol(letter) for letter in word]) + ' |')

        print('└─' + '─┴─'.join('─'*word_len) + '─┘')

    def _done(self):
        """Check if player won or lost"""
        if self._has_lost():
            self.notification = 'Sorry, you loose'
            self.state = 'lost'
            return True

        if self._has_won():
            self.notification = 'Congratulations! You win.'
            self.state = 'win'
            return True

        return False

    def _has_won(self):
        """Check if player guessed the word"""
        for letter in self.word:
            if not (letter in self.attempts):
                return False

        return True

    def _has_lost(self):
        """Check if player exceeded max attempts"""
        return self.gallows == type(self).max_gallows

    def _attempt(self, letter):
        letter = letter.lower()

        if not letter:
            return False

        if letter in self.used:
            self.notification = f'The letter "{letter.upper()}" already used.'
            return False

        self.attempts.append(letter)
        self.used.add(letter)

        if not (letter in self.word):
            self.gallows += 1

        return True

    def _get_word(self):
        """
        Get a word to play
        """
        raise 'Should be implemented in sub class'


class SinglePlayerHangman(Hangman):
    def _get_word(self):
        """
        Read a random word from file
        Waterman's "Reservoir Algorithm"
        """
        with open('words.txt') as words:
            word = next(words)
            for index, line in enumerate(words, 2):
                if randrange(index):
                    continue
                word = line

        return word.strip()


class TwoPlayersHangman(Hangman):
    def _get_word(self):
        """
        Allow Player #1 to enter the word
        """
        print('Make sure Player #2 is not watching the screen!')
        word = input('Please enter the word: ')

        clear()
        return word.lower()


def game():
    modes = [{'title': 'Single Player', 'clz': SinglePlayerHangman},
             {'title': 'Two Players', 'clz': TwoPlayersHangman}]

    selected_mode = select(list(map(lambda x: x['title'], modes)),
                           header='Please select game mode:')

    new_game = modes[selected_mode]['clz']()

    new_game.start()


# _init_dictionary()
game()
