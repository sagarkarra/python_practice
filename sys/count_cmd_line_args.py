'''
Input:
Print Command-Line Arguments
Output:
The command line arguments are:
c:/Users/JYOTH/Desktop/python_practice/cmd_line_args.py

Print all command-line arguments passed to the script.

import sys
print("The command line argument are:")
count=0
for i in sys.argv:
    count+=1
    print(count)

Solution 2:
'''
import sys
def count_arguments():
    print("Number of arguments:", len(sys.argv) - 1)

count_arguments()