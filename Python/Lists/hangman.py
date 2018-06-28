# defining the function display
def print_beginning_of_game():
    print("WELCOME TO HANGMAN")

def display(word, already_guessed_letters):
    new_str = ""
    for letter in word:
        if letter in already_guessed_letters:
            new_str += letter
        # Processing the space in our phrase
        elif letter == " ":
            new_str += "  "
        # the letter in our phrase has not been guessed yet
        else:
            new_str += "_ "
    return new_str

def main():
    print_beginning_of_game()

    # Have a word/ phrase
    phrase = "turtles are cool"

    # Keep track of user's guesses
    guessed_letters = []
    game_over = False

    # Tell user how many spaces and letters they need to guess
    beginning = display(phrase, guessed_letters) # Calling function display
    print(beginning)

    while game_over != True:
        # Allow user to give input to computer
        guess = input("Enter a letter: ")

        # Tell the user if they get the right letter
        if guess in phrase:
            print("You got a letter: {}".format(guess))
        # Tell the user if they get the wrong letter
        else:
            print("{} is not in the phrase".format(guess))
        # Add the guess letter to our list of guessed letters
        guessed_letters.append(guess)

        # Tell user how many spaces and letters they need to guess
        wakeup = display(phrase, guessed_letters)
        print(wakeup)

        # End the game if the user gets all the right letters in our word/ phrase
        if "_" in wakeup:
            game_over = False
        else:
            game_over = True
    print("END OF GAME")

if __name__ == "__main__":
    main()
