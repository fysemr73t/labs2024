import msoffcrypto
import sys
import io

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
    print(check_password(sys.argv[1],sys.argv[2]))
