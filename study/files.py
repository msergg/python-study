
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



import os
os.path.join('a','b','c')
# a/b/c
os.path.isdir()
os.path.isfile()

os.chdir()
os.rmdir()

os.listdir()


for path, dirs, files in os.walk('/usr/lib/gcc'):
    #print path, dirs, files
    if 'cc1' in files:
        print path, files




# pythex

# REGEX

import re

re.findall(r'(?P<msisdn>\+?(38)?0?\d{9})', 'aasdfasa 380632104444 asfasdf 38063210111 asd 38067210457655')
# (?P<msisdn>\+?(38)?0?\d{9})

r = re.match(r'(?P<msisdn>\+?(38)?0?\d{9})', '380632104444')
r.groupdict()



r = re.search(r'(?P<msisdn>\+?(38)?0?\d{9})', 'aasdfasa 380632104444 asfasdf 38063210111 asd 38067210457655')
print r.groupdict()


phone = re.compile(r'(?P<msisdn>\+?(38)?0?\d{9})')
r = phone.search('aasdfasa 380632104444 asfasdf 38063210111 asd 38067210457655')
# r.start()
print r.groupdict()
print r.start()
print len('aasdfasa 380632104444 asfasdf 38063210111 asd 38067210457655')
m = phone.search('aasdfasa 380632104444 asfasdf 38063210111 asd 38067210457655',pos=r.start() + 12)

print m.groupdict()
