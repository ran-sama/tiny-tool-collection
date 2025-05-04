#!/usr/bin/env python3
import socket, sys, paramiko
from datetime import datetime

#ssh-keygen -t dsa -f paramiko-dss.key
#ssh-keygen -t rsa -b 2048 -f paramiko-rsa.key
#ssh-keygen -t ed25519 -f paramiko-ed25519.key

LOGFILE = 'dump2.log'

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
            print("{}\t{}\t{}\t{}".format(datetime.now().isoformat(' ', 'seconds'), self.client_address[0], username, password))
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
        MY_KEY = paramiko.RSAKey(filename='/home/ran/paramiko-rsa.key')
        #MY_KEY = paramiko.DSSKey(filename='/home/ran/paramiko-dss.key')
        #MY_KEY = paramiko.ed25519key.Ed25519Key(filename='/home/ran/paramiko-ed25519.key')
        transport.add_server_key(MY_KEY)
        transport.local_version = "SSH-2.0-OpenSSH_9.3p1 Ubuntu-1ubuntu3"
        server_handler = SSHServerHandler(client_addr)
        transport.start_server(server=server_handler)
        channel = transport.accept(1)
        if not channel is None:
            channel.close()
    except Exception as e:
        print("ERROR: Connection was handled improperly.")
        print(e)

def main():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', 2222))
        server_socket.listen(100)
        paramiko.util.log_to_file ('paramiko2.log') 
        while(True):
            try:
                client_socket, client_addr = server_socket.accept()
                handleConnection(client_socket, client_addr)
            except Exception as e:
                print("ERROR: Client handling")
                print(e)
    except Exception as e:
        print("ERROR: Failed to create socket")
        print(e)
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
