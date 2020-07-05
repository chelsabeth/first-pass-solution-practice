'''
We'll say that a positive int divides iteself
if every digit in the num divides into the 
num evenly.

for example...128 divides itself
since 1, 2, and 8 all divide into 128 evenly

and we'll say that 0 does not divide into anything
evenly, so no num with a 0 digit divides itself.

Write a function to determine if a num divides itself

source - https://codingbat.com/prob/p165941
'''

def divides_self(num):
    # TODO:
    # check if num is equal to zero - return false
    if num == 0:
        return False
    # if length of input is 1 - return true
    if len(str(num)) == 1:
        return True

    # split input into iterable collection of integers
    # loop over collection of digits
    for digit in str(num):
        digit_int = int(digit)
    # if num is evenly divisible by current digit or current digit is 0 - return False
    if digit_int == 0 or num % digit_int != 0:
        return False

    # return true if we loop over entire collection 
    return True

print(divides_self(0)) # false
print(divides_self(1)) # true
print(divides_self(10)) # false
print(divides_self(128)) # true
print(divides_self(12)) # true
print(divides_self(120)) # false


# Questions:
# how big are the nums we will recieve as input? - this matters for runtime

# Assumptions:
# test has to work for all the integers in a num
# output will be a boolean - true or false