'''
Input:
Print Script Name
Output:
The script name is script_name.py

Print only the script's filename.
'''

import sys
import os
print("The script name is",os.path.basename(sys.argv[0]))
