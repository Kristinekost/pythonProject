import random
mapping = ["rock", "paper", "scissors"]
for any in range(3):
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
    computer = random.randint(0, 2)
    print("Your choice is", mapping[choice])
    print("Computers choice is", mapping[computer])
    if choice == computer:
        print("Its a draw!")
    elif (choice == 0 and computer == 2) or (choice == 1 and computer == 0) or (choice == 2 and computer == 1):
        print("You won!")
    else:
        print("Computer win!")