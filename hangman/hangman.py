import random
import hangman_words
from hangman_art import logo, stages

chosen_word = random.choice(hangman_words.word_list)
chosen_word_length = len(chosen_word)
display = []
lives = 6

for i in chosen_word:
    display += "_"

print(logo)
print(display)

end_of_game = False
while not end_of_game:
    guess = input("choose a letter    ").lower()

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("you lose")
            end_of_game = True

    for position in range(chosen_word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    print(f"{''.join(display)}")

    if "_" not in display:
        print("you win")
        end_of_game = True

    print(stages[lives])
