names_string = input("give me everybody's name, separated by a comma. ")
names = names_string.split(", ")
import random
# number_of_elements = len(names)
# random_numbers = random.randint(0, number_of_elements - 1)
# print(names[random_numbers])
print(random.choice(names))


