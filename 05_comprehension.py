########################################
# 5. Comprehensions
########################################

########################################
# 5.1. List comprehension
########################################

"""
Birden fazla satir ve kod ile yapilabilecek islemleri kolyaca istedigimiz cikti veri yapisina gore tek bir satirda gerecklestirme imkani saylar.
"""
# Klasik yol ile yapilan islem

salaries = [1000, 2000, 3000, 4000, 5000]

# Maaslara %20 zam yapilmasinin gerektiren bir fonksiyon yazalim

def new_salary(x):
    print(x * 1.2)

for salary in salaries:
    new_salary(salary)

# Zam yapilan maaslari yeni bir listeye ekleme
null_list = []
for salary in salaries:
    null_list.append(new_salary(salary))

# Kosullu islemler

null_list = []
for salary in salaries:
    if salary < 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary))

# Yukaridaki islemlerin list comprehension ile yapilmasi

[salary * 1.2 for salary in salaries]

[new_salary(salary) for salary in salaries]

[salary * 2 if salary < 3000 else salary for salary in salaries]

# Bu konu programin bel kemigidir ve cok iyi ogrenilmelidir.

# Maaslar listesindeki her bir maasi 2 ile carpalim
[salary * 2 for salary in salaries]

# Maasi 3000 den az olanlari 2 ile carpalim
[salary * 2 for salary in salaries if salary < 3000]

# Maasi 3000 den az olanlari 4, fazla olanlari 2 ile carpalim
[salary * 4 if salary < 3000 else salary * 2 for salary in salaries]

# Var olan bir fonksiyonu yapinin icerisinde kullanma

[new_salary(salary * 4) if salary < 3000 else new_salary(salary * 2) for salary in salaries]

# Istenilen ogrencilerin isimlerini buyuk, istenmeyenlerinkini kucuk yazalim
students = ['john', 'mark', 'venessa', 'mariam']
students_no = ['john', 'venessa']

[student.upper() if student not in students_no else student.lower() for student in students]
[student.lower() if student in students_no else student.upper() for student in students]

########################################
# 5.2. Dict comprehension
########################################

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
dictionary.keys()
dictionary.values()
dictionary.items()

# Her bir value nin karesinin alalim
{k: v ** 2 for k, v in dictionary.items()}

# Her bir key i buyuk harfe donusturelim
{k.upper(): v for k, v in dictionary.items()}

# Ayni anda hem key hem value uzerinde islem yapalim
{k.upper(): v ** 2 for k, v in dictionary.items()}

# Uygulama - Dict comprehension

# Amac: Bir listedeki cift sayilarin karesi alinarak bunlari bir sozluge eklemektir.
# Key degerleri orjinal degerler, value ler ise degistirilmis olmalidir.

number = range(10)

# Klasik yol
new_dict = {}
for i in number:
    if i % 2 == 0:
        new_dict[i] = i ** 2

print(new_dict)

# Dict comprehension

{k: k ** 2 for k in number if k % 2 == 0}

# Amac: Br veri setindeki degisken isimlerini buyuk harfe degistirmek
import seaborn as sns
df = sns.load_dataset('car_crashes')
df.columns

# list comprehension
[col.upper() for col in df.columns]

# kalsik yol
A = []
for col in df.columns:
    A.append(col.upper())

print(A)
df.columns = A
df.columns

# Amac: isminde 'INS' olan degiskenlerin basina FLAG, digerlerine NO_FLAG eklemek

# list comprehension
['FLAG_' + col if 'INS' in col else 'NO_FLAG_' + col for col in df.columns]

# klasik yol
A = []
for col in df.columns:
    if 'INS' in col:
        A.append('FLAG_' + col)
    else:
        A.append('NO_FLAG_' + col)

print(A)

# Amac: key degeri string ve value degeri de asagidaki gibi bir liste olan soyzluk olusturmak.
# Bu islem, sadece sayisal degiskelnler icin yapilir.
# output: {'total': ['mean', 'min', 'max', 'var]}
# veri okuma

df = sns.load_dataset('car_crashes')
df.columns

num_cols = [col for col in df.columns if df[col].dtypes != 'O']

# klasik yontem
sozluk = {}
agg_list = ['mean', 'min', 'max', 'var']
for col in num_cols:
    sozluk[col] = agg_list

print(sozluk)

# dict comprehension
{col: agg_list for col in num_cols}

# olusturalun sozlugu kaydetme
new_dict = {col: agg_list for col in num_cols}
df[num_cols].head()
df[num_cols].agg(new_dict)