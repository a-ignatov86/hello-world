def save_email():
    email = '  SuppORT@hexlet.IO'
    trim = email.strip()
    prop = trim.lower()
    return prop

print(save_email())