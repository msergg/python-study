# coding utf-8

import json
import hashlib


class phone_book(object):
    def __init__(self):
        self.phone_number_dic = {}
        self.phone_db_state_hash = ''

        try:
            self.load_phone_book_to_file()
        except:
            print 'ERROR Can`t read phonebookDB! Created new empty db.'
            self.phone_number_dic = {}
        self.update_phone_db_state_hash()

    def _get_phone_db_state_hash_now(self):
        return hashlib.sha1(json.dumps(self.phone_number_dic)).hexdigest()

    def _get_phone_db_state_hash_last(self):
        return self.phone_db_state_hash

    def update_phone_db_state_hash(self):
        self.phone_db_state_hash = self._get_phone_db_state_hash_now()

    def is_actual(self):
        return self._get_phone_db_state_hash_last() == \
               self._get_phone_db_state_hash_now()

    def save_phone_book_to_file(self):
        # Need to add implementation not to save if file was not changed
        if not self.is_actual():
            with open("phonebook.db", 'w') as f:
                str_to_file = json.dumps(self.phone_number_dic)
                f.write(str_to_file)
                f.close()
                self.update_phone_db_state_hash()

    def load_phone_book_to_file(self):
        with open("phonebook.db", 'r') as f:
            str_to_file = f.read()
            self.phone_number_dic = json.loads(str_to_file)
            f.close()

    def is_subscriber_exists(self, subscriber):
        for item_phone, item_customer in self.phone_number_dic.items():
            if item_customer == subscriber:
                return True
        raise NameError('No such subscriber')

    def is_msisdn_exists(self, msisdn):
        try:
            test = self.phone_number_dic[msisdn]
        except KeyError:
            raise NameError('No such subscriber')

    def add_new_subscriber(self, phone_number, subscriber):
        """Create phone number'"""
        self.phone_number_dic[phone_number] = subscriber

    def get_phone_book(self):
        return self.phone_number_dic

    def get_subscriber_by_phone(self, phone_number):
        """Get customer name by phone"""
        self.is_msisdn_exists(phone_number)
        subscriber = self.phone_number_dic[phone_number]
        return subscriber

    def get_phone_by_subscriber(self, subscriber):
        """Get phone number by name"""
        self.is_subscriber_exists(subscriber)
        for item_phone, item_customer in self.phone_number_dic.items():
            if item_customer == subscriber:
                return (item_phone, item_customer)

    def delete_customer_by_name(self, subscriber):
        """Delete phone number by name"""
        self.is_subscriber_exists(subscriber)
        for item_phone, item_customer in self.phone_number_dic.items():
            if item_customer == subscriber:
                del self.phone_number_dic[item_phone]
                return
        raise NameError('No such subscriber')


class phone_book_view_controller(object):
    def __init__(self):
        self.book = phone_book()
        self.controller = {1: self._create_phone_number,
                           2: self._get_phone_by_name,
                           3: self._get_customer_by_phone,
                           4: self._delete_by_name,
                           5: self._show_all}

    def print_menu(self):
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
            except:
                print 'ERRROR!'

        return wrapper

    @catch_name_error
    def start_action(self, choice):
        self.controller.get(choice, self._default_choice)()

    def _input_phone_number(self):
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
        item_0_u = subscriber_item[0].encode('utf-8')
        item_1_u = subscriber_item[1].encode('utf-8')
        try:
            print '{}:{}'.format(item_0_u, item_1_u)
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

print 'Please choose what to do: '
choice = 2
controller = phone_book_view_controller()

while choice != 0:
    choice = controller.print_menu()
    controller.start_action(choice)
    controller.book.save_phone_book_to_file()
    print '-----------------------------------------------------------------'
