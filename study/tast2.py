# coding utf-8
#from phone_book.phone_book_view_controller import PhoneBookViewController

from phone_book.phone_book_view_controller_network import PhoneBookViewControllerNet
import phone_book.settings



import socket
import select





is_finished = False

def handle(c):
    controller = PhoneBookViewControllerNet()
    choice = phone_book.settings.DEFAULT_CHOICE

    controller.set_socket(c)


    while choice != phone_book.settings.EXIT:
        choice = controller.print_menu()
        controller.start_action(choice)

    controller.print_to_socket('Good bye! :)')

    c.close()
    connections.remove(c)












s = socket.socket()

s.bind(('0.0.0.0', 8015))

s.listen(5)

s.setblocking(False)

connections = [s]

try:
    while True:
        reading_sockets, _, _ = select.select(connections, [], [])

        for reading_socket in reading_sockets:
            if reading_socket == s:
                c, a = s.accept()
                connections.append(c)
                print "Connected", a
                handle(c)
            else:
                handle(reading_socket)

except KeyboardInterrupt:
    is_finished = True

































