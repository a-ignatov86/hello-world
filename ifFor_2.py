#from nis import match


def normalize_url(url):
    
    match url[:7]:
        case 'https:/' :
            return url
        case 'http://' :
            return f'https://{url[7:]}'
        case _:
            return f'https://{url}'


def get_number_explanation(number):
    match number:
        case 666:
            return'devil number'
        case 42:
            return'answer for everything'
        case 7:
            return'prime number'
        case _:
            return'just a number'
print(get_number_explanation(0))
