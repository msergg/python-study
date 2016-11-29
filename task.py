# coding utf-8
from phone_book.phone_book_view_controller import PhoneBookViewController
from phone_book.config import ConfigParameters

config = ConfigParameters()
phone_book_file_db = config.get_phone_book_file_db()

print 'Please choose what to do: '
choice = 2
controller = PhoneBookViewController(phone_book_file_db)

while choice != 0:
    choice = controller.print_menu()
    controller.start_action(choice)
else:
    print 'Good bye! :)'







