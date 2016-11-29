# coding utf-8
from phone_book_file_db import PhoneBookFileDb
import json
import settings


class PhoneBookFileDbJSON(PhoneBookFileDb):
    def save_phone_book_to_file(self, book):
        self.phone_number_dic = book.phone_number_dic
        if not self.is_actual():
            with open(settings.JSON_DB_DATA_FILE, 'w') as f:
                str_to_file = json.dumps(self.phone_number_dic)
                f.write(str_to_file)
                f.close()
                self.update_phone_db_state_hash()

    def load_phone_book_from_file(self, book):
        try:
            with open(settings.JSON_DB_DATA_FILE, 'r') as f:
                str_to_file = f.read()
                self.phone_number_dic = json.loads(str_to_file)
                book.phone_number_dic = self.phone_number_dic
                f.close()
        except:
            with open(settings.JSON_DB_DATA_FILE, 'w') as f:
                f.close()
