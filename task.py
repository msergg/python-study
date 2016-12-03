# coding utf-8
from phone_book.phone_book_view_controller import PhoneBookViewController
import phone_book.settings

print 'Please choose what to do: '
choice = phone_book.settings.DEFAULT_CHOICE

controller = PhoneBookViewController()

while choice != phone_book.settings.EXIT:
    choice = PhoneBookViewController.print_menu()
    controller.start_action(choice)
else:
    print 'Good bye! :)'







