"""
TEST PROJECT

CRUD
"""


def try_is_customer_exists(func):
    def wrapper(self, *args):
        try:
            return func(self, *args)
        except NameError as e:
            print e
    return wrapper


class phone_book(object):
    def __init__(self):
        self.phone_number_dic = {}

    def add_new_subscriber(self, phone_number, subscriber):
        self.phone_number_dic[phone_number] = subscriber

    def get_phone_book(self):
        return self.phone_number_dic

    @try_is_customer_exists
    def get_subscriber_by_phone(self, phone_number):
        subscriber = self.phone_number_dic[phone_number]
        if not subscriber:
            raise NameError('NoSubscriber')
        return subscriber

    @try_is_customer_exists
    def get_phone_by_subscriber(self, subscriber):
        for item_phone, item_customer in self.phone_number_dic.items():
            if item_customer == subscriber:
                return (item_phone, item_customer)
        raise NameError('NoSubscriber')

    @try_is_customer_exists
    def delete_customer_by_name(self, subscriber):
        for item_phone, item_customer in self.phone_number_dic.items():
            if item_customer == customer:
                del self.phone_number_dic[item_phone]

        raise NameError('NoSubscriber')





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











book = phone_book()


print 'Please choose what to do: '
choice = 2


while choice != 0:

    choice = print_menu()


    """Create phone number'"""
    if choice == 1:
        print '1. Please input phone number: '
        phone_number = raw_input()
        print '2. Please input customer name: '
        customer = raw_input()

        book.add_new_subscriber(phone_number, customer)


    """Get phone number by name"""
    if choice == 2:
        print '1. Please input customer name: '
        customer = raw_input()


        subscriber_item = book.get_phone_by_subscriber(customer)
        print '{}:{}'.format(subscriber_item[0],subscriber_item[1])


    """Get customer name by phone"""

    if choice == 3:
        print '1. Please input msisdn: '
        phone_number = raw_input()

        result = book.get_subscriber_by_phone(phone_number)



    """Delete phone number by name"""

    if choice == 4:
        print '1. Please input customer name to delete: '
        subscriber = raw_input()

        result = book.delete_customer_by_name(subscriber)

        if result == 1:
            print 'Subscribers {} phone deleted'.format(subscriber)
        else:
            print 'There is no such subscriber'

    """Show all phones on a book"""
    if choice == 5:
        dic = book.get_phone_book()
        for phone, name in dic.items():
            print '{}:{}'.format(name, phone)








    print '-----------------------------------------------------------------'



















