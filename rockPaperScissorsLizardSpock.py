import random
import time

# Define the rules for the extended game
rules = {
    'Rock': ['Scissors', 'Lizard'],
    'Paper': ['Rock', 'Spock'],
    'Scissors': ['Paper', 'Lizard'],
    'Lizard': ['Spock', 'Paper'],
    'Spock': ['Scissors', 'Rock']
}

# Define the corresponding actions for each choice
actions = {
    'Rock': 'CRUSHES',
    'Paper': 'COVERS',
    'Scissors': 'CUTS',
    'Lizard': 'POISONS',
    'Spock': 'SMASHES'
}

# Function to print text with a typing effect
def print_with_typing(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Print a newline at the end

# Print the welcome message and information about the game with typing effect
print_with_typing("Welcome to the Game ROCK - PAPER - SCISSORS - LIZARD - SPOCK")
print_with_typing("The game was created by internet pioneer Sam Cass as an improvement on the classic game rock paper scissors.")
print_with_typing("The rules of the game are:")
print_with_typing("Scissors CUTS Paper")
print_with_typing("Paper COVERS Rock")
print_with_typing("Rock CRUSHES Lizard")
print_with_typing("Lizard POISONS Spock")
print_with_typing("Spock SMASHES Scissors")
print_with_typing("Scissors DECAPITATES Lizard")
print_with_typing("Lizard EATS Paper")
print_with_typing("Paper DISPROVES Spock")
print_with_typing("Spock VAPORIZES Rock")
print_with_typing("")
print_with_typing("(and as it always has)")
print_with_typing("")
print_with_typing("Rock CRUSHES Scissors")
print_with_typing("")

# Ask the user to acknowledge Sam Cass
print_with_typing("All Hail Sam Cass!!!")
acknowledge_sam = input("Type 'Hail' to continue or 'again' to Print the rules of the game again: ").lower()

while acknowledge_sam != 'hail':
    if acknowledge_sam == 'again':
        # Print the rules of the game again
        print_with_typing("Of Course")
        for choice, beats in rules.items():
            print_with_typing(f"{choice} {actions[choice]} {beats[0]}")
            print_with_typing(f"{choice} {actions[choice]} {beats[1]}")
    print_with_typing("All Hail Sam Cass!!!")
    acknowledge_sam = input("Type 'Hail' to continue or 'again' to Print the rules of the game again: ").lower()

while True:
    print_with_typing("\nEnter your choice:")
    print_with_typing("1 - Rock")
    print_with_typing("2 - Paper")
    print_with_typing("3 - Scissors")
    print_with_typing("4 - Lizard")
    print_with_typing("5 - Spock")

    # Take the input from the user
    choice = int(input("Enter your choice: "))

    # Check for valid input
    while choice not in [1, 2, 3, 4, 5]:
        choice = int(input("Enter a valid choice, please: "))

    # Map choice to a string
    choices = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock"}
    choice_name = choices[choice]

    print_with_typing(f"User choice is {choice_name}")
    print_with_typing("Now it's the Computer's Turn....")

    # Computer chooses randomly from 1, 2, 3, 4, and 5
    comp_choice = random.randint(1, 5)

    # Map computer choice to a string
    comp_choices = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock"}
    comp_choice_name = comp_choices[comp_choice]

    print_with_typing(f"Computer choice is {comp_choice_name}")
    print_with_typing(f"{choice_name} {actions[choice_name]} {comp_choice_name}")

    # Determine the result of the game
    if choice == comp_choice:
        result = "DRAW"
    elif comp_choice_name in rules[choice_name]:
        result = choice_name
    else:
        result = comp_choice_name

    # Print the result
    if result == "DRAW":
        print_with_typing("<== It's a tie ==>")
    elif result == choice_name:
        print_with_typing("<== User wins ==>")
    else:
        print_with_typing("<== Computer wins ==>")

    print_with_typing("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans != 'y':
        break

# After coming out of the while loop, print thanks for playing with typing effect
print_with_typing("Thanks for playing")
