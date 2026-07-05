'''
Input:
Simulate rolling a six-sided die.
Output:
After rolling a six sided die: 1

import random
result = random.randint(1, 6)
print("After rolling a six sided die:", result)

Solution 2:
'''
import random
def roll_dice():
    return random.randint(1, 6)

result = roll_dice()
print("After rolling a six sided die:", result)