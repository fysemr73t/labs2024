import base64
from base64 import b64decode
import hashlib
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes

encryptedHmacKey=b64decode("P+axedQ02hhTVI92XV42jnmcdbJu+cL+4W+VCr0/gtUe9QMeWZRUOL8gf1hDsu7ea6IexbX8NR9QeYpeBroKVA==")
encryptedHmacValue=b64decode("06r9vzXBEnB9axvs/eIMtIK9s4pmrHZcTGaAr69IxZs3tLWrwF9d4Z6Xdry3lHokKDGLQ9+GW3ZB1OfXjQRCxQ==")
spinCount=int("100000")
saltSize=int("16")
blockSize=int("16")
keyBits=int("256")
hashSize=int("64")
cipherAlgorithm="AES"
cipherChaining="ChainingModeCBC"
hashAlgorithm="SHA512"
saltValue="Oz6n/QuqFYiwqdP0Eql1QQ=="
encryptedVerifierHashInput=b64decode("FuVgEZrxkp2MkLxe5SRiOw==")
encryptedVerifierHashValue=b64decode("r8csoFa4eM4u6seAlyjEQn5+x82xAYiWMJg/FkiKmedEaGw4wmXMLs4AUcwHowqGHUEPfk4lPjNZFWBKDn3+xA==")
encryptedKeyValue=b64decode("hCIAgW5aJQKydqRNhUB1UOms/T+jo5Gfz2ObGQJgfwc=")

def test_password(word):
    # Values extracted from the XML block

    # Derive the encryption key from the password using PBKDF2
    key = PBKDF2(word.encode('utf-8'), saltValue, dkLen=32, count=spinCount, hmac_hash_module=SHA512)

    # Decrypt the encrypted verifier hash input
    cipher = AES.new(key, AES.MODE_CBC, iv=b'\x00' * 16)
    decryptedVerifierHashInput = cipher.decrypt(encryptedVerifierHashInput)

    # Decrypt the encrypted verifier hash value
    cipher = AES.new(key, AES.MODE_CBC, iv=b'\x00' * 16)
    decryptedVerifierHashValue = cipher.decrypt(encryptedVerifierHashValue)

    # Hash the decrypted verifier hash input
    verifierHash = hashlib.sha512(decryptedVerifierHashInput).digest()

    print("verifierHash:",verifierHash)
    print("decryptedVerifierHashValue:",decryptedVerifierHashValue)

    # Check if the hash matches the decrypted verifier hash value
    if verifierHash[:len(decryptedVerifierHashValue)] == decryptedVerifierHashValue:
        return True
    else:
        return False

# Example usage:
if __name__=="__main__":
    test_password("password")
