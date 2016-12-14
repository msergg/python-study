# coding utf-8
import sqlite3


class PhoneBookSQLite(object):
    con = sqlite3.connect('db.sqlite')

    def __init__(self):

        PhoneBookSQLite.con.execute("create table IF NOT EXISTS subscribers_book (id INTEGER primary key AUTOINCREMENT, subscriber varchar(50), msisdn varchar(50))")
        PhoneBookSQLite.con.commit()

    def is_subscriber_exists(self, subscriber):
        c = PhoneBookSQLite.con.execute("select msisdn from subscribers_book where subscriber = '{}';".format(subscriber))
        if not c.fetchone():
            raise NameError('No such subscriber')

    def is_msisdn_exists(self, msisdn):
        try:
            c = PhoneBookSQLite.con.execute("select subscriber from subscribers_book where msisdn = '{}';".format(msisdn))
            if not c.fetchone():
                raise KeyError
        except KeyError:
            raise NameError('No such subscriber')

    def add_new_subscriber(self, phone_number, subscriber):
        """Create phone number"""
        PhoneBookSQLite.con.execute("insert into subscribers_book (subscriber, msisdn) values ('{}', '{}');".format(subscriber, phone_number))
        PhoneBookSQLite.con.commit()

    def get_phone_book_dict(self):
        c = PhoneBookSQLite.con.execute("select msisdn, subscriber from subscribers_book ;")
        dict = {}
        for row in c:
            dict[row[0]] = row[1]

        return dict
    #
    # def load_phone_book_from_dict(self, dict):
    #     self.phone_number_dic = dict

    def get_subscriber_by_phone(self, phone_number):
        """Get customer name by phone"""
        c = PhoneBookSQLite.con.execute("select subscriber from subscribers_book where msisdn = '{}';".format(phone_number))
        return str(c.fetchone()[0])

    def get_phone_by_subscriber(self, subscriber):
        """Get phone number by name"""
        c = PhoneBookSQLite.con.execute("select subscriber, msisdn from subscribers_book where subscriber = '{}';".format(subscriber))
        return c.fetchone()

    def delete_customer_by_name(self, subscriber):
        """Delete phone number by name"""
        c = PhoneBookSQLite.con.execute("delete from subscribers_book where subscriber = '{}';".format(subscriber))
        PhoneBookSQLite.con.commit()

