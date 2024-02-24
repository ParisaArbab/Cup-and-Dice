"""
Author: Parisa Arbab
Date: Feb 15 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link: https://youtu.be/3rMbnwBFsfA

Explained in video:
1. Show how you extend sixSidedDie when writing TenSidedDie and TwentySidedDie.
2. Show how you compose the cups class with the die classes.

"""


import random

class SixSidedDie:
    """A class representing a six-sided die."""

    def __init__(self):
        """Initialize the die with a default face value."""
        self.faceValue = 1

    def roll(self):
        """Roll the die and every time update the face value with a random number between 1 and 6."""
        self.faceValue = random.randint(1, 6)
        return self.faceValue

    def getFaceValue(self):
        """keep the result of the last roll. Return the current face value of the die."""
        return self.faceValue

    def __repr__(self):
        """Return a string representation of the die and its current face value."""
        return f"SixSidedDie({self.faceValue})"
class TenSidedDie(SixSidedDie):
    """A class representing a ten-sided die, extending the SixSidedDie class."""

    def roll(self):
        """Roll the die and update the face value with a random number between 1 and 10."""
        self.faceValue = random.randint(1, 10)
        return self.faceValue

    def __repr__ (self):
        """Return a string representation of the ten-sided die and its current face value."""
        return f"TenSidedDie({self.faceValue})"

class TwentySidedDie(SixSidedDie):
    """A class representing a twenty-sided die, extending the SixSidedDie class."""

    def roll(self):
        """Roll the die and update the face value with a random number between 1 and 20."""
        self.faceValue = random.randint(1, 20)
        return self.faceValue

    def __repr__(self):
        """Return a string representation of the twenty-sided die and its current face value."""
        return f"TwentySidedDie({self.faceValue})"

"""Q2 Compose: class cup is a composition example. 
# It is composed of multiple dice objects, which can be of type SixSidedDie, TenSidedDie, or TwentySidedDie. 
# The Cup class manages these dice as a collection, 
allowing them to be rolled together and summing their values.
"""
class Cup:
    """A class representing a cup holding an assortment of dice."""
    #instantiate of six,ten,twenty side
    def __init__(self, six=1, ten=1, twenty=1):
        """Initialize the cup with a specified number of six-, ten-, and twenty-sided dice."""
        self.dice = [SixSidedDie() for _ in range(six)] + \
                    [TenSidedDie() for _ in range(ten)] + \
                    [TwentySidedDie() for _ in range(twenty)]


#Q1 Extend: override roll() to adjust the range of possible values to fit ten and twenty sides
    def roll(self):
        """Roll all dice in the cup and return the total sum of their face values."""
        return sum(die.roll() for die in self.dice)

    def getSum(self):
        """Return the sum of the current face values of all dice in the cup."""
        return sum(die.getFaceValue() for die in self.dice)

    def __repr__(self):
        """Return a string representation of the cup and all dice contained within it."""
        return f"Cup({', '.join(repr(die) for die in self.dice)})"



# Example Usage
if __name__ == "__main__":
    # Demonstrate using a six-sided die
    d = SixSidedDie()
    print(d.roll())  # Roll the die and print the result
    print(d.getFaceValue())  # Print the current face value of the die
    print(d)  # Print the string representation of the die

    # Demonstrate using a ten-sided die
    t = TenSidedDie()
    print(t.roll())  # Roll the die and print the result
    print(t)  # Print the string representation of the die

    # Demonstrate using a twenty-sided die
    tw = TwentySidedDie()
    print(tw.roll())  # Roll the die and print the result
    print(tw)  # Print the string representation of the die

    # Demonstrate using a cup with dice
    cup = Cup(1, 2, 1)  # Initialize a cup with 1 six-sided, 2 ten-sided, and 1 twenty-sided dice
    print(cup.roll())  # Roll all dice in the cup and print the total sum
    print(cup.getSum())  # Print the sum of the current face values of all dice in the cup
    print(cup)  # Print the string representation of the cup and its contents