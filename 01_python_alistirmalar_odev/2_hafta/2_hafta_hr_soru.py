"""
Aşağıdaki fonksiyonun her satırında ne yapıldığını anlatınız? 
Bu fonksiyonu enumerate ile yazabilir miydik? 
Yazabiliyor olsaydık bu ne kazandırırdı?
"""
def alternating(string):
    new_string = ''
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    print(new_string)


alternating('miuul veri bilimi okulu')


# alternating fonksiyonunun enumerate ile yazılması
def new_alternating(string):
    new_string = ''
    for index, letter in enumerate(string):
        if index % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)


new_alternating('miuul veri bilimi okulu')

# alternating fonksiyonunun list comprehension ile yazılması
def alternating_comprehension(string):
    return [letter.upper() if index % 2 == 0 else letter.lower() for index, letter in enumerate(string)]

for i in alternating_comprehension('miuul veri bilimi okulu'):
    print(i, end='')

# alternating fonksiyonunun dogrudan comprehension ile yazılması
for i in [letter.upper() if index % 2 == 0 else letter.lower() for index, letter in enumerate('miuul veri bilimi okulu')]:
    print(i, end='')


