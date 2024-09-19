

import sys
import argparse
import hashlib

WORDS = '/usr/share/dict/web2'

def checkhash(word,md5digest):
    hasher = hashlib.md5()
    hasher.update(word.encode('utf-8'))
    if hasher.hexdigest()==md5hash:
        print(f"md5({word})={md5hash}")
        return True
    return False

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Demo password cracher",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("md5hash",help="32 character MD5 hash")
    args = parser.parse_args()
    if len(args.md5hash)!=32:
        raise RuntimeError("md5hash must be 32 characters")
    md5hash = args.md5hash.lower() # make sure it's lower case

    count = 0
    with open(WORDS,"r") as f:
        for line in f:
            word = line.strip()
            if checkhash(word.lower(),md5hash):
                exit(0)
            if checkhash(word.upper(),md5hash):
                exit(0)
            # add your own!
            count += 1
        print(f"Couldn't find it; tried {count} words")
