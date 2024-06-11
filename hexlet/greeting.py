def say_hi(name='allG'):
    print('Hi! '+ name)
name = 'Bob'


import random


def sort_pair(nm_1,nm_2):
##    kr_1 = (nm_1,nm_2)
#    kr = (min(kr_1),max(kr_1))
#    return kr
    if nm_1 > nm_2:
        kr = (nm_2,nm_1)
    else:  kr = (nm_1,nm_2)
    return kr
print(sort_pair(1.5,1))