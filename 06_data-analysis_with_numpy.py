####################################
# 6. NumPy
####################################

# 6.1. Giriş

import numpy as np

a = [1, 2, 3, 4]
b = [2, 4, 6, 8]

# Pythonik yol ile bu iki listeyi carpmak
ab = []
for i in range(len(a)):
    ab.append(a[i] * b[i])

print(ab)

# Numpy ile yukaridaki islemin aynisini gerceklestirme
a = np.array(a)
b = np.array(b)
a * b
type(a * b)  # Veri tipi ndarray dir.

# 6.2. NUmPy arrayi olusturma

# Sifirdan numpy arrayi olusturma

a = np.array([1, 2, 3, 4, 5])  # liste uzerinden olusturulur
type(a)

# Sifirdan numpy arrayi olusturmanin diger yollari
# zero arrayi
np.zeros(10, dtype=int)

# belirli bir aralik olacak sekilde rastgele integer sayilardan olusan array olusturma
np.random.randint(0, 10, size=10)

# belirli bir istatistiksel dagilima gore array olusturma
np.random.normal(10, 4, (3, 4))
# 10: normal dagilimli kitlenin ortalaması
# 4: Argüman-burada standard sapma
# (3, 4): boyut bilgisi

# 6.3. Numpy arrays ozellikleri

# 0-10 arasinda rastgele integer sayi uretelim
a = np.random.randint(0, 10, size=5)

a.ndim  # boyut sayisi
a.shape  # boyut bilgisi
a.size  # toplam eleman sayisi
a.dtype  # veri tipi

# 6.4. Reshaping
# boyut degistirmek icin kullanilir
# 3x3 lük bir array olusturalim
x = np.random.randint(1, 10, size=9)
x.reshape(3, 3)

# atama islemi olmadan islemler gerceklestirilebilir
np.random.randint(1, 10, size=9).reshape(3, 3)

# hata alalim
# np.random.randint(1, 10, size=9).reshape(2, 5)      # ValueError

# 6.5. Index secimi

# 1D array
# numpy array olusturma
x = np.random.randint(0, 10, size=10)

# olusan arrayin 0. indexine erisme
x[0]

# olusan arrayde birden fazla secim yapma
x[0:5]  # slicing-dilimleme islemi

# 0. indexteki elemanin degistirme
x[0] = 99  # array([99,  6,  4,  8,  2,  6,  9,  8,  7,  5])

# 2D array
# 10 elemanli 3x5 array olusturma

x = np.random.randint(10, size=(3, 5))
# 3: satir-gozlem sayisi
# 5: sutun-degisken sayisi

# olusan arrayin ilk elemanina erisme

x[0, 0]

# (1, 1) indexi hangi deger ekarsilik gelir
x[1, 1]

# 2. satir ve 3. sütundaki elemani secelim ve degistirelim
x[2, 3] = 1000

# float bri ifade ile yer degistirme
x[2, 3] = 2.9  # numpy fixed-type eleman tutar.
x

# slicing-dilimleme islemi
# butun saturlari ve 0. sutunu secelim
x[:, 0]  # array([7, 4, 5])

# 1. satiri ve tum sutunlari secelim
x[1, :]  # array([4, 2, 4, 8, 6])

# hem satirladan hem de sutunlardan belirli bir aralik secme
x[0:2, 0:3]  # array([[7, 0, 1], [4, 2, 4]])

# 6.6. Fancy index

# Fancy index, bir numpy araryine bir liste girdigimizde kolay bir sekilde erisim imkani saglar
v = np.arange(0, 30, 3)

# birkac gozlem birimine eriselim
v[1]
v[3]

catch = [1, 2, 3]
v[catch]  # array([3, 6, 9])

# 6.7. Numpy da kosullu islemler

# Amacimiz 3 ten kucuk degerlere erismek
# Klasik yol yani for dongusu

m = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
ab = []
for i in m:
    if i < 3:
        ab.append(i)

print(ab)  # [0, 1, 2]

# yukaridaki islemin aynisini numpy ile yaplim
m[m < 3]  # m[m < 3]

m[m > 3]  # 3 ten buyuk degerlere ulasma
m[m != 3]  # 3 ten farkli degerlere erismek
m[m >= 3]  # 3 ve 3 ten buyuk degerlere erismek

# numpy da kosullu islemlerin arka tarafinda calisan mantik, 'fancy index' tir.

# 6.8. Numpy da matematiksel islemler

# yukarida tanimlanan m numpy arrayi ile islemleri yapalim
m / 5  # bolme islemi
m * 5  # carpma islemi
m ** 2  # kare alma
m - 1  # cikarma islemi
m + 3  # toplam islemi

# metotlar ile yukaridaki islemleri yapalim
np.subtract(m, 1)  # cikarma islemi
np.add(m, 1)  # toplama islemi
np.mean(m)  # ortalama
np.sum(m)   # toplam
np.min(m)   # minimum deger
np.max(m) # maximum deger
np.var(m) # varyans
np.std(m) # standard sapma

# numpya ile iki bilinmeyenli denklem cozumu

# denklem 1: 5x0 + x1 = 12
# denklem 2: x0 + 3x1 = 10

a = np.array([[5, 1], [1, 3]])  # katsayilar icin array
b = np.array([12, 10])  # sonuclar icin array
np.linalg.solve(a, b)   # cozum icin array

# pratikte veri analitigi ve ver analizi gibi islemlerde PANDAS kullanilir
