# coding utf-8
import phone_book_file_db_csv
import phone_book_file_db_json




class PhoneBookFileDbFactory(object):
    def __init__(self):
        pass

    def __new__(cls, file_type):
        if file_type == 'json':
            return phone_book_file_db_json.PhoneBookFileDbJSON()
        elif file_type == 'csv':
            return phone_book_file_db_csv.PhoneBookFileDbCSV()
        else:
            raise ValueError

