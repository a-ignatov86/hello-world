def is_ouestion(text):
    last_crair = text[len(text)-1]
    if last_crair == '?':
        return 'question'
    return 'not question'
print(is_ouestion('las?'))
print(is_ouestion('las'))
