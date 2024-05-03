import random

def choose_word():
    # List of words for the game
    words = ["python", "hangman", "program", "computer", "code", "game", "player"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with underscores for unguessed letters
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess! You have", attempts, "attempts left.")
            if attempts == 0:
                print("Sorry, you ran out of attempts! The word was:", word)
                break
        else:
            print("Correct guess!")

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break

if __name__ == "__main__":
    hangman()
