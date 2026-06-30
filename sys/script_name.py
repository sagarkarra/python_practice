'''
Input:

Print Script Name

Print only the script's filename.

import sys
import os

print("The script name is",os.path.basename(sys.argv[0]))

Solution 2:
'''
import sys
import os

def print_script_name():
    print("The script name is",os.path.basename(sys.argv[0]))

print_script_name()