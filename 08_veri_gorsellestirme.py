##############################
# 8. Veri Görsellestirme
##############################

# 8.1 kategorik degiskenleri gorsellestirme

# Kategorik degiskenler sütun grafik ile gosterilir
# matplotlib de barplot() metodu kullanilir
# seaborn da ise countplot() metodu kullanilir

# kütüphaneleri import etme ve veri setini okuma
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset('titanic')
df.head()

# amac: 'sex' degiskenini gorsellestirme
df['sex'].value_counts()
# value_counts() fonksiyonu elimiz ayagimiz olmalidir.
# kategorik degiskenler ile islem yaptigimizda akla ilk bu metot gelmelidir.
# pandas kütüphansei ile gorsellestirme
df['sex'].value_counts().plot(kind='bar')
plt.show(block=True)
# seaborn kütüphanesi ile gorsellestirme
sns.countplot(x=df['sex'])
plt.show(block=True)

# 8.2 Sayisal degiskenleri gorsellestirme
# sayisal degisknlerde veri goresllestirme ile elde edilecek olan sey, degiskenin dagilimi ve yapisidir.
# degiskenin dagilimini kolayca veren metotlar hist() ve boxplot() dur.
# boxplot() ayrica aykiri degerleri de gosterir
# matplotlib ile gorsellestirme
# histogram
plt.hist(df['age'], bins=20)  # sayisal degiskenlerin dagilimi elde edilir
plt.show(block=True)
sns.histplot(df['age'])
plt.show(block=True)
# boxplot
sns.boxplot(y=df['age'])
plt.show(block=True)

# 8.3. Matplotlib özellikleri
# matplotlib, yapisi itibariyle katmanli bir sekilde gorsellestirme imakni saglar.

# plot ozelligi
x = np.array([1, 8])
y = np.array([0, 150])
plt.plot(x, y)
plt.show(block=True)

plt.plot(x, y, 'o')  # 'o' ifadesi, noktalarin oldugu yere '*' isaretini koyar
plt.show(block=True)

# daha fazla noktanin olmasi durumu
x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])
plt.plot(x, y, 'o')
plt.show(block=True)

# marker ozelligi
y = np.array([13, 28, 11, 100])
plt.plot(y, marker='o')  # markers = ['o', 'x', '*', '.', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']
plt.show(block=True)
plt.plot(y, marker='P')
plt.show(block=True)

# Line ozelligi
y = np.array([13, 28, 11, 100])
plt.plot(y)
plt.show(block=True)

# cizgi stili eklenebilir
y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle='dashed')  # linestyle = ['dashed', 'dotted', 'dashdot]
plt.show(block=True)

# cizgilere renk ozelligi eklenebilir
y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle='dashed', color='r')
plt.show(block=True)

# coklu cizgiler ekleme
x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle='dashed', color='r')
plt.plot(x, linestyle='dashed', color='g')
plt.show(block=True)

# etiketler (labels)
x = np.array([80, 85, 90, 95, 100, 105, 125, 165])
y = np.array([120, 150, 200, 400, 500, 600, 700, 800])
plt.plot(x, y)
plt.title('Bu ana baslik')
plt.xlabel('X ekseni')
plt.ylabel('Y ekseni')
plt.gray()
plt.show(block=True)

# subplots: birlikte biden fazla grafigin gosterilme seklidir
# plot 1
plt.subplot(1, 2, 1)
x = np.array([80, 85, 90, 95, 100, 105, 125, 165])
y = np.array([120, 150, 200, 400, 500, 600, 700, 800])
plt.plot(x, y)
plt.title('Plot 1')

# plot 2
plt.subplot(1, 2, 2)
a = np.array([25, 35, 45, 55, 65, 75, 86, 98])
b = np.array([1, 3, 5, 7, 9, 11, 13, 15])
plt.plot(a, b)
plt.title('Plot 2')
plt.show(block=True)

# seaborn ile veri gorsellestirme
df = sns.load_dataset('tips')
df.head()
df.info()

# kategorik degiskenleri gorsellestirme (countplot() metodu)
sns.countplot(df['day'])
plt.show(block=True)

# matplotlib ile gorsellestirme
df['day'].value_counts().plot(kind='bar')
plt.show(block=True)

# sayisal degiskenlerin gorsellestirilmesi
sns.boxplot(y=df['total_bill'])
plt.show(block=True)

sns.histplot(df['total_bill'])
plt.show(block=True)