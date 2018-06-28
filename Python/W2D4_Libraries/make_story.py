def create_sentence(name, verb):
    name = name.title().lstrip().rstrip()
    verb = verb.lstrip().rstrip()
    sentence = "My name is {} and I like to {}.".format(name, verb)
    return sentence

def create_story():
    print("INTRO")
    print(create_sentence("    mimi   ", " eat  "))
    print("THE END")
