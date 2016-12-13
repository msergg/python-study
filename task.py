# coding utf-8
from phone_book.phone_book_view_controller import PhoneBookViewController

from phone_book.phone_book_view_controller_network import PhoneBookViewControllerNet
import phone_book.settings



import socket
import threading

is_finished = False




def handle(c):
    while not is_finished:
        controller = PhoneBookViewControllerNet()
        choice = phone_book.settings.DEFAULT_CHOICE
        controller.set_socket(c)


        while choice != phone_book.settings.EXIT:
            choice = controller.print_menu()
            controller.start_action(choice)

        controller.print_to_socket('Good bye! :)')

        c.close()
        break




s = socket.socket()

s.bind(('0.0.0.0', 8021))

s.listen(5)
print "Server started"




try:
    while True:
        c, a = s.accept()
        print "Connected", a
        t = threading.Thread(target=handle, args=(c, ))
        t.start()


except KeyboardInterrupt:
    is_finished = True

















