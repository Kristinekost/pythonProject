print("Welcome to the python pizza delivery! ")
size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill = bill + 2
else:
    if add_pepperoni == "Y":
        bill = 3
    if size == "M":
        bill = bill + 20
    if size == "L":
        bill = bill + 25
if extra_cheese == "Y":
    bill = bill + 1
print(f"your final sum is {bill}")