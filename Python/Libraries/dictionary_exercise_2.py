# Write a function that counts the frequency of each
# letter in a string

def letter_frequency(word):
    # Dictionary holds count of each letter
    # key = letter
    # value = count
    frequency = {}

    for char in word:
        # character is in our dictionary
        if char in frequency.keys():
            # we can just add 1 to the count
            frequency[char] =  frequency[char] + 1
        # character is NOT in our dictionary
        else:
            frequency[char] = 1
    print(frequency)

letter_frequency("pen pineapple apple pen")
