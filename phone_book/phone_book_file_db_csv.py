# coding utf-8
from phone_book_file_db import PhoneBookFileDb
import csv


class PhoneBookFileDbCSV(PhoneBookFileDb):
    def save_phone_book_to_file(self, book):
        self.phone_number_dic = book.phone_number_dic
        if not self.is_actual():
            with open('phonebook.csv', 'wb') as csvfile:
                writer = csv.writer(csvfile,
                                    delimiter=',',
                                    quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
                for msisdn, subscriber in self.phone_number_dic.items():
                    writer.writerow([msisdn, subscriber])
                csvfile.close()
                self.update_phone_db_state_hash()

    def load_phone_book_from_file(self, book):
        try:
            with open('phonebook.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                book.phone_number_dic = {}
                for row in reader:
                    book.phone_number_dic[row[0]] = row[1]
                csvfile.close()
        except:
            with open("phonebook.csv", 'w') as csvfile:
                csvfile.close()
