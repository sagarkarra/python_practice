'''
Input:
Generate a random floating-point number between 0 and 1.
Output:
Random floating point value is 0.6885874342068614

import random as r
print("Random floating point value is",r.random())

Solution 2:
'''
import random as r
def random_float_number():
    return r.random()
float_number=random_float_number()
print("Random floating point value is",float_number)
