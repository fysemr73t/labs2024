"""
Simple program to take every input line and output each line with a number appended
If an argument is provided, add from 0 to the number provided
"""


import sys
import hashlib
import argparse
import time

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Send each input line to the output, printing OUTPUT_COUNT lines to output every DELAY seconds. ",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--delay",default=5,type=int,)
    parser.add_argument("--output_count",default=5,type=int,)
    args = parser.parse_args()


    linecount = 0
    showcount = args.output_count
    tstart = t0 = time.time()
    for line in sys.stdin:
        line = line[:-1]        # remove the \n
        print(line)
        linecount += 1
        if time.time() > t0 + args.delay:
            print(f"line {linecount}:\t{line}",file=sys.stderr)
            showcount -= 1
            if showcount == 0:
                showcount = args.output_count
                t0 = time.time()
                print(f"lines/sec: {linecount//(t0-tstart):,}\n",file=sys.stderr)
