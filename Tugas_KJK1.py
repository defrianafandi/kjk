#python3

import hashlib, binascii

text = "hello"
data = text.encode("utf8")

sha224hash = hashlib.sha224(data).digest()
sha384hash = hashlib.sha384(data).digest()
sha3_224hash = hashlib.sha3_224(data).digest()
sha3_384hash = hashlib.sha3_384(data).digest()

print("Text: ", text)
print("sha224 hash: ",binascii.hexlify(sha224hash))
print("sha384 hash: ",binascii.hexlify(sha384hash))
print("sha3-224 hash: ",binascii.hexlify(sha3_224hash))
print("sha3-384 hash: ",binascii.hexlify(sha3_384hash))