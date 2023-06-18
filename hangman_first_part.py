import random
from words_hangman import word_list
chosen_word = random.choice(word_list)
lives = 6
from hangman_art import logo
print(logo)
print(f'Pssst, the solution is {chosen_word}.')
display = []
for i in chosen_word:
    display += "_"
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed  {guess}")
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        print(f"Your guessed {guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("you won")
    from hangman_art import stages
    print(stages[lives])