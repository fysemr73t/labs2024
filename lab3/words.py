"""
program  to take any input and output just the words, each on their own line.
"""

import sys

if __name__=="__main__":
    for line in sys.stdin:
        for ch in line:
            if ch.isalnum():
                sys.stdout.write(ch)
            else:
                sys.stdout.write('\n')
