##from greeting import say_hi, name
#import computation
#from computation import PI, E
#from computation import pi_times

from package.functions import greet
from package.constants import PERSON

from random import randint
#print(PI)
#print(computation.E)
#print(pi_times(2))
#print(computation.pi_times(E))

##greeting.say_hi(name='al')
##print(name)
##say_hi("stan")


def sort_pair(nmbrs):
#print(randint(1, 100))
    n_1, n_2 = nmbrs
    if n_1 > n_2:
        return n_2, n_1
    else:
        return n_1, n_2
    
print(sort_pair((5, 12)))