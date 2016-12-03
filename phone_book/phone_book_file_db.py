# coding utf-8
import hashlib
import json


class PhoneBookFileDb(object):
    def __init__(self):
        self.phone_number_dic = {}
