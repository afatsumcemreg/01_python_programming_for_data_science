########################################################################################################################
###############################################
def alternating_with_string(string):
    new_string = ''
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    print(new_string)

alternating_with_string('miuul')

###############################################
def alternating_with_list(string):
    new_string = []
    for i in range(len(string)):
        if i % 2 == 0:
            new_string.append(string[i].upper())
        else:
            new_string.append(string[i].lower())
    return new_string

for i in alternating_with_list('miuul'):
    print(i, end='')

###############################################
def alternating_comprehension(string):
    return [letter.upper() if index % 2 == 0 else letter.lower() for index, letter in enumerate(string)]

for i in alternating_comprehension('miuul'):
    print(i, end='')

###############################################
for i in [letter.upper() if index % 2 == 0 else letter.lower() for (index, letter) in enumerate('miuul')]:
    print(i, end='')

########################################################################################################################
import pandas as pd
import seaborn as sns
from helpers import eda
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

df = sns.load_dataset('titanic')
df.columns = [col.lower() for col in df.columns]
df.head()

eda.check_df(df)
cat_cols, num_cols, cat_but_car = eda.grab_col_names(df)
cat_cols = [col for col in cat_cols if 'survived' not in col]

for col in cat_cols:
    eda.cat_summary(df, col, plot=True)

for col in num_cols:
    eda.num_summary(df, col, plot=True)

for col in cat_cols:
    eda.target_summary_with_cat(df, 'survived', col, plot=True)

eda.high_correlated_cols(df, plot=True)
drop_list = eda.high_correlated_cols(df, plot=True)
eda.high_correlated_cols(df.drop(drop_list, axis=1), plot=True)

df.index
deleted_indexes = [1, 3, 5, 7, 9]
df.drop(deleted_indexes, axis=0).head()

df.index = df.age
df.head()
df.drop('age', axis=1, inplace=True)
df.head()

df['age'] = df.index
df.drop('age', axis=1, inplace=True)
df.head()

df.reset_index(inplace=True)
df.head()

'mustafa' in df
'age' in df
'sex' in df
df['age'].head()
df.age.head()
type(df['age'])
type(df[['age']])

df[['age', 'fare']].head()

col_names = ['age', 'fare', 'survived']
df[col_names].head()

df['new_fare'] = df['fare'] * 2
df['new_fare2'] = df['fare'] * 10
df.head()

df.drop('new_fare2', axis=1).head()
# df.drop('new_fare2', axis=1, inplace=True)
df.head()

col_names = [col for col in df.columns if 'fare' in col]
df.drop(col_names, axis=1).head()

df.loc[:, df.columns.str.contains('fare')].head()

df.drop(['fare', 'new_fare', 'new_fare2'], axis=1).values
df.loc[:, ~df.columns.str.contains('fare')].values

df['age'] = df['age'].astype('int')
for col in df.columns:
    if df[col].dtypes == 'category':
        df[col] = df[col].astype(int)
df.info()

df.iloc[0:3]
df.iloc[0, 0]
df.iloc[0:3, 0:3]

df.loc[0:3]
df.loc[0:3, 'age']
df.loc[0:3, col_names]

df = sns.load_dataset('titanic')
df[df['age'] > 50].head()
df['age'][df['age'] > 50].count()
df.loc[df['age'] > 50, 'age'].count()
df.loc[df['age'] > 50, ['age', 'class']].head()
df.loc[(df['age'] > 50) & (df['sex'] == 'male')].head()
df.loc[(df['age'] > 50) & (df['sex'] == 'male'), ['age', 'class', 'sex']]
df.loc[(df['age'] > 50) & (df['sex'] == 'male') & (df['embark_town'] == 'Cherbourg'), ['age', 'class', 'embark_town']]
df.loc[(df['age'] > 50) & (df['sex'] == 'male') & ((df['embark_town'] == 'Cherbourg') | (df['embark_town'] == 'Southampton')), ['age', 'class', 'embark_town']]

df.groupby('sex').agg({'age': 'mean'})
df.groupby('sex').agg({'age': ['mean', 'count']})
df.groupby('sex').agg({'age': ['mean', 'count'], 'embark_town': 'count'})
df.groupby('sex').agg({'age': ['mean', 'sum'], 'survived': 'mean'})
df.groupby(['sex', 'embark_town']).agg({'age': ['mean', 'sum'], 'survived': 'mean'})
df.groupby(['sex', 'embark_town', 'class']).agg({'age': 'mean', 'survived': 'mean', 'sex': 'count'})

df.pivot_table('survived', 'sex', 'embarked')
df.pivot_table('survived', 'sex', 'embarked', aggfunc=['sum', 'var'])    # aggfunc = 'std', 'sum', 'var', 'min', 'max', etc.
df.pivot_table('survived', ['sex', 'alone'], ['embarked', 'class'])
df.pivot_table('survived', 'sex', ['embarked', 'class'])
df['new_age'] = pd.cut(df['age'], [0, 10, 18, 25, 40, 90])
df.head()
df.pivot_table('survived', 'sex', 'new_age')
df.pivot_table('survived', 'new_age', 'sex')
df.pivot_table('survived', ['new_age', 'class'], 'sex')

df['fare1'] = df['fare'] ** 2
df['fare2'] = df['fare'] * 5
for col in df.columns:
    if 'fare' in col:
        print((df[col]/10).head())

df[['fare', 'fare1', 'fare2']].apply(lambda x: x/10).head()
df.loc[:, df.columns.str.contains('fare')].apply(lambda x: (x - x.mean()) / x.std()).head()

def scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains('fare')].apply(scaler).head()

df.loc[:, df.columns.str.contains('fare')] = df.loc[:, df.columns.str.contains('fare')].apply(scaler).head()
df.head()

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=['var1', 'var2', 'var3'])
df2 = df1 + 100
df3 = pd.concat([df1, df2], ignore_index=True)
df3 = pd.concat([df1, df2], ignore_index=True, axis=1)
df3

df1 = pd.DataFrame({'employees': ['mustafa', 'hacer', 'hakan', 'new_member'],
                   'group': ['engineer', 'accounter', 'doctor', 'engineer']})
df2 = pd.DataFrame({'employees': ['mustafa', 'hacer', 'hakan', 'new_member'],
                    'start_date': [2012, 2012, 2018, 2023]})

df3 = pd.merge(df1, df2)

########################################################################################################################
import pandas as pd
import seaborn as sns
from helpers import eda
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
sns.get_dataset_names()
df = sns.load_dataset('titanic')
df.columns = [col.lower() for col in df.columns]
df.head()
