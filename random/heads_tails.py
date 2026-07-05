'''
Input:
Simulate flipping a coin ("Heads" or "Tails").
Output:
After tossing: Tails

import random
result = random.choice(["Heads", "Tails"])
print("After tossing:",result)

Solution 2:
'''
import random
def flip_coin():
    return random.choice(["Heads", "Tails"])
result = flip_coin()
print("After tossing:",result)