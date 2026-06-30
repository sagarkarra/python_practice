'''
Input:
Print Command-Line Arguments
Output:
The command line arguments are:
c:/Users/JYOTH/Desktop/python_practice/cmd_line_args.py

Print all command-line arguments passed to the script.

import sys
print("The command line arguments are:")
for i in sys.argv:
    print(i)

Solution 2:
'''
import sys
def print_arguments():
    print("The command line arguments are:")
    for i in sys.argv:
        print(i)
        
print_arguments()
