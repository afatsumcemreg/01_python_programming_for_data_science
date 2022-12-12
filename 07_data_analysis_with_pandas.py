################################
# 7. Pandas
################################

import pandas as pd
import numpy as np
import seaborn as sns
from sqlalchemy import column

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# 7.1. Pandas series
# tek boyutlu ve index bilgisi barindirir

s = pd.Series([10, 77, 12, 4, 5])  # pandas serisi bir metottur
# pandas serisindeki index bilgisi bir ic ozelliktir
type(s)  # pandas.core.series.Series
s.index  # index bilgisini verir. # RangeIndex(start=0, stop=5, step=1)
s.dtype  # pandas serisinin veri tipi bilgisine erisme
s.size  # pandas serisinin eleman sayisi
s.ndim  # pandas serisinin boyut sayisini verir. pandas serileri tek boyutludur.
s.values  # pandas serisinin icersindeki degerlerin kendisine ulasma
type(s.values)  # numpy.ndarray

# pandas serileri ile kullanilabilecek diger metotlar
s.head()  # ilk 5 gozlemi getirir
s.head(3)  # ilk 3 gozlemi getirir
s.tail()  # son 5 gozlemi getirir
s.tail(3)  # son 3 gozlemi getirir

# pandas serileri ile gerceklestirilebilen matematiksel operatorler

y = pd.Series([2, 4, 6, 6, 12])
s * y
s / y
s + y
s - y
s ** y
s // y

# pandas serileri ile gerceklestirilebilen metotlar

np.subtract(s, y)
np.add(s, y)
np.multiply(s, y)
np.divide(s, y)
np.std(s), np.std(y)
np.var(s), np.var(y)
np.min(s), np.min(y)
np.max(s), np.max(y)
np.mean(s), np.mean(y)
np.median(s), np.median(y)
np.sum(s), np.sum(y)
np.sqrt(s), np.sqrt(y)

# 7.2. Veri okuma

# csv dosyalari en yaygin kullanima sahiptir
# csv dosyasini okumak icin 'read_csv' metodu cagrilir.
# farkli veri yapilari olmasi durumunda dokumantasyon oku.

df = pd.read_csv('00_course_materials/01_python_for_data_science/data_analysis_with_python/datasets/breast_cancer.csv')
df.head()

dff = pd.read_excel('11_projects/datasets/biomass_pretreatment.xlsx')
dff.head()

# 7.3. Veriye hizli bakis

df = sns.load_dataset('titanic')
df.head()  # ilk 5 gozlem
df.tail()  # son 5 gozlem
df.shape  # boyut bilgisi
df.info()  # degiskenler ve degisken tipleri hakkinda bilgi verir
df.columns  # degisken isimlerini verir
df.index  # indexlerin nerde baslayip nerde bittigini ve adim sayisini verir
df.describe().T  # betimsel istatistikler
df.isnull()  # true-fals dan olusan bir veri seti doner
df.isnull().values  # veri tipini ndarray e donusturur
df.isnull().values.any()  # veri setinde bos deger olup olmadigini dogrular.
df.isnull().sum().sort_values(ascending=False)  # her bir degiskenin kac eksik degerinin oldugunu verir
df.sex.value_counts()  # kategorik bir degiskenin sinif sayisini verir. cok onemli ve limiz ayagimizdir

# 7.4. Pandasta secim islemleri

# en onemli islemelerden biridir ve cok iyi bilinmelidir

df = sns.load_dataset('titanic')
df.head()
df.index  # indexlere gider.
df[0: 13]  # bellirli bir aralikta secim islemi
df.drop(0, axis=0)  # indexlerde silme islemi # 0, 0. indexi temsil eder. # axis=0 satirlari temsil eder

# fany index ile birden fazla gozlemin silinmesi
deleted_index = [1, 3, 4, 5, 6, 7, 8, 9]
df.drop(deleted_index, axis=0)
    # yukaridaki silme islemi kalici degildir. kalici olmasi icin:
        # atama islemi yapilmaldiir (1)
        # 'inplace=True' argumani eklenebilir (2) # genelde bu islem kullanilir

# degiskeni indexe cevirme
    # once degiskenler secilir
df['age']
# veya
df.age

    # age degiskenini indexe atma
df.index = df.age
df.index
    # age degiskeni, sütunlardan silinir
df.drop('age', axis=1)
    # 'age' degiskenini kalici silmek icin 'inplace=True' argumani eklenir
df.drop('age', axis=1, inplace=True)

# indexi degskene cevirme
    # bu islem 2 seklide gerceklestirilir
    # yontem 1: dataframe nin icerisinde olmayan bir isimlendirmeyi girerek
df['age'] = df.index
df.drop('age', axis=1, inplace=True)
df.head()
df.reset_index()
df.reset_index(inplace=True)

# 7.5. Degiskenle uzerinde islemler

df = sns.load_dataset('titanic')

# Dataframe de herangi bir degiskenin var olup olmadigini sorgulama
'age' in df.columns
'mustafa' in df.columns

# ozellikle bir degisken secme
df['age'].head()   # veya
df.age.head()

# secilen bir degiskenin tipi
type(df['age']) # pandas.core.series.Series
type(df[['age']]) # pandas.core.frame.DataFrame

    # tek bir degisken secerken secimin sonucunun datafaram olarak kalmasini istiyorsak, bu durumda iki koseli parantez '[[]]' kullanarak secim yapilmalidir. secim islemini yaparkan buna dikkat edilmelidir.

df[['age']].head()

# birden fazla degisken secme
df[['age', 'sex']].head()

# fancy index ile yukaridaki islemi gerceklestierme
col_names = ['age', 'sex']
df[col_names].head()

# dataframe degisken ekleme
df['age2'] = df['age'] * 2
df['age3'] = df['age'] / df['age2']

# bir degiskeni silme
df.drop('age3', axis=1).head()  # kalici bir silme islemi degildir. bunun icin 'inplace=True' argumanini ekle

# birden fazla degiskeni silme
col_names = ['age', 'adult_male', 'alive']
df.drop(col_names, axis=1).head()   # kalici bir silme islemi degildir.

# veri setinde belirli bir ifadeyi barindiran degiskenleri silme
    # 'age' iceren degiskenleri secme
df.loc[:, df.columns.str.contains('age')].head() # loc - local based

    # 'age' iceren degiskenleri silmek icin tilda (~) isareti kullanilir
df.loc[:, ~df.columns.str.contains('age')]
    # loc, dataframe de sevcme islemleri icin kullanilan bir ozel yapidir
    # contains metodu stringlere uygulanan bir metottur ve bu metodun icerisine string bir ifade yazilir.

# sayisla bir degiskeni kategorik bir degisken cevirme
df['col_name'] = df['col_name'].astype('category')
df['col_name'].dtype    # 'category

df['age'].dtype     # dtype('float64')
df['age'] = df['age'].astype('category')
df['age'].dtype     # category

# 7.6. loc ve iloc

# Secim islemleri icin kullanilir
# iloc - integer_based: index bilgisi vererek secim islemleri yapma
# loc - local_based:  indexlerdeki labellara gore secim yapar

df = sns.load_dataset('titanic')
df.head()

# iloc
df.iloc[0:3] # 3. indexe kadar gozlemleri getirir
df.iloc[0, 0]   # 0. gozlem birimi ve 0. degiskeni geitir
df.iloc[0:3, 0:3]   # iki boyutlu secim yapma

# loc
df.loc[0:3] # mutlak olarak isimlendirmenin kendinisi secer. buradaki secim isleminde 3. index dahildir.

# loc ve iloc arasindaki fark
# iloc ile satirlarda 0 dan 3 e kadar secelim ve sutunlarda da bir degisken secelim
df.iloc[0:3, 'age'] # ValueError hatasi verir. cunku iloc, integer-based secim yapar ve burada index bekler
df.iloc[0:3, 0:3]   # bu durumda hata vermez.
# bu islemlern aynisi loc ile yapilabilir
df.loc[0:3, 'age']  # bu durumda 'age' degiskeni secilmis olur
# satir ya da indexlerdeki degerlerin bizzat kendilerine gore secim islemi yapmak istersek bu durumda 'loc kullanilir.
# fancy index kavrami
col_names = ['age', 'embarked', 'alive']
df.loc[0:3, col_names]

# 7.7. Kosullu secim

# yasi 50 den buyuk olanlara eriselim
df[df['age'] > 50].head()
# yasi 50 den buyuk kac kisi var
df[df['age'] > 50].count()  # bu ifade sonuctan herhangi bir degisken secmedigimiz icin degiskenlerin tamaminda yasi 50 den buyuk olanlari sayar.
df[df['age'] > 50]['age'].count()   # yasi 50 den buyuk kas kisinin oldugunu sayar.

# yasi 50 den buyuk 'class' degerlerini getirme
df.loc[(df['age'] > 50), 'class'].head()
df[df['age'] > 50]['class'].head()

# yikaridaki kodlamaya 'age' degiskenini de ekleyelim
df.loc[(df['age'] > 50), ['age', 'class']].head()
df[df['age'] > 50][['age', 'class']].head()

# yasi 50 den buyuk erkekleri secme ve bunlarin 'age' ve 'class' degiskenlerini getirme
df.loc[(df['age'] > 50) & (df['sex'] == 'male'), ['sex', 'age', 'class']].head()

# yasi 50 den buyuk erkekleri, yolculuk icin gemiye binilen limani ifade eden 'embark_town' deiskeninden 'Cherbourg' limanin secelim ve bunlarin 'age', 'class' ve 'embark_town' degiskenlerini getirme
df.loc[(df['age'] > 50) & (df['sex'] == 'male') & (df['embark_town'] == 'Cherbourg'), ['age', 'class', 'embark_town']]

df[(df['age'] > 50) & (df['sex'] == 'male') & (df['embark_town'] == 'Cherbourg')][['age', 'class', 'embark_town']]

# yasi 50 den buyuk erkekleri, yolculuk icin gemiye binilen limani ifade eden 'embark_town' deiskeninden 'Southampton' veya 'Cherbourg' limanin secelim ve bunlarin 'age', 'class' ve 'embark_town' degiskenlerini getirme

df.loc[(df['age'] > 50) & (df['sex'] == 'male') & ((df['embark_town'] == 'Cherbourg') | (df['embark_town'] == 'Southampton')), ['age', 'class', 'embark_town']]

df[(df['age'] > 50) & (df['sex'] == 'male') & ((df['embark_town'] == 'Cherbourg') | (df['embark_town'] == 'Southampton'))][['age', 'class', 'embark_town']]

# 7.8. Toplulastirma ve gruplama

# toplulastirma, bir veri yapisinin icinde barinan degerleri toplu bir sekilde temsil etmektir.
# toplulastirma fonksiyonlari, ozet istatistikler ve betimleme istatistikleri verir
# count(), first(), last(), mean(), median(), std(), max(), min(), var(), sum(), pivot_table()
# pivot_table() haric diger toplulastirma fonksiyonlari, gruplama islemi ile birlikte kullanilir.
# once gruplama islemi yapilir, sonrasinda toplulastirma fonksiyonlari kullanilir.

# kadinlarin ve erkeklerin yas ortalamasina eriselim. bu durumda cinsiyete gore yas ortalamasi alinir. ancak norlamlde yas ortalamasi asagidaki gibi elde edilirdi.
df['age'].mean()

# fakat kadin ve erkeklerin yas ortalamasin almak icin 'sex' degiskenine gore kirilim yapildiktan sonra yas degiskeninin ortalamasi alinir.

df.groupby('sex').agg({'age': 'mean'})
df.groupby('sex')['age'].mean()

# birden fazla toplulastirma fonksiyonu groupby ile birlikte kullanilabilir. ornegin, 'sex' degiskeni kiriliminda kadin ve erkeklerin yas ortalamasi ile birlikte sayilarini ve yas toplamlarini ele alalim
df.groupby('sex').agg({'age': ['mean', 'count', 'sum']})

# 'sex' degiskenine gore kirdiktan sonra 'age' degiskeninin ortalamasi ve toplamini ve 'embark_town' degiskeninin frekansini getirelim
df.groupby('sex').agg({'age': ['mean', 'sum'], 'embark_town': ['count']})
# buradan cikan sonuc, embark_town degiskeninin frekansini degil de sex degiskeninin frekansini getirmistir. Bu nedenle pivot_table burada kullailmalidir. dolayisiyla groupby a aldiktan sonra sayisal bir degisken girilmelidir. kategorik degiskenlerde grupby islemi calismamaktadir.

# sex degiskenine gore kirdiktan sonra 'age' degiskeninin ortalamasi ve toplamini ve survived degiskeninin de ortalamasini alalim
df.groupby('sex').agg({'age': ['mean', 'sum'], 'survived': 'mean'})

# birden fazla kategorik degiskene gore kirilm yapma
# 'sex' ve 'embarked' degiskenine gore kirilim yaptiktan sonra age ve survived degiskenlerinin ortalamasini alalim
df.groupby(['sex', 'embarked']).agg({'age': ['mean'], 'survived': 'mean'})

# 'sex', 'embarked' ve 'class' degiskenlerine gore kirilim yaptiktan sonra age ve survived degiskenlerinin ortalamasini alalim
df.groupby(['sex', 'embarked', 'class']).agg({'age': ['mean'], 'survived': 'mean'})

# 7.9. Pivot Table

# veri setini kirilimlar acisindan degerlendirmek ve ilgilendigimiz ozet istatistikleri bu kirilimlar acisindan gorme imkani saglar.
# sex ve embarked degiskeni acisinda pivot_table olusturmak ve kesisiminde de survived degiskeni bilgisine erisme
df.pivot_table('survived', 'sex', 'embarked')
# 1. arguman: values argümanidir. kesisimlerde gormekistedigimiz argümandir
# 2. index, yani satir icin girilen deger
# 3. sütun icin girilen deger

# pivot_table metodunun on tanimli argümani 'mean' dir. bu 'aggfunc' argümanin girilerek degisitirilebilir.
df.pivot_table('survived', 'sex', 'embarked', aggfunc='std')    # standard sapma
df.pivot_table('survived', 'sex', 'embarked', aggfunc='var')    # varyans

# sütun acisindan birden fazla boyut ekleme
# ornegin embarked degiskeni ile birlikte 'class' degiskenini boyut olarak ekleyelim
df.pivot_table('survived', 'sex', ['embarked', 'class'])

# hem satir hem de stün acisindan iki seviyeli boyut ekleme
# ornegin sütuna 'embarked' degiskeni ile birlikte 'class' degiskenini ve satira da 'sex' degiskeni ile 'alive' degiskenlerini boyut olarak ekleyelim
df.pivot_table('survived', ['sex', 'alive'], ['embarked', 'class'])

# amac hem 'sex', hem 'embarked' hem de 'age' degiskenlerine gore kirilim yapalim.
# burada 'age' degiskeni sayilsa bir degisken oldugundan pivot tabloya degisken olarak ekleyebilmek icin bunun kategorik bir degiskene dnusuturlmasi gerekmektedir. bunu yapmanin yolu 'cut' ve 'qcut' metotlarini kullanmaktir. eger sayisal degiskeni hangi kategorilere bolmek istedigimizi biliyorsak bu durumda 'cut()' metodu kullanilmalidir. eger sayisal degiskeni tanimiyorsak ve ceyreklik degerlerine gore bolunsun istiyorsak bu durumda 'qcut()' metodu kullanilmalidir
# sayisal bir degiskenden yeni bir kategorik degisken olusturma
df['new_age'] = pd.cut(df['age'], [0, 10, 18, 25, 40, 90])
df.head()

# sex ne new_age kiriliminda survived degiskenini inceleme
df.pivot_table('survived', 'sex', 'new_age')

# sex ne ['class', 'new_age'] kiriliminda survived degiskenini inceleme
df.pivot_table('survived', 'sex', ['class', 'new_age'])

# ['sex', 'new_age'] ne 'class' kiriliminda survived degiskenini inceleme
df.pivot_table('survived', ['sex', 'new_age'], 'class')

# 7.10. Apply ve Lambda

# 'apply' satir ya da sütünlarda otomatik olarak fonksiyon calistirma imkani saglar.
# 'lambda' ise def gibi bir fonksiyon tanimlama seklidir. Kullan at bir fonksiyondur

# age degiskeni uzerinden iki yeni degisken olusturalim
df.drop(['new_age'], axis=1, inplace=True)
df['age2'] = df['age'] * 2
df['age3'] = df['age'] * 5
df.head()

# veri setindeki age ile ilgili degiskenleirn 10 sayisina bolunmesi
(df['age']/10).head()
(df['age2']/10).head()
(df['age3']/10).head()
# buradaki ihtiyac, bu islemi yukaridaki gibi her zaman el ile yazamaacagimiz icin bir fonksiyon uygulanmasidir
# for dongusu ile bu islemi gerceklestirebiliriz
for col in df.columns:
    if 'age' in col:
        print((df[col]/10).head())
    
# bu yapilan islemler apply be lambda ile gerceklestirebiliriz
df[['age', 'age2', 'age3']].apply(lambda x: x/10).head()
df.loc[:, df.columns.str.contains('age')].apply(lambda x: x/10).head()
# burda x ler degiskenleri temsil etmektedir.

# fonksiyonun uygulandigi dataframdeki degerleri normallestirme fonksiyonunu kullanarak standartlastirma islemi
# apply ve lambda ile yukaridaki islemi gerceklestirebiliriz
df.loc[:, df.columns.str.contains('age')].apply(lambda x: (x-x.mean())/x.std()).head()
# fonksiyon ile bu islemi gerceklestirme
def standard_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains('age')].apply(standard_scaler).head()

# yapilan degisikliklerin kaydedilmesi
df.loc[:, df.columns.str.contains('age')] = df.loc[:, df.columns.str.contains('age')].apply(standard_scaler).head()
df.head()
# veya
# df.loc[:, ['age', 'age2', 'age3']] = df.loc[:, df.columns.str.contains('age')].apply(standard_scaler).head()

# 7.11. Birlestirme (Join) islemleri

# iki sekilde birlestirme yapilabilir
    # concat() metodu
    # merge() metodu

# rastgele integerlardan 5x3 lük bir numpya arrayi olusturma
m = np.random.randint(1, 30, size=(5, 3))
# pd.DataFrame(), dataframe olusturmak icin kullanilir
# iki farkli dataframe olusturalim
df1 = pd.DataFrame(m, columns = ['var1', 'var2', 'var3'])
df2 = df1 + 99

# yontem 1: concat metodu
pd.concat([df1, df2])
# indexlerde problem var. bunun sebebi, ikisinin de index bilgisini oldugu gibi tutmus olmasidir. 
# bu prblemi duzeltmek icin 'ignore_index=True' argümani girilmelidir
pd.concat([df1, df2], ignore_index=True)

# concat ile birlestirme islemin sütun bazinda yapma
# bunun icin 'axis=1' argumani girilir
pd.concat([df1, df2], ignore_index=True, axis=1)

# yontem 2: merge() metodu
# bu yontem detayli birlestirme islemlerinin yapilmasina imkan tanir.
df1 = pd.DataFrame({
    'employees': ['John', 'Dennis', 'Mark', 'Maria'],
    'group': ['accounting', 'engineering', 'engineering', 'hr']
})

df2 = pd.DataFrame({
    'employees': ['John', 'Dennis', 'Mark', 'Maria'],
    'start_date': [2010, 2009, 2014, 2019]
})

# birlestirme islemi
pd.merge(df1, df2)
# hangi degiskene gore birlestirme islemini belirtmek icin 'on' argümani kullanilir.
pd.merge(df1, df2, on='employees')

# her bir calisanin müdür bilgisine erismek
df3 = pd.merge(df1, df2)
df4 = pd.DataFrame({
    'group': ['accounting', 'engineering', 'hr'],
    'manager': ['Caner', 'Mustafa', 'Berkcan']
})

pd.merge(df3, df4)