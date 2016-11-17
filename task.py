"""
TEST PROJECT

CRUD
"""


CRUD_DICT = {1: 'Create phone number', 2: 'Get phone number by name',
             3:'Update phone number by name', 4:'Delete phone number by name'}


phone_number_dic = {}

print 'Please choose what to do: '

choice = 2

for i, text in CRUD_DICT.items():
    print str(i) + " : "+ text

choice = int(raw_input('Input your choice:'))




if choice == 1:
    print '1. Please input phone number: '
    phone_number = raw_input()
    print '2. Please input customer name: '
    customer = raw_input()
    phone_number_dic[phone_number] = customer

print phone_number_dic











