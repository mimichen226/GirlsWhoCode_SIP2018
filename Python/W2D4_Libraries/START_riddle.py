# Starter code for a riddle game
# The user has N tries to guess the answer to a riddle
# After the first attempt, give the user a hint for each attempt

def display(riddle, try_number, hint_list):
    '''
    Given the riddle and number of attempts, the function
    displays number of attempts and the riddle question

    input: riddle (string), try_number(integer), hint_list (list of strings)
    output (return value): N/A
    '''
    # TODO: Print the attempt number and the riddle question

    # Print a hint if not the first attempt
    if try_number > 0:
        print("HINT: {}".format()) # TODO: Access hint_list for a hints


def riddle():
    # Initialize our variables
    guess_count = 0                   # Keeps track of the number of guesses (need if using a while loop)
    riddle = "this is the riddle"     # TODO: The riddle
    answer = "answer"                 # TODO: The answer to the riddle; can be a string or list of possible answers
    hints = ["hint 1", "hint 2"]      # TODO: List of hints; number of hints == number of allowed attempts - 1
                                      # i.e. if 3 guesses allowed, need 2 hints
    guess = None                      # Keep track of the user's guess
    win = False                       # Keep track of whether the user has won

    # Use a loop that gives the user 3 tries to guess the answer to the riddle

        # TODO: Call "display" function (with the right parameters!!)
        # and print out the riddle prompt, attempt number,
        # and hints if not the first try

        # TODO: Get user input and process it
        guess = input("Enter your guess: ").lower().rstrip()

        # TODO: Check if answer is correct

            # TODO: Set variable "win" to True and break out of loop

    # TODO: Print different messages for winning and losing.
    #       Be sure to include the right answer in your message
    #
    #      i.e. "Congrats! The answer is indeed _____" for winning,
    #      "WRRRROOOOONG. The correct answer is _____" for losing

if __name__ == "__main__":
    riddle()
