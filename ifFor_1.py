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
