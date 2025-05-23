"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Milan Angelis
email: milanangelis@seznam.cz
"""

import random
from time import time


def generate_unique_number(digits = 4) -> str:
    """
    Function that generates a random number with a defined number of digits,
        each digit is unique and the first digit is not "0".

    :param digits: number of digits (default value: 4)
    :type digits: int
    :return: a random number with the specified number of digits
    :rtype: str

    :Example: 
    >>> result = generate_unique_number(6)
    >>> result
    "506971"
    """

    # Generate the first digit:
    all_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    first_digit = random.choice(all_digits)
    all_digits.remove(first_digit)
    all_digits.append("0")

    # Generate next digits:
    generated_digits = random.sample(all_digits, digits - 1)
    generated_digits.insert(0, first_digit)
    generated_number = "".join(generated_digits)
    return generated_number


def check_input(numeric_string: str, digits = 4) -> bool:
    """
    Function that checks the numeric string for bulls and cows game:
    - if the numeric string contains only digits,
    - if the numeric string has the right number of digits (parameter digits),
    - if all the digits are unique,
    - if the first digit is not "0".

    :param numeric_string: numeric string to be checked
    :type numeric_string: str
    :param digits: number of digits (reference value), default value = 4
    :type digits: int
    :return: True if all the conditions are met, False otherwise
    :rtype: bool

    :Example:
    >>> number_check = check_input("1274")
    >>> number_check
    True
    """

    if not numeric_string.isdigit():
        print("Your input contains non-digit symbols.")
        return False
    elif len(numeric_string) != digits:
        print(f"Your number does not consist of {digits} digits.")
        return False
    elif len(numeric_string) != len(set(numeric_string)):
        print("The number contains at least two identical digits.")
        return False
    elif numeric_string[0] == "0":
        print("The first digit must not be 0.")
        return False
    return True
    

def count_bulls_cows(guess: str, original: str) -> tuple:
    """
    Function that compares two numeric strings and returns 
    the number of identical digits at the same index in the string (bulls) 
    and the number of identical digits at different indices (cows).

    :param original: the original numeric string
    :type original: str
    :param guess: the numeric string to be compared with the original string
    :type guess: str
    :return: a pair of values, where the first element is the number of bulls
        and the second element is the number of cows
    :rtype: tuple

    :Example:
    >>> result = count_bulls_cows("25746", "25407")
    >>> result
    (2, 2)
    """

    bulls, cows = (0, 0)
    for number in range(len(original)):
        if guess[number] == original[number]:
            bulls += 1
        elif guess[number] in original:
            cows += 1
    return bulls, cows


def print_bulls_cows(x: int, y: int) -> None:
    """
    Function that prints the bulls and cows counts. 
    Function takes singular and plural forms into account.

    :param x: the number of bulls
    :type x: int
    :param y: the number of cows
    :type y: int
    :return: None (printing results only)
    :rtype: None

    :Example:
    >>> text = print_bulls_cows(2, 1)
    >>> text
    2 bulls, 1 cow
    """

    words = ["bull", "bulls", "cow", "cows"]
    bull = words[0] if x == 1 else words[1]
    cow = words[2] if y == 1 else words[3]
    print(f"{x} {bull}, {y} {cow}.")


def play_game(users_guess: str) -> tuple:
    """
    Function that runs one game of bulls and cows.

    :param users_guess: user's guess to be compared to the generated number
    :type users_guess: str
    :return: a pair of values representing the number of user's attempts
        the duration time of the game in seconds
    :rtype: tuple

    :Example:
    >>> attempts, time = play_game("2741")
    >>> attempts, time
    (5, 23)
    """

    # Generating random number using function generate_unique_number():
    random_number = generate_unique_number()
    attempts = 1

    # Starting timer
    time_start = time()

    # While loop (while the numbers don't match):
    while users_guess != random_number:

        # Validation of user's input:
        while not check_input(users_guess, 4):
            print("Try again: ")
            users_guess = str(input())

        # User's number may have changed after "validation block":    
        if users_guess == random_number:
            attempts += 1
            break

        # Compare user's number with the generated number:
        attempts += 1
        bulls, cows = count_bulls_cows(users_guess, random_number)
        print_bulls_cows(bulls, cows)
        users_guess = str(input())

    # Stop the timer and format the time (seconds):
    time_end = time()
    users_time = round(time_end - time_start)

    return attempts, users_time


def main():

    number_of_digits = 4
    
    # Print the greeting:
    print(f"""
Hi there!
-----------------------------------------------
I've generated a random 4-digit number for you.
Let's play a bulls and cows game.

-----------------------------------------------
Enter a number:
-----------------------------------------------
""")

    # Save statistics for each game round (guesses and time),
    # Results will be saved there after each game:
    statistics = (f"""
Statistics (guesses / time (s)):
. . . . . . . . . . . . . . . .
    """)

    # While loop for repeating the game (until the user selects quit)
    while True:

        users_number = str(input())
        # If the user selects "q", it means 
        # they don't want to play another game:
        if users_number == "q":
            break

        # Play the game
        number_of_attempts, time_attempt = play_game(users_number)

        # Save the information about the current game to statistics:
        statistics += (f"""{number_of_attempts} / {time_attempt}
    """
    )

        print(f"""
Correct, you've guessed the right number
in {number_of_attempts} guesses!
Your time: {time_attempt} seconds
-----------------------------------------------
That's amazing!
-----------------------------------------------
{statistics}
-----------------------------------------------
I've generated a new {number_of_digits} digit number for you. 
If you'd like to play again, enter a number.
Otherwise, press "q" to quit the game.
-----------------------------------------------
"""
    )


if __name__ == "__main__":
    main()