#def is_contains_char(text,char):
#    i=0
#    while i< len(text):
#            if text[i].upper()==char.upper():
#                return True
#            i+=1
#    return False

#print(is_contains_char("textY","y"))

#def count_char(text, char):
#    result = 0
#    current_char = ''
#    for current_char in text:
#        if current_char.lower()==char.lower():
#            result +=1
#    return result        
#print(count_char('text', 'T'))

def filter_string(text,symbol):
    result=''
    current_symbol = ''
    for current_symbol in text:
        if current_symbol.lower() != symbol.lower():
            result +=current_symbol
    return result.lstrip().rstrip()
print(filter_string('I look back if you are lost','i'))

