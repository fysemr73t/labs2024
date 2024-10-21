import msoffcrypto
import sys
import io
import argparse

def check_password(fname, password):
    with open(fname,'rb') as f:
        with io.BytesIO() as b:
            ms = msoffcrypto.OfficeFile(f)
            ms.load_key(password=password)
            try:
                ms.decrypt(b)
                return True
            except msoffcrypto.exceptions.InvalidKeyError:
                return False


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Try each password against the provided file until a match is found",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("wordfile",type=str)
    parser.add_argument("passwords",type=str,nargs="*")
    args = parser.parse_args()

    def get_words():
        for word in args.passwords:
            yield word          # always yield, even '-'
            if word=='-':
                for line in sys.stdin:
                    yield line[:-1]


    for word in get_words():
        print(f"checking {word}")
        if check_password( args.wordfile, word):
            print(f"The password is '{word}'")
            exit(0)

    print("password not provided")
