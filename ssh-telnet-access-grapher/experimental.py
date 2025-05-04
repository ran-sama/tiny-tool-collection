import multiprocessing, socket, errno, sys

data = (
    [2222, 100], [2323, 100]
)

def mp_worker((my_port, my_queue)):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', my_port))
    s.listen(my_queue)
    while True:
        (insock, address) = s.accept()
        print(address[0])
        sys.stdout.flush()
        try:
            sent = 0
            totalsent = 0
            msg = "https://github.com/ran-sama" + "\n" #reply with a message
            MSGLEN = len(msg)
            while totalsent < MSGLEN:
                sent = insock.send(msg[totalsent:])
                if sent == 0:
                    pass
                totalsent = totalsent + sent
            insock.shutdown(socket.SHUT_RDWR) # socket.SHUT_RDWR or 2
            insock.close()
        except socket.error, e:
            pass
        else:
            pass

def mp_handler():
    p = multiprocessing.Pool(2)
    p.map(mp_worker, data)

if __name__ == '__main__':
    mp_handler()
