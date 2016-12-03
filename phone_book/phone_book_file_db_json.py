# coding utf-8
from phone_book_file_db import PhoneBookFileDb
import json
import settings


class PhoneBookFileDbJSON(PhoneBookFileDb):
    def save_phone_book_to_file(self, phone_book):
        with open(settings.JSON_DB_DATA_FILE, 'w') as f:
            str_to_file = json.dumps(phone_book.get_phone_book_dict())
            f.write(str_to_file)
            f.close()

    def load_phone_book_from_file(self):
        try:
            with open(settings.JSON_DB_DATA_FILE, 'r') as f:
                str_to_file = f.read()
                self.phone_number_dic = json.loads(str_to_file)
                f.close()
                return self.phone_number_dic
        except:
            return {}
