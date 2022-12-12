# 9. Kesifci veri analizi

# 9.1. Genel resim
# Amac, hizli bir sekilde elimize gelen verileri genle fonksiyonlar ile analiz etmektir.
# kütüphaneleri import etme ve veri setini okuma
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset('titanic')
df.head()

# genel resmi gormek icin uygulanacak ilk fonksiyonlar
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum().sort_values(ascending=False)

# genel resmi gormek icin fonksiyon tanimlama
def check_df(dataframe, head=5):
    print('#' * 20, 'head'.upper(), 20 * '#')
    print(dataframe.head(head))
    print('#' * 20, 'tail'.upper(), 20 * '#')
    print(dataframe.tail(head))
    print('#' * 20, 'shape'.upper(), 20 * '#')
    print(dataframe.shape)
    print('#' * 20, 'dtypes'.upper(), 20 * '#')
    print(dataframe.dtypes)
    print('#' * 20, 'info'.upper(), 20 * '#')
    print(dataframe.info())
    print('#' * 20, 'null values'.upper(), 20 * '#')
    print(dataframe.isnull().sum().sort_values(ascending=False))
    print('#' * 20, 'descriptive statistics'.upper(), 20 * '#')
    print(dataframe.describe([0.0, 0.05, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99, 1]).T)

check_df(df)

# yeni bir veri setine tanimlanan fonksiyounu uygulama
dff = sns.load_dataset('tips')
check_df(dff)

# 9.2. Kategorik degisken analizi

# amac: tek bir kategorik degiskeni analiz etmek
df['embarked'].value_counts()   # sinif sayilarina erisme
df['sex'].unique()      # essiz degerlere erisme
df['sex'].nunique()     # toplam essiz deger sayisina erisme
df['class'].nunique()

# kategorik degiskenleri secme
cat_cols = [col for col in df.columns if df[col].dtypes == 'O']

# sayisal ama kategorik olan degiskenleri yapakalama
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes != 'O']

# kategorik ama kardinal olan degiskenleri yakalama
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and df[col].dtypes == 'O']

# num_but_cat de bir kategorik degisken oldugundan cat_cols icerisine dahil edilir
cat_cols = cat_cols + num_but_cat
df[cat_cols].head() # kategorik degiskenler cikti olarak gelir
df[cat_cols].nunique()  # kategorik degisknler acisindan yapilan islemlerin dogrulanmasi, essiz sinif sayisi

# veri setindeki sayisla degiskenler (num cols)
num_cols = [col for col in df.columns if df[col].dtypes != 'O'] # tipi object olmayanlar secilir
num_cols = [col for col in num_cols if col not in cat_cols] # cat_cols icerisinden cikarilir

# kategorik degiskenlerin bilgilerini ozeleyen bir 'cat_summary' fonksiyonu yazma
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({
        col_name: dataframe[col_name].value_counts(),
        'Ratio (%)': 100 * (dataframe[col_name].value_counts() / len(dataframe))
    }))

cat_summary(df, 'sex')

# cat_summary fonksiyonuna grafik ozelligi ekleme
def cat_summary(dataframe, col_name, plot=False):
    print('\n', '#'*10, col_name.upper(), '#'*10)
    print(pd.DataFrame({
        col_name.upper(): dataframe[col_name].value_counts(),
        'RATIO (%)': round(100 * (dataframe[col_name].value_counts() / len(dataframe)), 2)
    }))

    if plot:
        sns.countplot(x=dataframe[col_name])
        plt.show(block=True)

cat_summary(df, 'sex', plot=True)

df['alone'].dtype

for col in cat_cols:
    cat_summary(df, col, plot=True)

# 9.3. Sayisal degisken analizi

# amac, titanic veri setindeki sayisla degiskenlerin betimsel istatisitikleri
numeirical_cols = ['age', 'fare']
df[numeirical_cols].describe().T

# progromatik olrak sayisal degiskenleri secme
num_cols = [col for col in df.columns if df[col].dtypes != 'O'] # buradan gelen degiskenler sayisal gorunumlu kategorik degiskenlerdir
num_cols = [col for col in num_cols if col not in cat_cols] # sayisal gorunumlu kategorik degiskenlerden, kategorik degiskenler silinmistir

# sayisal degiskenleri ozetleyen bir 'num_summary' fonksiyonu yazma
def num_summary(dataframe, numerical_col, plot=False):
    print('\n', '#'*10, numerical_col.upper(), '#'*10)
    quantiles = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99, 1]
    print(pd.DataFrame({
        numerical_col.upper(): round(dataframe[numerical_col].describe(quantiles).T, 2)
    }))

    if plot:
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        sns.boxplot(y=dataframe[numerical_col])
        plt.subplot(1, 2, 2)
        sns.histplot(x=dataframe[numerical_col])
        plt.show(block=True)

num_summary(df, 'age', plot=True)

for col in num_cols:
    num_summary(df, col, plot=True)

# 9.4. Degiskenlerin yakalanmasi

# veri setindeki kategorik, sayisal ve kardinal degiskenleri yakalan 'grab_col_names' fonksiyonu
def grab_col_names(dataframe, cat_th=10, car_th=20):
    # kategorik degiskenler
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == 'O']
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtypes != 'O']
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and dataframe[col].dtypes == 'O']
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # sayisal degiskenler
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != 'O']
    num_cols = [col for col in num_cols if col not in num_but_cat]

    # raporlama bölümü
    print(f'Observations: {dataframe.shape[0]}')
    print(f'Variables: {dataframe.shape[1]}')
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    # hesaplanan degerleri tutma
    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df)

# farkli veri seti icin grab_col_names fonksiyonunu deneme
dff = sns.load_dataset('tips')
cat_cols, num_cols, cat_but_car = grab_col_names(dff)

# kategorik degiskenleri ozetleyen cat_summary fonksiyonunu grab_col_names ile kullanalim
cat_cols, num_cols, cat_but_car = grab_col_names(df)

for col in cat_cols:
    cat_summary(df, col, plot=True)

# sayisal degiskenleri ozetleyen num_summary fonksiyonunu grab_col_names ile kullanalim
for col in num_cols:
    num_summary(df, col, plot=True)

# 9.5. Hedef degiskenin analizi

# hedef degiskenin kategorik degiskenler ile analiz edilmesi
df.groupby('sex').agg({'survived': 'mean'})

# hedef degiskeni kategorik degiskenler ile analiz eden 'target_summary_with_cat' fonksiyonun yazma
def target_summary_with_cat(dataframe, target, categorical_col, plot=False):
    print('\n', '#' * 10, categorical_col.upper(), '#' * 10)
    print(pd.DataFrame({
        'TARGET_MEAN': round(dataframe.groupby(categorical_col)[target].mean(), 2)
    }), end='\n\n')

    if plot:
        sns.barplot(x=dataframe[categorical_col], y=dataframe[target])
        plt.show(block=True)

target_summary_with_cat(df, 'survived', 'sex')

cat_cols = [col for col in cat_cols if 'survived' not in col]

for col in cat_cols:
    target_summary_with_cat(df, 'survived', col, plot=True)

# hedef degiskenin sayisal degiskenler ile analiz edilmesi
# groupby() fonksiyonuna bagimli degisken girilir
def target_summary_with_num(dataframe, target, numerical_col, plot=False):
    print('\n', '#' * 10, numerical_col.upper(), '#' * 10)
    print(round(dataframe.groupby(target).agg({numerical_col: 'mean'}), 2))

    if plot:
        sns.barplot(x=dataframe[target], y=dataframe[numerical_col])
        plt.show(block=True)

target_summary_with_num(df, 'survived', 'age')

for col in num_cols:
    target_summary_with_num(df, 'survived', col, plot=True)

# 9.6 Korelasyon analizi
# her calismada yapilamayan bir islemdir
# ihtiyac oldugunda analiz araci olarak kullanilmalidir

# breast_cancer veri setini import etme

df_titanic = pd.read_csv('datasets/breast_cancer.csv')
df_titanic = df_titanic.iloc[:, 1:-1]
df_titanic.head()

cat_cols, num_cols, cat_but_car = grab_col_names(df_titanic)
check_df(df_titanic)
num_cols

# korelasyonu hesaplamak icin corr() fonksiyonu kullanilir
corr = df_titanic[num_cols].corr()

"""
korelasyon, degiskenlerin birbiri ile iliskisini ifade edne bir istatistiksel ölcümdür
-1 ile +1 arasinda degisir. 
-1 (negatif korelasyon) veya +1 (pozitif korelasyon) e yaklastikca iliskinin siddedti kuvvetlenir
0 civarindaki bir korelasyon, korelasyonun olmadigi anlamina gelir
Genellikle analitik calismalarda birbiri ile yuksek korelasyonlu degiskenlerin bulunmamasi istenir.
Cunku bu durumda her iki degisken de ayni seyi ifade etmektedir
"""

# isi haritasi (heatmap) olusturma
plt.figure(figsize=(12, 12))
sns.heatmap(corr, cmap='RdBu')
plt.show(block=True)

# yüksek korelasyonlu degiskenlerin silinmesi
    # negatif korelasyonlari pozitife donusturme
cor_matrix = df_titanic.corr().abs()

    # matrixteki gereksiz bilgilerin silinmesi
upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))

    # korelasyonu 0.90 dan buyuk olan degiskenlerin secilmesi
drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90)]

    # silme islemi
df_titanic.drop(drop_list, axis=1).shape[1]

# yüksek korelasyonlu degiskenleri silmek icin 'high_correlated_cols' fonksiyonu
def high_correlated_cols(dataframe, corr_th=0.90, plot=False):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool_))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]

    if plot:
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, cmap='RdBu', annot=True, annot_kws={'fontsize': 5})
        plt.show(block=True)

    return drop_list

high_correlated_cols(df_titanic)    # silinmesi gereken kolonlar
drop_list = high_correlated_cols(df_titanic, plot=True)     # kaydetme islemi
high_correlated_cols(df_titanic.drop(drop_list, axis=1), plot=True)     # silme islemi

from helpers import eda
df = eda.load_excel('datasets/microwave_pretreatment.xlsx')
df.head()