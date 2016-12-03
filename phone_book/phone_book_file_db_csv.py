# coding utf-8
from phone_book_file_db import PhoneBookFileDb
import csv
import settings


class PhoneBookFileDbCSV(PhoneBookFileDb):
    def save_phone_book_to_file(self):
        if not self.is_actual():
            with open(settings.CSV_DB_DATA_FILE, 'wb') as csvfile:
                writer = csv.writer(csvfile,
                                    delimiter=',',
                                    quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
                for msisdn, subscriber in self.phone_number_dic.items():
                    writer.writerow([msisdn, subscriber])
                csvfile.close()
                self.update_phone_db_state_hash()

    def load_phone_book_from_file(self):
        try:
            with open(settings.CSV_DB_DATA_FILE, 'r') as csvfile:
                reader = csv.reader(csvfile)
                self.phone_number_dic = {}
                for row in reader:
                    self.phone_number_dic[row[0]] = row[1]
                csvfile.close()
                return self.phone_number_dic
        except:
            with open(settings.CSV_DB_DATA_FILE, 'w') as csvfile:
                csvfile.close()
