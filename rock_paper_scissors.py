"""
Este módulo proporciona acceso a funciones aleatorias y funciones relacionadas con el tiempo.

- random: Proporciona funciones para generar números aleatorios.
"""
import random

# Print the rules of the game
print("Winning rules of the game ROCK PAPER SCISSORS are:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")

while True:
    print("Enter your choice:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    # Take the input from the user
    choice = int(input("Enter your choice: "))

    # Check for valid input
    while choice not in [1, 2, 3]:
        choice = int(input("Enter a valid choice, please: "))

    # Map choice to a string
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    choice_name = choices[choice]

    print("User choice is", choice_name)
    print("Now it's the Computer's Turn....")

    # Computer chooses randomly from 1, 2, and 3
    comp_choice = random.randint(1, 3)

    # Map computer choice to a string
    comp_choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    comp_choice_name = comp_choices[comp_choice]

    print("Computer choice is", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    # Determine the result of the game
    if choice == comp_choice:
        result = ["DRAW"]
    elif ((choice == 1 and comp_choice == 2) or
          (choice == 2 and comp_choice == 1)):
        result = ["Paper"]
    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        result = ["Rock"]
    else:
        result = ["Scissors"]

    # Print the result
    if result == "DRAW":
        print("<== It's a tie ==>")
    elif result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans != 'y':
        break

# After coming out of the while loop, print thanks for playing
print("Thanks for playing")
