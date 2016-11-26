import ConfigParser

class ConfigParameters(object):
    def __init__(self):
        pass

    def get_file_type_value(self):
        try:
            config = ConfigParser.RawConfigParser()
            config.read('phonebook.cfg')

            file_type = config.get('Parameters', 'file_type')

            return file_type
        except:
            return 'json'




# config = ConfigParser.RawConfigParser()
#
# config.add_section('Parameters')
# config.set('Parameters', 'file_type', 'csv')
#
# with open('phonebook.cfg', 'wb') as configfile:
#     config.write(configfile)



