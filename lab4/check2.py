import base64
import hashlib
import pbkdf2
import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes


def test_password(word):
    # Values extracted from the XML block
    spinCount = 100000
    saltValue = base64.b64decode("cBIrkU+ElMoevZacEm4EOw==")
    encryptedVerifierHashInput = base64.b64decode("vMK+SnWZl5/S0a1Zzs6Gzw==")
    encryptedVerifierHashValue = base64.b64decode("mRdqS9DtcO0l+7ddkEPx93C9N1nwC1I/DXUIJsLKDzQ30/Zzetxhsz4nXij+TEwzEI83zFTBVAUezq7ubQkYvw==")
    encryptedKeyValue = base64.b64decode("bcLBCgPRdJXt2Ieri0L8Hvlfi4lVuasl9Qd66KyTj/I=")

    # Derive the encryption key from the password using PBKDF2
    key = PBKDF2(word.encode('utf-8'), saltValue, dkLen=32, count=spinCount, hmac_hash_module=SHA512)
    # key = pbkdf2.pbkdf2(hashlib.sha512, word.encode('utf-8'), saltValue, spinCount, 32)

    # Decrypt the encrypted verifier hash input
    cipher = AES.new(key, AES.MODE_CBC, iv=b'\x00' * 16)
    decryptedVerifierHashInput = cipher.decrypt(encryptedVerifierHashInput)

    # Decrypt the encrypted verifier hash value
    cipher = AES.new(key, AES.MODE_CBC, iv=b'\x00' * 16)
    decryptedVerifierHashValue = cipher.decrypt(encryptedVerifierHashValue)

    # Hash the decrypted verifier hash input
    verifierHash = hashlib.sha512(decryptedVerifierHashInput).digest()

    print("verifierHash=",verifierHash)
    print("decryptedVerifierHashValue:=",decryptedVerifierHashValue)

    # Check if the hash matches the decrypted verifier hash value
    if verifierHash[:len(decryptedVerifierHashValue)] == decryptedVerifierHashValue:
        return True
    else:
        return False

# Example usage:
password = "something"
if test_password(password):
    print("Password is correct!")
else:
    print("Password is incorrect.")
