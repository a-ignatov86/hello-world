#def  is_a_start (text):
#    start = text[0].lower()
#    return start == 'a'
#print(is_a_start('Atext'))

##def is_correct_password(password):
##    lenght = len(password)
##
 ##   return lenght > 8 and lenght < 20
##print(is_correct_password('123456789'))

#def is_not_even(num):
#    return num % 2  != 0
#print(not is_not_even(2))

##def is_leap_year(num):
##    a = (num % 400 ==0) or (num % 4 ==0 and num % 100 !=0)
##    return a
##print(is_leap_year(2016))

#def string_or_not(text):
#    is_string = isinstance(text, str)
#    answer = is_string and 'yes' or 'no'
#    return answer
#print (string_or_not(True))

nums=range(1,10)

def is_prime(num):
    for x in range(2,num):
        if (num%x) == 0:
            return False
        return True

primes= list(filter(is_prime, nums))
print(primes)