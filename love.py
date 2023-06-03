print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
our_names = (name1 + name2).lower()
num1 = our_names.count("t") + our_names.count("r") + our_names.count("u") + our_names.count("e")
num2 = our_names.count("l") + our_names.count("o") + our_names.count("v") + our_names.count("e")
percentage = str(num1) + str(num2)
percentage = int(percentage)
if percentage < 10 or percentage > 90:
    print(f"Your score {percentage}, you go together like coke and mentos.")
if 40 < percentage < 50:
    print(f"Your score {percentage}, you are alright together")
else:
    print(f"Your score is {percentage}")