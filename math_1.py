#dollars_count = 50*1.25
#rubbles_per_dollars = 60
#rubbles_count = dollars_count * rubbles_per_dollars
#print('This prise is ' + str(rubbles_count) + 'rubles')

def get_hidden_card(card_numbr, count_stars = 4):
    a = str(card_numbr)
    hidden_card = a[-4:] 
    stars="*" * count_stars
    return f'{stars}{hidden_card}'

print(get_hidden_card(1234567890123456,12))