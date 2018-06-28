# --- Define your functions below! ---
def Intro():
    print("Hello! Welcome to the chatbot!")
def greeting():
    print("Let's have a deep conversation")
def dating():
    print ("I am 105 years old. I am a Fashion Nova Instagram Model in my free time.")
    print ("During the day, I am a cereal eater. At night I am Batman.")
    rep = input("Soooo, come here often? ")
    print("Sorry I am no longer interested")

def artist():
    print("""
    Dis u:\n
    \n
    '''⌐(ಠ۾ಠ)¬''' \n
    """)
def is_valid_input(response, all_valid_inputs):
    if response in all_valid_inputs:
        return True
    else:
        return False

# --- Put your main program below! ---
def main():
    valid_input = ["Hi!", 'Hello ;)','love me','Come here often?','I need a partner in crime', 'draw me', 'art', 'draw please']
    Intro()

    while True:
        answer = input("(What will you say?) ")
        if is_valid_input(answer, valid_input):
            if answer == "Hi!":
                greeting()
            elif answer in ['Hello ;)','love me','Come here often?','I need a partner in crime']:
                dating ()
            elif answer in ['draw me', 'art', 'draw please']:
                artist()
        else:
            print("These are the inputs I understand: ")
            for vi in valid_input:
                print(vi)
            print("... I don't understand anything else")

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
