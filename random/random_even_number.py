'''
Input:
Generate a random even number between 2 and 100
Output:
Random Even Number: 48

import random
num = random.randrange(2, 101, 2)
print("Random Even Number:", num)

Solution 2:
'''
import random
def even_number():
    return random.randrange(2, 101, 2)
print("Random Even Number:", even_number())