import json
import hashlib


class PhoneBook(object):
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
        """Create phone number"""
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