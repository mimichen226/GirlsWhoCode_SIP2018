sum = 0
for i in range(15):
    sum += i
    if i < 5 or i % 10 == 0:
        print("Apple Pen")
    elif i % 3 == 0 and i > 8:
        print("Pineapple Pen")
    else:
        continue
print("PEN PINEAPPLE APPLE PEN")
print("Sum is {}".format(sum))
