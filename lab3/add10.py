"""
Simple program to take every input line and output each line with a number appended
"""


import sys
import hashlib

if __name__=="__main__":
    for line in sys.stdin:
        line = line[:-1]        # remove the \n
        for count in range(0,10):
            print(f"{line}{count}")
