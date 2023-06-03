year = int(input("Which year do you want to check? "))
if year % 4 == 0 and year % 100 != 0:
    print("the year is leap")
elif year % 400 == 0:
    print("the year is leap")
else:
    print("the year is not leap")