# Cup-and-Dice
runs a dice betting game where players can roll different sets of dice, betting on the outcome to win money based on specific rules
This Python script runs a dice betting game where players can roll different sets of dice, betting on the outcome to win money based on specific rules. The game involves interacting with the user to make game decisions and calculating outcomes based on dice rolls. Here's a breakdown of its functionality:

Game Introduction: Welcomes the player, asks for their name, and sets an initial balance of $100 to play with.

Main Game Loop: Continuously prompts the player to start a game until they choose to stop or run out of money. Key steps include:

Checking the player's balance. If it's $0 or less, the game ends.
Asking if the player wants to play a round. If not, the game concludes with a farewell message.
Setting a random goal number between 1 and 100 for the dice roll to aim for.
Taking a bet amount from the player, ensuring it's within their balance.
Dice Selection: The player decides how many six-sided, ten-sided, and twenty-sided dice to roll for the round. The Cup class (assumed to be previously defined) is used to simulate rolling these dice together.

Rolling and Outcome: The total of the dice roll is compared to the goal:

Exact Match: If the roll exactly matches the goal, the player wins 10 times their bet.
Close Match: If the roll is within 3 (but not over) the goal, the player wins 5 times their bet; if within 10 (but not over), they win twice their bet.
Miss: Otherwise, the player loses their bet.
Result Display: After each round, the game shows the roll outcome, whether the player won or lost, and their new balance.

Helper Functions:

get_positive_input: Ensures user inputs are positive integers within the player's balance, allowing for zero if specified.
calculate_winnings: Determines the player's winnings based on the dice roll outcome compared to the goal.
print_result: Displays the round's result, including any winnings and the updated balance.
The script assumes the existence of classes for different-sided dice (SixSidedDie, TenSidedDie, TwentySidedDie) and a Cup class for holding and rolling a combination of these dice, though the implementations of these classes are not provided in the snippet. This game combines elements of chance with strategic betting, offering an engaging way for players to potentially increase their initial stake based on the luck of the dice roll and their betting decisions.
