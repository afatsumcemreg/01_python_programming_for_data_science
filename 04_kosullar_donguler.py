###################################
# kosullar ve donguler
###################################

# if kosulu

# True ve False hatirlama
1 == 1
1 == 2
1

if 1 == 1:
    print('True')

if 1 == 2:
    print('True')

number = 11
if number == 10:
    print('True')

number = 10
if number == 10:
    print('True')


# DRY prensibini uygulama
def number_check(number):
    if number == 10:
        print('True')


number_check(10)
number_check(12)


# elif-else kosullari

# else
def number_check(number):
    if number == 10:
        print('Number is 10')
    else:
        print('Number is not 10')


number_check(10)
number_check(12)


# elif
def number_check(number):
    if number > 10:
        print('Number is greater than 10')
    elif number < 10:
        print('Number is lower than 10')
    else:
        print('Number is equal to 10')


number_check(12)
number_check(8)
number_check(10)

# for döngüsü

students = ['mustafa', 'hacer', 'hakan', 'new_member']
# amac, buradaki her bir elemana erismek
students[0]
students[1]
students[2]
students[3]

# yukaridaki islemi for dongusu ile yapmak
for student in students:  # buradaki isimlendirme istenildigi gibi yapilir.
    print(student)

    # amacimiz listedeki her bir ismi buyutmek
for student in students:
    print(student.upper())

    # maaslari ifade eden bir listenin her bir elemanini yazdirmak

salaries = [1000, 2000, 3000, 4000, 5000]
for salary in salaries:
    print(salary)

    # maaslara %20 zam yapalim

for salary in salaries:
    print(int(salary * 0.2 + salary))

    # fonksiyonel maaslara zam uygulamasi


def new_salary(salary, rate):
    return salary * rate / 100 + salary


new_salary(2000, 20)

for salary in salaries:
    print(int(new_salary(salary, 20)))

    # baska bir maas listesi icin fonksiyonu uygulama

salaries_ = [800, 1000, 3000, 10000]
for salary in salaries_:
    print(int(new_salary(salary, 50)))

    # maas >3000 is %30, degilse %40 zam uygulama

for salary in salaries:
    if salary > 3000:
        print(int(new_salary(salary, 30)))
    else:
        print(int(new_salary(salary, 40)))


# uygulama mülakat sorusu
# amac, girilen string ifadenin cift indexlerini buyuk, tek indexlerini kücük harf yapmak
def alternating(string):
    new_string = ''
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    return new_string


alternating('mustafa')
alternating('miuul')
alternating('hakan_yavuz')

# break, continue and while

# break: kosul saglandiginda dongu durar
for salary in salaries:
    if salary == 3000:
        break
    print(salary)

# contnue: aranan kosul saglandiginda kosulu atlar ve devam eder
for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

# while: bir sart uygulandigi surece calismaya devam eder
number = 1
while number <= 5:
    print(number)
    number += 1

# enumerate: otomatik index üretici
# for dongusu ile birlikte kullanilabilir

students = ['mustafa', 'hacer', 'hakan', 'new_member']
for student in students:  # index bilgisi yok
    print(student)

for index, student in enumerate(students):  # index bilgisi var ve 0 ile baslar
    print(index, student)

for index, student in enumerate(students, 1):  # index bilgisi var ve 1 ile baslar
    print(index, student.upper())

# cift indexteki ogrencileri bir listeye, tek indextekileri diger bir listeye ekleyelim
a, b = [], []

for index, student in enumerate(students):
    if index % 2 == 0:
        a.append(student)
    else:
        b.append(student)
print(a)
print(b)


# uygulama mülakat sorusu - enumerate
# divide_students fonksiyonu yaz
# cift indexte yer alan ögrencileri bir listye ekle
# tek indexte yer alan ögrencileri bir listye ekle
# fakat bu iki liste tek bir liste icerisinde return olsun

def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    return groups


divide_students(students)


# alternating fonksiyonunun enumerate ile yazılması
def new_alternating(string):
    new_string = ''
    for index, letter in enumerate(string):
        if index % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    return new_string


new_alternating('mustafa')
new_alternating('miuul')

# alternating fonksiyonunun comprehension ile yazılması
def alternating_comprehension(statement):
    new_string = [j.upper() if i % 2 == 0 else j.lower() for i, j in enumerate(statement)]
    return new_string

new_string = alternating_comprehension('veri bilimi okulu')
for i in new_string:
    print(i, end='')

# alternating fonksiyonunun comprehension ile yazılması
new_string = [j.upper() if i % 2 == 0 else j.lower() for i, j in enumerate('veri bilimi okulu')]
for i in new_string:
    print(i, end='')

# zip: listenin elemanlarini esler ve birbirinden farkli sekilde olan listeleri bir
# arada degerlendirme imkani saglar

students = ['mustafa', 'hacer', 'hakan', 'new_member']
departments = ['mathematics', 'statistics', 'engineering', 'chemistry']
ages = [32, 35, 5, 0]

new_list = list(zip(students, departments, students))
for index, nlis in enumerate(new_list):
    print(index, nlis)

# lambda, map, filter ve reduce

# lambda fonksiyonu
# cok onemlidir ve en cok aplly() metodu ile birlikte kullanilir
# iki sayinin toplamini veren fonksiyonlari tanimlayalim
# kullan-at bir fonksiyondur
# 1. fonksiyon: def ile

def summer(a, b):
    return a + b

summer(3, 5)

# 2. fonksiyon: labda ile
(lambda a, b: a + b)(3, 5)

# map fonksiyonu
# dongu yazmaktan kurtalmak icin yazilir
salaries = [100, 200, 300, 400, 500]

def salary_calc(salary):
    return salary * 20 / 100 + salary

salary_calc(1500)

for salary in salaries:
    print(salary_calc(salary))

list(map(salary_calc, salaries))

# lambda ve map fonksiyonlarinin birlikte kullanimi
list(map(lambda x: x * 0.2 + x, salaries))
list(map(lambda x: x**2, salaries))     # salaries listesindeki her bir maasin karesini alma

# filter fonksiyonu
    # filtreleme icin kullanilir
    # yaygin kullanilmaz
    # dongü yazmaya gerek olmaz

    # amac, bir listedeki hem cif hem tek sayilari filtreleme

num_lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, num_lis))     # cift sayilar
list(filter(lambda x: x % 2 != 0, num_lis))     # tek sayilar

# reduce fonksiyonu
    # fonksiyonu kullanabilmek icin 'functools' modulunden 'reduce' import edilir
    # asagidaki fonksiyonlar sirasiyla tanimlanan listedeki sayilari carpar, toplar ve boler
from functools import reduce
reduce(lambda x, y: x * y, num_lis)
reduce(lambda x, y: x + y, num_lis)
reduce(lambda x, y: x / y, num_lis)

# quiz
    # Soru 1: asagidaki 'wages' listesindeki degerlerin 40 tan kücük olanlarini 1.1 ile, olmayanlari ise oldugu gibi birakalim
    # cikan sonuclari 'new_wages' listesine atalim

    # for dongusu
wages = [10, 20, 30, 40, 50]
new_wages = []
for i in wages:
    if i < 40:
        new_w = i * 1.1
        new_wages.append(new_w)
    else:
        new_wages.append(i)

print(new_wages)

    # list comprehension
[wage * 1.1 if wage < 40 else wage for wage in wages]

    # Soru 2: asagide verilen 'wage' listesinde wage > 950 olursa wage degerinin 1.1 ile, degilse 1.2 ile carpan bir
    # list comprehension ve for dongüsü yaziniz yaziniz

wages = [700, 800, 900, 1000]

    # for dongusu
new_wage = []
for wage in wages:
    if wage > 950:
        wage = wage * 1.1
        new_wage.append(wage)
    else:
        wage = wage * 1.2
        new_wage.append(wage)
print(new_wage)

    # list comprehension
[wage * 1.1 if wage > 950 else wage * 1.2 for wage in wages]

    # Soru 3: Asagid verilen ogrenci listesinde eger ogrencinin indexi cift ise ogrencinin ilk harfini buyuk, degilse
    # kücük yazdiran bir kodlama yaziniz

students = ['Derya', 'Ahmet', 'Turgut', 'Ayse']

    # for dongusu
new_list = []
for student in students:
    if len(student) % 2 == 0:
        letter = student[0].upper()
        new_list.append(letter)
    else:
        letter = student[0].lower()
        new_list.append(letter)

print(new_list)

    # lis comprehension
[i[0].upper() if len(i) % 2 == 0 else i[0].lower() for i in students]

    # Soru 4: Asagida verilen stringin her bir indexi 2 ile carpilip 2 ile bolunebilmesinden elde edilen cikti

string = 'abracadabra'

    # for dongusu
new_list = []
for index, letter in enumerate(string):
    if index * 2 % 2 == 0:
        new_list.append(letter)
    else:
        new_list.append(letter)

print(new_list)

    # list comprehension
[letter for index, letter in enumerate(string) if index * 2 % 2 == 0]

    # Soru 5: Asagid averilen 'cities' listesindeki her bir sehri indexi ile birlikte fonksiyon kullanarak yaziniz
cities = ['london', 'paris', 'berlin']

    # fonksiyon tanimlama
def plate(cities):
    for index, city in enumerate(cities, 1):
        print(f'{index}: {city}')

plate(cities)

    # list comprehension
a = [f'{index}: {city}' for index, city in enumerate(cities, 1)]
for i in a:
    print(i)