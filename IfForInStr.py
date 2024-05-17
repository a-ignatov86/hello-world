def has_char(text,char):
    
    i = 0
    while i < len(text):
        if text[0].lower()!=char.lower():
            return False
        else:
            return True
        i+=1
    return True

print(has_char('twxt', 't'))
