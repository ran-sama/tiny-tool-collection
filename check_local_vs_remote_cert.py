#!/usr/bin/python3
# -*- coding: utf-8 -*-
import ssl, binascii
from cryptography import x509

def ski_extractor(domain, port):
    pem_text = ssl.get_server_certificate((domain, port))
    pem_bytes = bytes(pem_text, 'utf-8')
    loaded_pem = x509.load_pem_x509_certificate(pem_bytes)
    ski_object = x509.SubjectKeyIdentifier.from_public_key(loaded_pem.public_key())
    digest_string = binascii.hexlify(bytearray(ski_object.digest)).decode('utf-8')
    return digest_string

def ski_matcher(remote, local, port):
    local_hash = ski_extractor(local, port)
    remote_hash = ski_extractor(remote, 443)
    print(remote, local_hash == remote_hash, "got " + remote_hash)

#checks the certificate found online against the cert stored locally
#useless code because no one really can make issue a second cert from a different CA other than a goverment
ski_matcher('example.com', '10.0.0.16', 443)
