"""
Simple program to take every input line and output each line with a number appended
If an argument is provided, add from 0 to the number provided
"""


import sys
import hashlib
import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="For each input line, output that line followed by nothing and then the numbers 0 through maxnum",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--maxnum",default=10,type=int,)
    args = parser.parse_args()


    for line in sys.stdin:
        line = line[:-1]        # remove the \n
        print(line)
        for count in range(0,args.maxnum+1):
            print(f"{line}{count}")
