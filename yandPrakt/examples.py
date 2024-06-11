import urllib.parse as ur

user_query = 'как стать бэкенд-разработчиком'

url = 'https://yandex.ru/search/?text=' 
#+ user_query # ваш код здесь

normal_query = user_query.split(' ')
finish_query = ('%20').join(normal_query)

#print(f'{url}{finish_query}&lr=213 ')

a =ur.quote(user_query)
print(a)
b =ur.unquote(a)
print(b)

