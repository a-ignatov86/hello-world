def is_ouestion(text):
    last_crair = text[-1]
    if last_crair == '?':
       text_type = 'question' 
    elif last_crair =='!':
        text_type = "exclamation"
    else :

        text_type = 'normal'
    return 'Text is ' + text_type
print(is_ouestion('las?'))
print(is_ouestion('las!'))
print(is_ouestion('las'))

def abs(number):
    return number if number >= 0 else -number
print(abs(22))
print(abs(-2))

def get_type_of_sentence2(text):
    return 'question' if text[-1] == '?' else 'normal'
print (get_type_of_sentence2('Ntxrr?'))
