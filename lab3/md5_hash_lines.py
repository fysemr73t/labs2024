"""
Simple program to hash each line of input and output the hash, a tab, and the line
"""


import sys
import hashlib

if __name__=="__main__":
    for line in sys.stdin:
        line = line[:-1]        # remove the \n
        hasher = hashlib.md5()
        hasher.update(line.encode('utf-8'))
        print(hasher.hexdigest()+"\t"+line)
