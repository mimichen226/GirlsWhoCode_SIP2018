## OUR LARGER PROBLEM: Given a list of ages, calculate the average

# The input
ages = [16,22,20,19,22,11,17]
# Find the sum (loop through the elements of the age list)
sum = 0
for a in ages:
    sum += a
# Find the number of elements in our aList
count = len(ages)
# Divide the sum by the number of the elements
print(sum/ count)
