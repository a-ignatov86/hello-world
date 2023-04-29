#entry = input('Password: ')

#if entry == 'sub2b001':
#    print('Access Granted')
#else:
#    print('Access Denied')

#def f( a=1, b=2, c= None, d = 'nxy'):
#    print(a,b,c,d)

#print(f(7,d=1))

def trim_and_repeat(string='python',offset=0,repetitions=1):
    slise=string[offset:]
    result = slise * repetitions
    return result
print(trim_and_repeat(offset=3, repetitions=2))