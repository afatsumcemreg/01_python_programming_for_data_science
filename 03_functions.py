##################################
# fonksiyonlar
##################################
print('a')
help(print)

# 'sep' argümaninin kullanimi
print('a', 'b')
print('a', 'b', sep='__')

# Fonksiyon tanimlama
# ornegin girilen sayilarin 2 ile carpilmaini saglayan bir fonksiyon yazalim
def calculate(x):
    print(x*2)


calculate(2)

# 2 parametreden olusan bir fonksiyon tanimlama
def summer(x, y):
    print(x + y)


summer(3, 5)

# docstring

# Asagida tanimlanan fonksiyona docstring ekleyelim
def summer(num1, num2):
    """
    Sum of two numbers
    Args:
        num1: int / float
        num2: int / float

    Returns: int / float

    Examples:

    Notes:

    """
    print(num1 + num2)


summer(3, 6)

help(summer)

# fonksiyonlarin govde bolumu

# fonksiyon tanimlama
# def function_name(arguments):
#     statement(function_body)

# herhangi bir argümani olmayan ir fonksiyon tanimlama
def say_hi():
    print('mrb')
    print('hi')
    print('hello')


say_hi()

# yukaridaki fonksiyonu arguman girerek tanimlama
def say_hi(string):
    print(string)
    print('hi')
    print('hello')


say_hi('hi, mustafa')

# girilen iki sayinin carpimi ve sayilari nesnede tutma
def multiplicate(a, b):
    c = a * b
    print(c)


multiplicate(4, 5)

# girilen degerleri bir liste icinde saklama
list_store = []

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(2, 4)
add_element(3, 4)
add_element(4, 5)

# on tanimli argümanlar
def division(a, b):
    print(a/b)


division(2, 5)

def divide(a, b=10):    # b=10 burada ön tanimli argüman
    print(a*b)


divide(15)

def msg(string='Merhaba'):
    print(string)
    print('Hi')
    print('Hallo, Guten Tag!')


msg()
msg('Hello')

# ne zaman fonksiyon yazariz?
"""
Birbirinin tekrar eden islemler yapmak zorunda kaldigimizda, tekrar tekrar ayni islemleri yapmamak icin,
yapi ayni da olsa degisen durumlari fonksiyon ile tanimlayip daha sonra bu fonksiyon cagrilarak 
otamatik bir sekilde kullanmak icin fonksiyon yazilir.

Temel programlama prensiplerinden birisi, 'KENDINI TEKRAR ETME (DO NOT REPEAT YOURSELF)', yani DRY 
prensibidir. BU sebeple birbirinin tekrar etme durumu soz konusu oldugunda fonksiyon yazma ihtiyaci
dogar
"""

def calculate(warm, mositure, charge):
    print((warm + mositure) / charge)


calculate(98, 12, 78)

# return
# fonksiyon ciktilarinin girdi olarak kulanamk icin kullanilan bir yapidir.

def calculate(warm, mositure, charge):
    print((warm + mositure) / charge)


calculate(98, 12, 78) * 10          # TypeError
type(calculate(98, 12, 78))         # NoneType

def calculate(warm, mositure, charge):
    return (warm + mositure) / charge


a = calculate(98, 12, 78) * 10   # ciktiyi tekrar kullanmak icin atama islemi


def calculate(warm, moisture, charge):
    warm = warm*2
    moisture = moisture*5
    charge = charge/4
    output = (warm + moisture) / charge
    return warm, moisture, charge, output


warm, moisture, charge, output = calculate(98, 12, 78)

# fonksiyon icerisinden fonksiyon cagirmak

# maksat, fonksiyonlarin govde bolumunu daha genis acidan degerlendirmektir.
# iki fonksiyon tanimlayalim
def calculate(warm, moisture, charge):
    return int((warm + moisture) / charge)


calculate(98, 12, 12)

def standaridzation(a, b):
    return a * 0.1 * b * b


standaridzation(45, 1)

def all_calculation(warm, moisture, charge, b):
    a = calculate(warm, moisture, charge)
    c = standaridzation(a, b)
    print(c * 10)


all_calculation(98, 12, 12, 25)

def all_calculation(warm, moisture, charge, a, b):
    print(calculate(warm, moisture, charge))
    c = standaridzation(a, b)
    print(c * 10)


all_calculation(98, 12, 12, 3.14, 25)

# lokal ve global degiskenler

list_store = []      # global degisken

def add_element(a, b):
    # lokal degisken
    c = a * b
    list_store.append(c)
    print(list_store)

# append() metodu ile degistirilebilir bir yapi olan liste uzerinde bir etki olusturuluyor.
# buna 'lokal etki alanindan global etki alanini etkilemek' denir.


add_element(3, 5)
add_element(b=15, a=6)
