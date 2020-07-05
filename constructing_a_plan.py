'''
We'll say that a positive int divides iteself
if every digit in the num divides into the 
num evenly.

for example...128 divides itself
since 1,2, and 8 all divide into 128 evenly

and we'll say that 0 does not divide into anything
evenly, so no num with a 0 digit divides itself.

Write a function to determine if a num divides itself

source - https://codingbat.com/prob/p165941
'''

def divides_self(num):
    # TODO:
    pass


print(divides_self(128)) # true
print(divides_self(12)) # true
print(divides_self(120)) # false