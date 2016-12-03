# coding utf-8
import re


class phonebook(object):
    def __init__(self):
        self.dict = {}

    def print_dict(self):
        print self.dict

    def is_subscriber_exists(self, subscriber):
        for item_contact in self.dict.values():
            if item_contact.subscriber_name == subscriber:
                return True
        raise NameError('No such subscriber')


    def is_msisdn_exists(self, phone):
        try:
            return self.dict[phone]
        except KeyError:
            raise NameError('No such subscriber')


    def add_new_subscriber(self, contact):
        self.dict[contact.phone_number] = contact


    def get_phone_book_dict(self):
        return self.dict

    def load_phone_book_from_dict(self, dict):
        self.dict = dict

    def get_subscriber_by_phone(self, phone_number):
        return  self.is_msisdn_exists(phone_number).subscriber_name


    def get_phone_by_subscriber(self, subscriber):
        for value in self.dict.values():
            if value.subscriber_name_starts_with(subscriber):
                return value.phone_number


    def delete_customer_by_name(self, subscriber):
        for value in self.dict.values():
            if value.subscriber_name_starts_with(subscriber):
                del self.dict[value.contact.phone_number]


class PhoneBookContact(object):
    def __init__(self, phone_number, subscriber_name, address=''):
        self.phone_number = self._verify_phone_number(phone_number)
        self.subscriber_name = subscriber_name
        self.address = address

    def _verify_phone_number(self, phone_number):
        r = re.match(r'(?P<phone>^38(\d{3})\d{7}$)', phone_number)
        if r is not None:
            self.phone_number = r.groupdict()['phone']
            return self.phone_number
        raise ValueError('Incorect phone number')

    def phone_starts_with(self, phone_number_part):
        if phone_number_part in self.phone_number:
            return self

    def subscriber_name_starts_with(self, subscriber_name_part):
        if subscriber_name_part in self.subscriber_name:
            return self

    def get_object_to_save(self):
        print self.__dict__

    def __repr__(self):
        return '{}:{}, {}'.format(self.subscriber_name, self.phone_number, self.address)

    def __getitem__(self, item):
        return self.phone_starts_with(item)





















a = PhoneBookContact('380632107523', 'User1')
b = PhoneBookContact('380632104444','Customer', 'Kiev')




list1  = phonebook()



a.get_object_to_save()
a.phone_starts_with('3806321')
a.subscriber_name_starts_with('User')