def is_palindrome(text):
    if ''.join(reversed(text))== text:
       return True
    return False
print(is_palindrome('rotor'))