# coding utf-8
from phone_book.phone_book_view_controller import PhoneBookViewController

print 'Please choose what to do: '
choice = 2
controller = PhoneBookViewController()

while choice != 0:
    choice = PhoneBookViewController.print_menu()
    controller.start_action(choice)
else:
    print 'Good bye! :)'







