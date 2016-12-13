import socket
import time
s = socket.socket()
s.connect(('10.132.14.62', 8000))
# s.connect(('127.0.0.1', 8000))

while True:
    s.sendall('Hello Vlad OLOLO 1')
    data = s.recv(1024)

    print data
    # time.sleep(1)



