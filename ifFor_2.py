def normalize_url(url):
    
    if url[0:8] =='https://' :
        return url
    elif url[0:7] == 'http://':
        return f'https://{url[7:]}'
    else: 
        return  f'https://{url}'


    
print(normalize_url('http://123'))
