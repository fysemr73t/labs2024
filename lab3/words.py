"""
program  to take any input and output just the words, each on their own line.
"""

import sys

if __name__=="__main__":
    inword = True
    for line in sys.stdin:
        for ch in line:
            if ch.isalnum():
                sys.stdout.write(ch)
                inword = True
            else:
                if inword:
                    sys.stdout.write('\n')
                    inword = False
    if inword:
        sys.stdout.write('\n')
