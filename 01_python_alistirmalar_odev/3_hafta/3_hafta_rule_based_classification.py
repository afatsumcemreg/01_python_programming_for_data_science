# import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# import dataset and get the general information about the dataset
df = pd.read_csv("01_python_programming_for_data_science/01_python_alistirmalar_odev/3_hafta/persona.csv")
df.columns = [col.lower() for col in df.columns]
df.head()

def check_df(dataframe):
    print(dataframe.head())
    print(dataframe.tail())
    print(dataframe.shape)
    print(dataframe.columns)
    print(dataframe.info())
    print(dataframe.isnull().values.any())
    print(dataframe.isnull().sum())
    print(dataframe.describe([0.05, 0.1, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]).T)

check_df(df)

# Unique SOURCE number and frequences?
df['source'].unique()
df['source'].nunique()
df['source'].value_counts()
sns.countplot(x=df['source'])
plt.show(block=True)
# df.groupby('source').count()

# Unique PRICE number?
df['price'].nunique()
df['price'].unique()
sns.countplot(df['price'])
plt.show(block=True)

# price numbers
df['price'].value_counts()

# price numbers of countries
df['country'].value_counts()

# accrdong to countries, sum of prices
df.groupby('country').agg({'price': 'sum'})

# according to source types, number of prices
df.groupby('source').agg({'price': 'count'})

# according to countries, means of price
df.groupby('country').agg({'price': 'mean'})

# according to sources, means of price
df.groupby('source').agg({'price': 'mean'})

# in the breakdown country and source, means of price
df.groupby(['country', 'source']).agg({'price': 'mean'})

# in the breakdown country, source, sex, and age, means of price
df.groupby(['country', 'source', 'sex', 'age']).agg({'price': 'mean'}).head()

# Sort the output by PRICE?
age_df = df.groupby(['country', 'source', 'sex', 'age']).agg({'price': 'mean'}).sort_values('price', ascending=False)
age_df.head()

# convert the names in the indexes to the variable name
age_df.reset_index(inplace=True)
age_df.head()

# convert the age variable into categorical variable and add it to age_df
age_df['age_cat'] = pd.cut(age_df['age'], bins=[0, 18, 23, 30, 40, 70], labels=['0_18', '19_23', '24_30', '31_40', '41_70'])
age_df.head()
# age_df.drop('a_cat', axis=1, inplace=True)

# define a level-based customers (persona) named 'customers_level_based'
age_df['customers_level_based'] = ['_'.join(i).upper() for i in age_df.drop(['age', 'price'], axis=1).values]
age_df.head()

# amelasyon
# age_df['customers_level_based'] = [col[0].upper() + '_' + col[1].upper() + '_' + col[2].upper() + '_' + col[5].upper() for col in age_df.loc[:, age_df.columns].values]

# age_df['customers_level_based'] = [col[0].upper() + '_' + col[1].upper() + '_' + col[2].upper() + '_' + col[3].upper() for col in age_df[['country', 'source', 'sex', 'age_cat']].values]
# age_df.head()

age_df = age_df.groupby('customers_level_based').agg({'price': 'mean'})
age_df.reset_index(inplace=True)
age_df.head()
age_df.shape

# segement new customers (personas)
age_df['segment'] = pd.qcut(age_df['price'], 4, labels=['D', 'C', 'B', 'A'])
age_df.head()
age_df.groupby('segment').agg({'price': ['mean', 'max', 'sum']})

# classify new customers and estimate how much revenue they can generate
new_user_1 = 'TUR_ANDROID_FEMALE_31_40'
age_df[age_df['customers_level_based'] == new_user_1]

new_user_2 = 'FRA_IOS_FEMALE_31_40'
age_df[age_df['customers_level_based'] == new_user_2]