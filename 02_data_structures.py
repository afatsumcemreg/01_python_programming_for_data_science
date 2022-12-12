###################################
# veri yapilarina giris
###################################

# sayilar
x = 46
type(x)

x = 10.35
type(x)

x = 2j + 1
type(x)

# stringler
x = 'hello ai era!'
type(x)

# boolean
True
False
type(True)
type(False)
5 == 4
1 == 1
type(5 == 4)

# listeler
x = [1, 2, 3]
type(x)

# sözlük
x = {'name': 'mustafa', 'age': 32}
type(x)

# demet
x = ('python', 'mustafa', 'hakan')
type(x)

# kümeler
x = {'python', 'mustafa', 'hakan'}
type(x)

###################################
# sayilar
###################################
a = 5
type(a)

b = 10.5
type(b)

c = 2j + 1
type(c)

# bazi matematiksel islemler
a * 3
a/7
a*b/10
a**2

# sayilarin tipini degistirme
# float - integer
int(b)
int(a*b/10)
c = a*b/10      # atama islemi
int(c)

# integer - float
float(a)

###################################
# stringler
###################################
print("mustafa") == print('mustafa')        # True
'mustafa'   # without print function

# atama islemi
name = 'mustafa'

# cok satirli karakter dizileri
long_string = """Eger elimizde birden fazla satir varsa
ve daha büyük bir alanda stringi string olarak gormek istiyorsak
bu durumda boyle bir islem yapilamlidir. Uc tirnak isaretinin 
arasina ilgili string girilerek yapilabilir.
"""
long_string

# karakter dizilerinde eleman secme
name[0]     # indexler her zaman sifirdan baslar
name[3]
name[5]

# karakter dizilerinde slicing
name[0:3]      # 0. indexten 3. indexe kadar (3. index haric) degerler gelir.
long_string[0:26]

# string icerisinden eleman sorgulama
# 'elimizde' ifadesi
'elimizde' in long_string
'mustafa' in long_string

###################################
# string metotlari
###################################

# bir veri yapisinin metotlarina erisme
dir(str)
dir(int)
dir(float)

# önemli string metotlari
# len() fonksiyonu: boyut bilgisi verir
len(long_string)
len(name)
type(len)   # class yapisi icerisinde olmadigindan bu bir fonksiyondur
len('miuul')

# upper-lower
x = name.upper()        # class yapisi icinde oldugundan bu bir metottur
x.lower()
'MUSTAFA'.lower()

# type(upper) dedigimizde hata aliriz

# replace() metodu
isim = 'hakan'
isim.replace('h', 't')

# split() metodu
'mustafa germec'.split()
long_string.split()

# strip() metodu
' mustafa '.strip()
'*mustafa*'.strip('*')

# capitalize() metodu
'mustafa'.capitalize()

# startswith() metodu
'mustafa'.startswith('m')
'hakan'.startswith('m')

###################################
# list
###################################

# sayilardan olusan bir liste
notes = [1, 2, 3, 4]
type(notes)

# stringlerden olusan bir liste
names = ['mustafa', 'hakan', 'hacer']
type(names)

# listenin kapsayiciligi
lst = [1, 2, 3, 'a', 'b', True, [1, 2, 3]]
type(lst)

# elemanlara erisme
lst[0]

# True ifadesine eriselim
lst[5]

# icerideki listeye erisme
lst[6]

# icerideki listenin ilk elemanina erisme
lst[6][0]
type(lst[6])
type(lst[6][0])

# listenin degistirilebilirligi
lst[0] = 99

# listede slicing islemi
lst[0:4]

# liste metotlarini getirme
dir(lst)
dir(list)

# onemli liste metotlari

# len() fonk.
len(lst)

# append() metodu
lst.append(False)   # lst listesinin sonuna False eklendi

# pop() metodu
lst.pop(0)      # 0. indexteki eleman silindi

# insert() metodu
lst.insert(2, 99)   # 2. indexe eleman eklendi


###################################
# sözlük
###################################

# sozluk olusturma

a = dict()
type(a)

dictionary = {'reg': 'regression',
              'log': 'logistic regression',
              'cart': 'classification and regression'}

# eleman secme
dictionary['reg']

# sozlukte farkli veri yapilari
dictionary = {'reg': ['regression', 10],
              'log': ['logistic regression', 20],
              'cart': ['classification and regression', 30]}

dictionary['reg']
dictionary['cart'][1]

# key degerleri uzerinden sorgulama
'reg' in dictionary
'yas' in dictionary

# key e gore value ler erisme
dictionary['reg']
dictionary.get('reg')

# value degistirme
dictionary['reg'] = ['ysa', 10]

# key degerlerine erisme
dictionary.keys()

# value degerleirne erisme
dictionary.values()

# key-value ciftlerine erisme
dictionary.items()

# key-value degelerini güncelleme
dictionary.update({'reg': ['random forest', 22]})

# key-value ekleme
dictionary.update({'lightgbm': 10})

# silme islemi
dictionary.pop('reg')

###################################
# tuple
###################################

t = tuple()
type(t)

x = ('mustafa',)
type(x)

y = ('mustafa', 'hakan', 1, 2)
type(y)

# secme islem
y[0]

# slicing islemi
y[0:2]

# degistirme islemi yapilamaz. hata aliriz
y[0] = 'hacer'

# tuple veri setini listeye dosnusturerek degistirme islemi
y = list(y)
y[0] = 'hacer'
y = tuple(y)
type(y)

###################################
# setler
###################################

# lsite üzerinden set olsuturma
set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# difference() metodu: iki kümenin farki
# set1 de olup set2 de olmayan
set1.difference(set2)
set1 - set2

# set2 de olup set 1 de olmayan
set2.difference(set1)
set2 - set1

# symmetric_difference() metodu: iki kümedede birbirinde olmayanlar
set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

# intersection() metodu: kesisimi verir
set1.intersection(set2)
set2.intersection(set1)
set1 & set2

# union() metodu: birlestirir
set2.union(set1)
set1.union(set2)

# isdisjoint() metodu: kesisimin bos olup olmadigini soyler
set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9])

set1.isdisjoint(set2)
set2.isdisjoint(set1)

# issubset() metodu: alt küme olup olmadigi
set1.issubset(set2)
set2.issubset(set1)

# issuperset() metodu:bir kümenin digerini kpsayip kapsamadigi
set1.issuperset(set2)
set2.issuperset(set1)

# Asagidaki koda parcasinin ciktisi nedir
name = 'VBO_Bootcamp'
string = 'new_term'
f'Name:{name} type:{string}'
