'''
Input:
Print Script Name
Output:
PS C:\Users\JYOTH\Desktop\python_practice\sys> & C:/Python311/python.exe c:/Users/JYOTH/Desktop/python_practice/sys/script_name.py
The script name is script_name.py

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
