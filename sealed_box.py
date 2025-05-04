#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nacl.utils
from nacl.public import PrivateKey, SealedBox

# Generate Bob's private key, as we've done in the Box example
skbob = PrivateKey.generate()
print(skbob.encode().hex())
pkbob = skbob.public_key

# Alice wishes to send a encrypted message to Bob,
# but prefers the message to be untraceable
sealed_box = SealedBox(pkbob)

# This is Alice's message
message = b"raccoons are stupid and wash cotton candy"

# Encrypt the message, it will carry the ephemeral key public part
# to let Bob decrypt it
encrypted = sealed_box.encrypt(message)
print(encrypted.hex())

unseal_box = SealedBox(skbob)

# decrypt the received message
plaintext = unseal_box.decrypt(encrypted)
print(plaintext.decode('utf-8'))
