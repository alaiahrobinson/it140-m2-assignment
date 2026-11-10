
"""
Calculates and displays the year a user was born.

Input:
    User's name as a string entered from the keyboard.
    User's age as an integer entered from the keyboard.

Process:
    Subtract the user's age from the current year.

Output:
    Personalized birth-year message displayed on the screen.

Typical usage example:
    What is your name? Alex
    How old are you? 24
    Hello Alex! You were born in 2002.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    user_name = input("What is your name? ")
    user_age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - user_age

    # Output personalized message with user's name and birth year.
    print(f"\nHello {user_name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()

