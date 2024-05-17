#import numpy as np
#a = np.array([1,2,3])
#a2 = np.array([[1,2,3],[7,8,9]])

#print(a)
#print(a2)
#def my_substr(text:str, lenght:int):
#    result = ''
#    i = 0
#    while i < lenght:
#        result += text[i]
#        i += 1
#     !!!   return result
#print (my_substr('aaaa', 4))


def count_chars(text:str, letter:str):
    finish_cont=0
    i=0
    while i < len(text):
        if text[i] == letter:
            finish_cont +=1
        else:
            finish_cont +=0

        i += 1
    return finish_cont

print(count_chars('texttt','t'))