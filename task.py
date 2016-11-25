"""
TEST PROJECT

CRUD
"""
import json
import hashlib

#---------------------------------------------------------------------------------------------------------------------
def try_is_customer_exists(func):
    def wrapper(self, *args):
        try:
            return func(self, *args)
        except NameError as e:
            print e
        except:
            print 'ERRROR!'
    return wrapper
#---------------------------------------------------------------------------------------------------------------------
def print_menu():
    CRUD_DICT = {1: 'Create phone number', 2: 'Get phone number by name',
                 3: 'Get customer name by phone', 4: 'Delete phone number by name',
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
#---------------------------------------------------------------------------------------------------------------------
def input_phone_number():
    phone_number = str(raw_input())

    while not phone_number.isdigit():
        print 'WARN Inocrrect msisdn. Please retry.'
        phone_number = str(raw_input())
    return phone_number
#---------------------------------------------------------------------------------------------------------------------
class phone_book(object):
    def __init__(self):
        self.phone_number_dic = {}
        self.phone_db_state_hash = ''

        try:
            self.load_phone_book_to_file()
        except:
            print 'ERROR Can`t read phonebookDB!'
            self.phone_number_dic = {}
        self.update_phone_db_state_hash()



    def _get_phone_db_state_hash_now(self):
        return hashlib.sha1(json.dumps(self.phone_number_dic)).hexdigest()

    def _get_phone_db_state_hash_last(self):
        return self.phone_db_state_hash

    def update_phone_db_state_hash(self):
        self.phone_db_state_hash = self._get_phone_db_state_hash_now()

    def is_actual(self):
        return self._get_phone_db_state_hash_last() == self._get_phone_db_state_hash_now()


    def save_phone_book_to_file(self):
        # Need to add implementation not to save if file was not changed
        if not self.is_actual():
            f = open("phonebook.db", 'w')
            str_to_file = json.dumps(self.phone_number_dic)
            f.write(str_to_file)
            f.close()
            self.update_phone_db_state_hash()



    def load_phone_book_to_file(self):
        f = open("phonebook.db", 'r')
        str_to_file = f.read()
        self.phone_number_dic = json.loads(str_to_file)
        f.close()

    def add_new_subscriber(self, phone_number, subscriber):
        """Create phone number'"""
        self.phone_number_dic[phone_number] = subscriber

    def get_phone_book(self):
        return self.phone_number_dic

    @try_is_customer_exists
    def get_subscriber_by_phone(self, phone_number):
        """Get customer name by phone"""
        try:
            subscriber = self.phone_number_dic[phone_number]
            return subscriber
        except:
            raise NameError('No such subscriber')


    @try_is_customer_exists
    def get_phone_by_subscriber(self, subscriber):
        """Get phone number by name"""
        for item_phone, item_customer in self.phone_number_dic.items():
            if item_customer == subscriber:
                return (item_phone, item_customer)
        raise NameError('No such subscriber')

    @try_is_customer_exists
    def delete_customer_by_name(self, subscriber):
        """Delete phone number by name"""
        for item_phone, item_customer in self.phone_number_dic.items():
            if item_customer == subscriber:
                del self.phone_number_dic[item_phone]
                return ### FIX!!
        raise NameError('No such subscriber')
#---------------------------------------------------------------------------------------------------------------------

book = phone_book()

print 'Please choose what to do: '
choice = 2

#---------------------------------------------------------------------------------------------------------------------

while choice != 0:

    choice = print_menu()


    """Create phone number'"""
    if choice == 1:
        print '1. Please input phone number: '
        phone_number = input_phone_number()
        print '2. Please input customer name: '
        customer = raw_input()

        book.add_new_subscriber(phone_number, customer)

        print "OK."


    """Get phone number by name"""
    if choice == 2:
        print '1. Please input customer name: '
        customer = raw_input()

        subscriber_item = book.get_phone_by_subscriber(customer)

        try:
            print '{}:{}'.format(subscriber_item[0],subscriber_item[1])
        except TypeError:
            pass



    """Get customer name by phone"""
    if choice == 3:
        print '1. Please input msisdn: '
        phone_number = input_phone_number()

        try:
            subscriber = book.get_subscriber_by_phone(phone_number)
        except TypeError:
            pass




    """Delete phone number by name"""
    if choice == 4:
        print '1. Please input customer name to delete: '
        subscriber = raw_input()

        try:
            book.delete_customer_by_name(subscriber)
            print 'Subscribers {} phone deleted'.format(subscriber)
        except TypeError:
            pass





    """Show all phones on a book"""
    if choice == 5:
        dic = book.get_phone_book()
        for phone, name in dic.items():
            print '{}:{}'.format(name, phone)



    print book.phone_db_state_hash
    book.save_phone_book_to_file()


    print '-----------------------------------------------------------------'














# Need to do
#
# def f_a():
#     print 'Func a'
#
#
# def f_b():
#     print 'Func b'
#
#
# def f_c():
#     print 'Func c'
#
#
# action = raw_input('?')
#
#
#
# d = {'a': f_a, 'b': f_b, 'c': f_c}
#
# def default():
#     print 'Default'
#
# d.get(action, default)()



# Make phone_number_dic and object contains dictionary





