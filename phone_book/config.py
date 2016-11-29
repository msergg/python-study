# coding utf-8
import ConfigParser
import settings


import argparse
from phone_book_file_db_json import PhoneBookFileDbJSON
from phone_book_file_db_csv import PhoneBookFileDbCSV



class ConfigParameters(object):
    def __init__(self):
        try:
            file_type = self.get_file_type_value()
        except:
            print "Configuration file is not configuired!"

        file_type = self.load_args_parameters()

        if file_type == 'csv':
            self.phone_book_file_db = PhoneBookFileDbCSV()
        else:
            self.phone_book_file_db = PhoneBookFileDbJSON()

    def get_phone_book_file_db(self):
        return self.phone_book_file_db

    def get_file_type_value(self):
        try:
            config = ConfigParser.RawConfigParser()
            config.read(settings.CONFIG_FILE)


            file_type = config.get('Parameters', 'file_type')

            return file_type
        except:
            return settings.DEFAULT_DATA_FILE_FORMAT

    def load_args_parameters(self):
        parser = argparse.ArgumentParser(description='Chose file format to save')

        parser.add_argument("file_type", help="Use 'json' or 'csv' as parameter "
                                              "to choose your data storage\n"
                                              "example: task.py json", nargs='?')
        args = parser.parse_args()

        if not args.file_type is None:
            file_type = args.file_type
            print 'Using: ' + file_type + ' data file format'
            return file_type






