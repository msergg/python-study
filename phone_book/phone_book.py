# coding utf-8

class PhoneBook(object):
    def __init__(self):
        self.phone_number_dic = {}

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
        """Create phone number"""
        self.phone_number_dic[phone_number] = subscriber

    def get_phone_book_dict(self):
        return self.phone_number_dic

    def load_phone_book_from_dict(self, dict):
        self.phone_number_dic = dict

    def get_subscriber_by_phone(self, phone_number):
        """Get customer name by phone"""
        self.is_msisdn_exists(phone_number)
        return self.phone_number_dic[phone_number]

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

