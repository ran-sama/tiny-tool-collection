#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio, re, ssl

#generate: openssl req -new -x509 -nodes -newkey ec:<(openssl ecparam -name secp384r1) -keyout cert.key -out cert.crt -days 3650
#MYSERV_CLIENTCRT = "/home/ran/net/dummy/client.pem"
MYSERV_FULLCHAIN = "/home/ran/net/dummy/cert.crt"
MYSERV_PRIVKEY = "/home/ran/net/dummy/secret.key"

global sslcontext
sslcontext = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
sslcontext.options |= ssl.OP_NO_TLSv1
sslcontext.options |= ssl.OP_NO_TLSv1_1
#sslcontext.options |= ssl.OP_NO_TLSv1_2
#sslcontext.protocol = ssl.PROTOCOL_TLS
#sslcontext.verify_mode = ssl.CERT_REQUIRED
sslcontext.set_ciphers("ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305")
sslcontext.set_ecdh_curve("secp384r1")
#sslcontext.load_verify_locations(MYSERV_CLIENTCRT)
sslcontext.load_cert_chain(MYSERV_FULLCHAIN, MYSERV_PRIVKEY)

async def handler(reader, writer):
    try:
        while True:
            line = await reader.readline()
            if line:
                line = line.decode('latin1').partition('\r\n')[0]
                if re.match(r"^CONNECT.*|^DELETE.*|^GET.*|^HEAD.*|^OPTIONS.*|^PATCH.*|^POST.*|^PUT.*|^TRACE.*", line):
                    print(line)
            else:
                break
            writer.close()
    except ConnectionResetError:
        pass

async def main():
    server = await asyncio.start_server(handler, '0.0.0.0', 7891, ssl=sslcontext)
    async with server:
        await server.serve_forever()

asyncio.run(main())
