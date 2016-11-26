import json
import hashlib

class PhoneBookFileDb(object):
    def __init__(self):
        self.phone_number_dic = {}
        self.phone_db_state_hash = ''
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

    def save_phone_book_to_file(self, book):
        self.phone_number_dic = book.phone_number_dic
        if not self.is_actual():
            with open("phonebook.db", 'w') as f:
                str_to_file = json.dumps(self.phone_number_dic)
                f.write(str_to_file)
                f.close()
                self.update_phone_db_state_hash()

    def load_phone_book_from_file(self, book):
        try:
            with open("phonebook.db", 'r') as f:
                str_to_file = f.read()
                self.phone_number_dic = json.loads(str_to_file)
                book.phone_number_dic = self.phone_number_dic
                f.close()
        except:
            with open("phonebook.db", 'w') as f:
                f.close()






