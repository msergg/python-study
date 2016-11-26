import hashlib
import json

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
