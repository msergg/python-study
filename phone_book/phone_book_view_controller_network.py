# coding utf-8
from phone_book import PhoneBook
from phone_book_sqlite import PhoneBookSQLite
from config import ConfigParameters

import settings

class PhoneBookViewControllerNet(object):
    def __init__(self, filedb = False):

        self.filedb = filedb

        if self.filedb:
            self.book = PhoneBook()
            config = ConfigParameters()
            self.phone_book_file_db = config.get_phone_book_file_db()
            dict = self.phone_book_file_db.load_phone_book_from_file()

            self.book.load_phone_book_from_dict(dict)

        else:
            self.book = PhoneBookSQLite()






        self.controller = {1: self._create_phone_number,
                           2: self._get_phone_by_name,
                           3: self._get_customer_by_phone,
                           4: self._delete_by_name,
                           5: self._show_all}


    def set_socket(self, socket):
        self.socket = socket


    def print_to_socket(self, text):
        self.socket.sendall(str(text + '\n'))

    def socket_input(self, bytes=1024):
        return str(self.socket.recv(bytes)).strip()


    def print_menu(self):
        CRUD_DICT = {1: 'Create phone number',
                     2: 'Get phone number by name',
                     3: 'Get customer name by phone',
                     4: 'Delete phone number by name',
                     5: 'Show all phones on a book',
                     0: 'Exit'}

        for i, text in CRUD_DICT.items():
            self.print_to_socket(str(str(i) + " : " + text ))

        try:

            # choice = int(raw_input('Input your choice:'))
            choice = int(self.socket_input())
        except ValueError:
            self.print_to_socket('Wrong input!')
            choice = settings.DEFAULT_CHOICE

        return choice

    def catch_name_error(func):
        def wrapper(self, *args):
            try:
                return func(self, *args)
            except NameError as e:
                self.print_to_socket(str(e))
            # except:
            #      self.print_to_socket('ERROR!')

        return wrapper

    @catch_name_error
    def start_action(self, choice):
        self.controller.get(choice, self._default_choice)()

        if self.filedb:
            self.phone_book_file_db.save_phone_book_to_file(self.book)

    
    def _input_phone_number(self):
        phone_number = str(self.socket_input())

        while not phone_number.isdigit():
            self.print_to_socket('WARN Inocrrect msisdn. Please retry.')
            phone_number = str(self.socket_input())
        return phone_number

    def _default_choice(self):
        pass

    def _create_phone_number(self):
        self.print_to_socket('1. Please input phone number: ')
        phone_number = self._input_phone_number()
        self.print_to_socket('2. Please input customer name: ')
        customer = self.socket_input()
        phone_number_unicode = phone_number.decode('utf-8')
        customer_unicode = customer.decode('utf-8')
        self.book.add_new_subscriber(phone_number_unicode, customer_unicode)
        self.print_to_socket("OK.")

    def _get_phone_by_name(self):
        self.print_to_socket('1. Please input customer name: ')
        customer = self.socket_input()
        print customer
        customer_unicode = customer.decode('utf-8')
        subscriber_item = self.book.get_phone_by_subscriber(customer_unicode)
        item_0_u = subscriber_item[0].center(settings.CENTER_WIDTH).encode('utf-8')
        item_1_u = subscriber_item[1].center(settings.CENTER_WIDTH).encode('utf-8')
        try:
            self.print_to_socket('|------Subscriber------|-----Phone number-----|')
            self.print_to_socket('| {}|{} |'.format(item_0_u, item_1_u))
            self.print_to_socket('|----------------------|----------------------|')
        except TypeError:
            pass

    def _get_customer_by_phone(self):
        self.print_to_socket('1. Please input msisdn: ')
        phone_number = self._input_phone_number()
        phone_number_u = phone_number.decode('utf-8')
        try:
            subscriber = self.book.get_subscriber_by_phone(phone_number_u)
            phone_number_unicode = phone_number.center(settings.CENTER_WIDTH).decode('utf-8')
            subscriber_unicode = subscriber.center(settings.CENTER_WIDTH).decode('utf-8')
            self.print_to_socket('|------Subscriber------|-----Phone number-----|')
            self.print_to_socket('| {}|{} |'.format(subscriber_unicode, phone_number_unicode))
            self.print_to_socket('|----------------------|----------------------|')
        except NameError:
            pass

    def _delete_by_name(self):
        self.print_to_socket('1. Please input customer name to delete: ')
        subscriber = self.socket_input()
        self.book.delete_customer_by_name(subscriber.decode('utf-8'))
        self.print_to_socket('Subscribers {} phone deleted'.format(subscriber))

    def _show_all(self):
        dic = self.book.get_phone_book_dict()
        self.print_to_socket('|------Subscriber------|-----Phone number-----|')

        for phone, name in dic.items():
            name_pre_utf = name.center(settings.CENTER_WIDTH).encode('utf-8')
            phone_pre_utf = phone.center(settings.CENTER_WIDTH).encode('utf-8')
            self.print_to_socket('| {}|{} |'.format(name_pre_utf, phone_pre_utf))
        self.print_to_socket('|----------------------|----------------------|')
