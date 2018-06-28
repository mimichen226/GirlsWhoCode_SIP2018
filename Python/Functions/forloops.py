mylist = ["haha","cool","yay", "Mimi"]

# access the elements
for ml in mylist: # goes through each element
    print(ml) # ml is the elements

# accss the index
print()
for index in range(len(mylist) - 1):  # range(4)  # goes through the range of NUMBERS 0, 1, 2, 3
    print(index)  # index is the index of the elements
    print(mylist[index], mylist[index + 1]) # print the elements
