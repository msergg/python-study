# coding utf-8
from phone_book import PhoneBook
from phone_book_file_db_json import PhoneBookFileDbJSON
from phone_book_file_db_csv import PhoneBookFileDbCSV
from config import ConfigParameters


class PhoneBookViewController(object):
    def __init__(self):

        self.config = ConfigParameters()

        file_type = self.config.get_file_type_value()
        self.book = PhoneBook()

        if file_type == 'csv':
            self.phone_book_file_db = PhoneBookFileDbCSV()
        else:
            self.phone_book_file_db = PhoneBookFileDbJSON()

        self.phone_book_file_db.load_phone_book_from_file(self.book)

        self.controller = {1: self._create_phone_number,
                           2: self._get_phone_by_name,
                           3: self._get_customer_by_phone,
                           4: self._delete_by_name,
                           5: self._show_all}

    @staticmethod
    def print_menu():
        CRUD_DICT = {1: 'Create phone number',
                     2: 'Get phone number by name',
                     3: 'Get customer name by phone',
                     4: 'Delete phone number by name',
                     5: 'Show all phones on a book',
                     0: 'Exit'}

        for i, text in CRUD_DICT.items():
            print str(i) + " : " + text

        try:
            choice = int(raw_input('Input your choice:'))
        except ValueError:
            print 'Wrong input!'
            choice = 9999

        return choice

    def catch_name_error(func):
        def wrapper(self, *args):
            try:
                return func(self, *args)
            except NameError as e:
                print e
            # except:
            #     print 'ERRROR!'

        return wrapper

    @catch_name_error
    def start_action(self, choice):
        self.controller.get(choice, self._default_choice)()
        print '----------------------------------------------'
        self.phone_book_file_db.save_phone_book_to_file(self.book)

    @staticmethod
    def _input_phone_number():
        phone_number = str(raw_input())

        while not phone_number.isdigit():
            print 'WARN Inocrrect msisdn. Please retry.'
            phone_number = str(raw_input())
        return phone_number

    def _default_choice(self):
        pass

    def _create_phone_number(self):
        print '1. Please input phone number: '
        phone_number = self._input_phone_number()
        print '2. Please input customer name: '
        customer = raw_input()
        phone_number_unicode = phone_number.decode('utf-8')
        customer_unicode = customer.decode('utf-8')
        self.book.add_new_subscriber(phone_number_unicode, customer_unicode)
        print "OK."

    def _get_phone_by_name(self):
        print '1. Please input customer name: '
        customer = raw_input()
        customer_unicode = customer.decode('utf-8')
        subscriber_item = self.book.get_phone_by_subscriber(customer_unicode)
        item_0_u = subscriber_item[0].center(21).encode('utf-8')
        item_1_u = subscriber_item[1].center(21).encode('utf-8')
        try:
            print '|------Subscriber------|-----Phone number-----|'
            print '| {}|{} |'.format(item_0_u, item_1_u)
            print '|----------------------|----------------------|'
        except TypeError:
            pass

    def _get_customer_by_phone(self):
        print '1. Please input msisdn: '
        phone_number = self._input_phone_number()
        phone_number_u = phone_number.decode('utf-8')
        try:
            subscriber = self.book.get_subscriber_by_phone(phone_number_u)
            print subscriber
        except NameError:
            pass

    def _delete_by_name(self):
        print '1. Please input customer name to delete: '
        subscriber = raw_input()
        self.book.delete_customer_by_name(subscriber.decode('utf-8'))
        print 'Subscribers {} phone deleted'.format(subscriber)

    def _show_all(self):
        dic = self.book.get_phone_book()
        print '|------Subscriber------|-----Phone number-----|'

        for phone, name in dic.items():
            name_pre_utf = name.center(21).encode('utf-8')
            phone_pre_utf = phone.center(21).encode('utf-8')
            print '| {}|{} |'.format(name_pre_utf, phone_pre_utf)
        print '|----------------------|----------------------|'
