###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1, 2, 3, 4, "String", 3.2, False]
type(l)
# Sıralıdır
# Kapsayıcıdır
# Değiştirilebilir


d = {"Name": "Jake",
     "Age": [27, 56],
     "Adress": "Downtown"}
type(d)
# Değiştirilebilir
# Kapsayıcı
# Sırasız
# Key değerleri farklı olacak



t = ("Machine Learning", "Data Science")
type(t)
# Değiştirilemez
# Kapsayıcı
# Sıralı


s = {"Python", "Machine Learning", "Data Science", "Python"}
type(s)
# Değiştirilebilir
# Sırasız + Eşsiz
# Kapsayıcı


###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."
text.upper().replace(",", " ").replace(".", " ").split()

## uzun yol

a = []
new_str = ""
for letter in text:
    if letter != " " and letter != "," and letter != ".":
        new_str += letter.upper()
    elif new_str == "":
        continue
    else:
        a.append(new_str)
        new_str = ""



###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.

data_list = lst[0:4]
data_list

# Adım 4: Sekizinci index'teki elemanı silin.

lst.pop(8)
lst


lst.remove("N")

# Adım 5: Yeni bir eleman ekleyin.

lst.append(101)
lst

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

lst.insert(8, "N")
lst


###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict1 = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Adım 1: Key değerlerine erişiniz.

dict1.keys()

# Adım 2: Value'lara erişiniz.

dict1.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict1.update({"Daisy": ["England", 13]})
dict1

dict1["Daisy"][1] = 13
dict1

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict1.update({"Ahmet": ["Turkey", 24]})
dict1

# 2. yontem
dict1["Ahmet"] = ["Turkey", 23]


# Adım 5: Antonio'yu dictionary'den siliniz.
dir(dict)

dict1.pop("Antonio")
dict1

# 2. yontem
del dict1["Antonio"]

###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2, 13, 18, 93, 22]


def func(list):
    çift_list = []
    tek_list = []

    for i in list:
        if i % 2 == 0:
            çift_list.append(i)
        else:
            tek_list.append(i)

    return çift_list, tek_list


çift, tek = func(l)

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

## 1
ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
for i, x in enumerate(ogrenciler):
    if i < 3:
        i += 1
        print("Mühendislik Fakültesi", i, ". öğrenci: ", x)
    else:
        i -= 2
        print("Tıp Fakültesi", i, ". öğrenci: ", x)


## 2
ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
for i, x in enumerate(ogrenciler,1):
    if i < 4:
        print("Mühendislik Fakültesi", i, ". öğrenci: ", x)
    else:
        i -= 3
        print("Tıp Fakültesi", i, ". öğrenci: ", x)



###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")


## zip kullanmadan
for i,kod in enumerate(ders_kodu):
    print(f"Kredisi {kredi[i]} olan {ders_kodu[i]} kodlu dersin kontenjanı {kontenjan[i]} kişidir.")



###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

# difference(): İki kümenin farkı
# symmetric_difference(): İki kümede de birbirlerine göre olmayanlar
# intersection(): İki kümenin kesişimi
# union(): İki kümenin birleşimi
# isdisjoint(): İki kümenin kesişimi boş mu?
# issubset(): Bir küme diğer kümenin alt kümesi mi?
# issuperset(): Bir küme diğer kümeyi kapsıyor mu?



kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def kume(set1, set2):
    if set1.issuperset(set2): # set2.issubset(set1):
        print(set1.intersection(set2))  # set2.intersection(set1)
    else:
        print(sorted(set2.difference(set1)))


kume(kume1, kume2)



