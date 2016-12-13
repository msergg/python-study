# import socket
# import threading
#
# is_finished = False
#
# def handle(c):
#     while not is_finished:
#         data = c.recv(1024)
#         if not data:
#             s.close()
#             break
#         print data
#         c.sendall(data)
#
#
#
#
# s = socket.socket()
#
# s.bind(('0.0.0.0', 8000))
#
# s.listen(5)
# print "Server started"
#
#
#
#
# try:
#     while True:
#         c, a = s.accept()
#         print "Connected", a
#         t = threading.Thread(target=handle, args=(c,))
#         t.start()
# except KeyboardInterrupt:
#     is_finished = True
#
#
#
#
#








import socket
import select



def handle(c):
    data = c.recv(1024)
    if not data:
        connections.remove(c)
        c.close()
        return
    print data
    c.sendall(data)


# tornado
# reactor (twitsted)



s = socket.socket()

s.bind(('0.0.0.0', 8000))

s.setblocking(False)
s.listen(5)


print "Server started"

connections = [s]


while True:
    reading_sockets, _, _ = select.select(connections, [], [])

    for reading_socket in reading_sockets:
        if reading_socket == s:
            c, a = s.accept()
            connections.append(c)
            print "Connected", a

        else:
            handle(reading_socket)






