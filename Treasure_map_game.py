row1 = ["🤡", "🤡", "🤡"]
row2 = ["🤡", "🤡", "🤡"]
row3 = ["🤡", "🤡", "🤡"]
map = [row1, row2, row3]
treasure = [1, 1]
print(f"{row1}\n{row2}\n{row3}\n")
is_win = False
for any in range(4):
    position = input("Where do you want to put the treasure? ")
    chosen_numbers = position.split(' ')
    chosen_column = int(chosen_numbers[0])
    chosen_row = int(chosen_numbers[1])
    if chosen_row != treasure[1] or chosen_column != treasure[0]:
        map[chosen_row][chosen_column] = "X"
        print(f"{row1}\n{row2}\n{row3}\n")
    else:
        map[chosen_row][chosen_column] = "💸"
        print(f"{row1}\n{row2}\n{row3}\n")
        is_win = True
        break
if is_win:
    print("You win!")
else:
    print("You lose!")