# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from random import randint

HARD_LEVEL = 5
EASY_LEVEL = 10


def check_answer(guess, number, turn):
    if guess > number:
        print("too high")
        return turn - 1
    elif guess < number:
        print("too low")
        return turn - 1
    else:
        print("spot on")
        exit()


def set_difficulty(difficulty):
    if difficulty == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"pssst, the answer is {answer}")

    turns = set_difficulty(input("type 'easy' for 10 turns, or 'hard' for 5 turns:  "))

    while turns > 0:
        turns = check_answer(int(input(f"please enter your {turns} guess:  ")), answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")



game()