print("Welcome to the tip Calculator ")
total_bill = int(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10 12 or 15 "))
if percentage_tip == 10 or percentage_tip == 12 or percentage_tip == 15:
    total_people = int(input("How many people to split the bill? "))
    splited_payment = ((total_bill / 100 * percentage_tip) + total_bill) / total_people
    print("Each person should pay $", round(splited_payment, 2))
else:
    percentage_tip = int(input("Please enter 10 12 or 15 next time"))

