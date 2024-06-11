#def is_palindrome(text):
#    if ''.join(reversed(text))== text:
#       return True
#    return False
#print(is_palindrome('rotor'))
#import package
#print(package.NAME)
mobile_devices = {
    'cucuPhone': 2010,
    'cucuBlet': 2013,
    'cucuClock': 2015,
    'cucuEar': 2018,
    'cuCube': 2015,
}

home_devices = {
    'cucuLot': 2011,
    'cucuBlock': 2010,
    'cucuWall': 2010,
    'cucuMonitor': 2020,
    'cucuLamp': 2015,
    'cucuTable': 2016,
    'cucuTV': 2017,
}

not_supported_devices = {'cucuBlock', 'cucuBlet', 'cucuWall'}

result_catalog = {}

# Допишите функцию выборки поддерживаемого девайса из словаря
def get_supported_catalog(dict_devices, device):
    supported_catalog = {}
    if device in dict_devices:
        supported_catalog.append(device)
    return supported_catalog

get_supported_catalog(mobile_devices, set(mobile_devices))

print('Каталог поддерживаемых девайсов: ')
print(result_catalog)