#first_name = 'Joffrey'
#greeting = 'Hello'
##text= ''' example 
#multy
##string'''
#print(f'{greeting}, {first_name}!')
#print(text)
#print('- Did Joffrey\n agree?' )

#print(11 % 2 == 0 and 'yes' or 'no') # => 'yes'

def join_numbers_from_range(start,finish):
    string_of_numbers = ''
    i = start
    while i <= finish:
        string_of_numbers += str(i)
        i +=1
    return (print(string_of_numbers))
join_numbers_from_range(2,6)
