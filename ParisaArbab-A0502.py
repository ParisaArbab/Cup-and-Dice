"""
Author: Parisa Arbab
Date: Feb 15 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link: https://youtu.be/hfJLyGIIsmY

Explained in video:
1. Show your primary loop and brag about how clean it is because you practiced top-down development.
2. Describe how you leverage the dice and cups classes from the previous assignment.  Use the classes – don’t store a bunch of values in the game engine that you need!
3. What happens if the user bets a negative amount and then purposefully loses the game?  Do you subtract a negative amount (add) to their account?
"""


import random
from Cup import Cup
# Q2: Assuming the classes SixSidedDie, TenSidedDie, TwentySidedDie, and Cup are defined as before




def main():
    """
    Main function to run the dice betting game. It interacts with the user, takes inputs for the game actions,
    and uses the previously defined dice and cup classes to simulate dice rolls and calculate winnings.
    """
    print("Welcome to the Dice Betting Game!")
    name = input("What's your name? ")
    balance = 100
    print(f"\nHello, {name}! You have ${balance} to play with.")
    while True:    #Q1 Primary Loop
        if balance <= 0:
            print(f"Sorry, {name}. Your balance is ${balance} and you are not able to continue the game.")
            break  # Exit the loop and end the game


        play_game = input("Would you like to play a game? (yes/no) ").lower().strip()
        if play_game not in ['yes', 'y']:
            print("Thank you for playing. Goodbye!")
            break
        else:
            goal = random.randint(1, 100)
            bet = get_positive_input("How much would you like to bet? $", balance)
            balance -= bet

        six_sided_dice_count = get_positive_input("How many six-sided dice would you like to roll? ", balance, allow_zero=True)
        ten_sided_dice_count = get_positive_input("How many ten-sided dice would you like to roll? ", balance, allow_zero=True)
        twenty_sided_dice_count = get_positive_input("How many twenty-sided dice would you like to roll? ", balance, allow_zero=True)

        cup = Cup(six_sided_dice_count, ten_sided_dice_count, twenty_sided_dice_count)
        roll_result = cup.roll()
        print(f"Rolling... You rolled a total of {roll_result} aiming for {goal}.")

        winnings = calculate_winnings(roll_result, goal, bet)
        balance += winnings

        print_result(name, balance, winnings)




def get_positive_input(prompt, max_amount, allow_zero=False):
    """
    Helper function to ensure user inputs a positive number
    """
    while True:
        try:
            value = int(input(prompt))
            if (value > 0 or (allow_zero and value == 0)) and value <= max_amount:
                return value
            else:
                print(f"insufficient balance.")
        except ValueError:
            print("Please enter a valid number.")





def calculate_winnings(roll, goal, bet):
    """
    Calculates winnings based on the roll result, the goal, and the bet amount.
    Ensures that for 5x and 2x winnings, the roll does not exceed the goal.
    """
    if roll == goal:
        return bet * 10  # 10x the bet for an exact match
    elif goal - 3 <= roll <= goal:
        return bet * 5  # 5x the bet if within 3 of the goal, but not over
    elif goal - 10 <= roll <= goal:
        return bet * 2  # 2x the bet if within 10 of the goal, but not over
    return -bet  # Loss: return negative bet to subtract it from balance

def print_result(name, balance, winnings):
    """
    Prints the result of the game round, including the player's name, winnings, and updated balance.
    """
    if winnings > 0:
        print(f"Congratulations, {name}! You won ${winnings}. Your new balance is ${balance}.")
    else:
        print(f"Sorry, {name}. You didn't win this time. Your balance is now ${balance}.")

if __name__ == "__main__":
    main()
