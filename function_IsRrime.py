def is_prime(number):
    if number < 2:
        return False
    
    divider = 2

    while divider <= number/2:
        if number % divider ==0:
            return False
        divider +=1
        
    return True
print(is_prime(991))        