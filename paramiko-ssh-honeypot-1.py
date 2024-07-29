#!/usr/bin/env python3
import socket, sys, paramiko
from datetime import datetime

#ssh-keygen -t dsa -f paramiko-dss.key
#ssh-keygen -t ecdsa -f paramiko-ecdsa.key
#ssh-keygen -t rsa -b 2048 -f paramiko-rsa.key
#ssh-keygen -t ed25519 -f paramiko-ed25519.key

LOGFILE = 'dump1.log'

class SSHServerHandler(paramiko.ServerInterface):
    def __init__(self, client_address):
        self.client_address = client_address
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    def check_auth_password(self, username, password):
        try:
            logfile_handle = open(LOGFILE,"a")
            print("{}\t{}\t{}\t{}".format(datetime.now().isoformat(' ', 'seconds'), self.client_address[0], username, password), end='', flush=True)
            logfile_handle.write("{}\t{}\t{}\t{}".format(datetime.now().isoformat(' ', 'seconds'), self.client_address[0], username, password + "\n"))
            logfile_handle.close()
        finally:
            pass
        return paramiko.AUTH_FAILED
    #allow password authentication only
    def get_allowed_auths(self, username):
        return 'password'

def handleConnection(client_socket, client_addr):
    try:
        transport = paramiko.Transport(client_socket)
        #MY_KEY = paramiko.RSAKey.generate(bits=2048)
        #MY_KEY = paramiko.RSAKey(filename='/home/ran/paramiko-rsa.key')
        #MY_KEY = paramiko.DSSKey(filename='/home/ran/paramiko-dss.key')
        MY_KEY = paramiko.ecdsakey.ECDSAKey(filename='/home/ran/paramiko-ecdsa.key')
        #MY_KEY = paramiko.ed25519key.Ed25519Key(filename='/home/ran/paramiko-ed25519.key')
        transport.add_server_key(MY_KEY)
        transport.local_version = "SSH-2.0-OpenSSH_9.3p1 Ubuntu-1ubuntu3"
        server_handler = SSHServerHandler(client_addr)
        try:
            transport.start_server(server=server_handler)
        except:
            sys.stderr.write("[-] Error: SSH Negotation failed.\n")
            return
        channel = transport.accept(20)
        print("", transport.remote_version, end='\n', sep='\t', flush=True)
        if channel is None:
            transport.close()
            return
        #No need for this since the client will never authenticate
        server_handler.event.wait()
        if not server_handler.event.is_set():
            transport.close()
            return
        channel.close()
    except:
        sys.stderr.write("[-] There was an error generating a new connection.\n")
        transport.close()

def start_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', 2222))
    except:
        sys.stderr.write("[-] Failed to create and bind a new socket.\n")
        sys.exit(1)
    while True:
        try:
            server_socket.listen(100)
            paramiko.util.log_to_file ('/dev/null', level = "ERROR") 
            client_socket, client_addr = server_socket.accept()
        except:
            sys.stderr.write("[-] Failed to create listen socket or accept the connection from the client.\n")
        handleConnection(client_socket, client_addr)

def main():
    try:
        start_server()
    except (KeyboardInterrupt, SystemExit) as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
