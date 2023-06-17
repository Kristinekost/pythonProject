import random
word_list = ["ardvark", "baabok", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
display = []
for i in chosen_word:
    display += "_"
guess = input("Guess a letter: ").lower()
for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        display[i] = guess
print(display)