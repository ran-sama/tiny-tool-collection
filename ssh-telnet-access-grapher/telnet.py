import socket, time, errno, sys

def writeLog(client):
    fopen = open('/media/kingdian/telnet.txt', 'a') # log directory
    fopen.write('%s\n'%(client[0]))
    fopen.close()

def main():
    print 'Starting telnet honeypot!'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 2323))
    s.listen(100)
    while True:
        (insock, address) = s.accept()
        sys.stdout.write('%s - %s:%d' % (time.ctime(), address[0], address[1]))
        writeLog(address)
        try:
            sent = 0
            totalsent = 0
            msg = "https://github.com/ran-sama" + "\n" #reply with a message
            MSGLEN = len(msg)
            while totalsent < MSGLEN:
                sent = insock.send(msg[totalsent:])
                if sent == 0:
                    sys.stdout.write(" [\033[91mFAILED\033[0m]")
                totalsent = totalsent + sent
            insock.shutdown(socket.SHUT_RDWR) # socket.SHUT_RDWR or 2
            insock.close()
        except socket.error, e:
            pass
            sys.stdout.write(' Error: %s' % (e))
            print(" [\033[93mDEPEND\033[0m]")
        else:
            print (" [  \033[92mOK\033[0m  ]")

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Bye!'
        exit(0)
    except BaseException, e:
        sys.stdout.write(' Base Exception: %s' % (e))
        exit(1)
