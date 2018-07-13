# Starter code for a riddle game
# The user has 3 tries to guess the answer to a riddle
# After
def display(riddle, try_number, hint_list):
    '''
    Given the riddle and number of attempts, the function
    displays number of attempts and the riddle question

    input: riddle (string), try_number(integer)
    output (return value): N/A
    '''
    # Print the attempt number and the riddle question
    print("Attempt #{}: {}".format(try_number + 1, riddle)) # +1 so start counting at 1
    # Print hints for 2nd, 3rd, etc attempts
    if try_number > 0:
        print("HINT: {}".format(hint_list[try_number - 1]))


def riddle():
    # Initialize our variables
    guess_count = 0                   # Keeps track of the number of guesses (need if using a while loop)
    riddle = "What has a head and a tail but no body?"     # The riddle
    answer = "penny"     # The answer to the riddle; can be a string or list of possible answers
    hints = ["it is inanimate", "1 cent"] # Need allowed_number_of_guesses - 1 hints
                        # i.e. if 3 guesses allowed, need 2 hints
    guess = None                      # Keep track of the user's guess
    win = False                       # Keep track of whether the user has won

    # Use a loop that gives the user 3 tries to guess the answer to the riddle
    while guess_count < 3:
        # Print out the riddle prompt, attempt number, and hints if not the first try
        display(riddle, guess_count, hints)
        # Get user input and process it
        guess = input("Enter your guess: ").lower().rstrip()
        guess_count += 1
        # Check if answer is correct
        if guess == answer:
            # Set variable "win" to True and break out of loop
            win = True
            break
    # Print the answer. Different message template for winning and losing
    # i.e. "Congrats! The answer is indeed _____" for winning, and
    #      "WRRRROOOOONG. The correct answer is _____" for losing
    if win:
        print("Congrats! The answer is indeed {}".format(answer))
    else:
        print("BZZZZZZZZ... The correct answer is {}".format(answer))

if __name__ == "__main__":
    riddle()
