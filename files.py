
import json

# w write
# a append
# r read
# x

f = open("file.txt", 'r')

#write
#
dict = {'a': 123, 'b':456}
# str_to_file = json.dumps(dict)
#
# f.write(str_to_file)
# f.close()


# read
# dict = {}
# str_to_file = ''
#
# str_to_file = f.read()
#
# dict = json.loads(str_to_file)
#
# print dict['a']
f.close()

phone_number_dic = {}

#
# import hashlib
# import json
#
#
# phone_db_state_hash =  hashlib.sha1(json.dumps(phone_number_dic)).hexdigest()

import pickle