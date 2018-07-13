def cool_math(number):
    sqrt = number**(1/2)
    square = number**2
    mod3 = number % 3
    return sqrt, square, mod3

magic_number = 5
square_root, square, modulus_3 = cool_math(magic_number)
print("The square root of {} is {}".format(magic_number, square_root))
print("The square of {} is {}".format(magic_number, square))
print("The modulus_3 of {} is {}".format(magic_number, modulus_3))
