import json
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import ChaCha20_Poly1305
from Crypto.Random import get_random_bytes

#nonce_xchacha20 = get_random_bytes(24)
nonce_xchacha20 = b64decode("QEFCQ0RFRkdISUpLTE1OT1BRUlNUVVZX")

#header = b"header"
header = b64decode("UFFSU8DBwsPExcbH")
plaintext = b"Ladies and Gentlemen of the class of '99: If I could offer you only one tip for the future, sunscreen would be it."
#key = get_random_bytes(32)
key = b64decode("gIGCg4SFhoeIiYqLjI2Oj5CRkpOUlZaXmJmam5ydnp8=")
cipher = ChaCha20_Poly1305.new(key=key, nonce=nonce_xchacha20)
cipher.update(header)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

jk = [ 'nonce', 'header', 'ciphertext', 'tag' ]
jv = [ b64encode(x).decode('utf-8') for x in (nonce_xchacha20, header, ciphertext, tag) ]
result = json.dumps(dict(zip(jk, jv)))
print(result)

# We assume that the key was securely shared beforehand
try:
    b64 = json.loads(result)
    jk = [ 'nonce', 'header', 'ciphertext', 'tag' ]
    jv = {k:b64decode(b64[k]) for k in jk}

    cipher = ChaCha20_Poly1305.new(key=key, nonce=jv['nonce'])
    cipher.update(jv['header'])
    plaintext = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])
    print("The message was: " + plaintext.decode('utf8'))
except (ValueError, KeyError):
    print("Incorrect decryption")
