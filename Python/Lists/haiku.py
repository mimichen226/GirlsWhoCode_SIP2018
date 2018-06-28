import random

three = ["Mimi Chen", "chocolate", "ambulance"]
five = ["hippopotamus", "capitalism"]

three_index = random.randint(0, len(three) - 1)
five_index = random.randint(0, len(five) - 1)
three_index_2 = random.randint(0, len(three) - 1)

print("{}\n{}\n{}".format(three[three_index], five[five_index], three[three_index_2]))
