import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno 
amazon = pd.read_csv('/kaggle/input/unlock-profits-with-e-commerce-sales-data/Amazon Sale Report.csv')
amazon.info()
amazon.set_index('index', inplace = True)
msno.matrix(amazon)
msno.bar(amazon)
amazon.nunique()
amazon.apply(pd.unique)
amazon.drop(columns = ['Unnamed: 22','fulfilled-by','ship-country', 'currency','Sales Channel '], inplace = True)
before_remove_duplicates = len(amazon)
amazon.drop_duplicates(inplace = True)
after_remove_duplicates = len(amazon)
duplicate_rows_removed = before_remove_duplicates - after_remove_duplicates
print(f'{duplicate_rows_removed} duplicate rows have been removed! \nThe Dataset now has {after_remove_duplicates} rows.')
amazon[amazon.isnull().any(axis = 1)]
amazon[amazon['promotion-ids'].isnull()]
amazon['promotion-ids'].fillna('no promotion', inplace = True)
amazon['Courier Status'].fillna('unknown', inplace = True)
amazon[amazon['Amount'].isnull()]amazon['Amount'].fillna(0, inplace = True)
msno.matrix(amazon)
amazon[amazon['ship-city'].isnull()]
amazon['ship-city'].fillna('unknown', inplace = True)
amazon['ship-state'].fillna('unknown', inplace = True)
amazon['ship-postal-code'].fillna('unknown', inplace = True)
msno.matrix(amazon)
mapper = {'Order ID':'orderID', 'Date':'date', 'Status':'shipStatus','Fullfilment':'fullfilment', 'ship-service-level':'serviceLevel', 'Style':'style', 'SKU':'sku', 'Category':'productCategory', 'Size':'size', 'ASIN':'asin', 'Courier Status':'courierShipStatus', 'Qty':'orderQuantity', 'Amount':'orderAmount (INR)', 'ship-city':'city', 'ship-state':'state', 'ship-postal-code':'zip', 'promotion-ids':'promotion','B2B':'customerType' }
amazon.rename(columns = mapper, inplace = True)
amazon.head()
amazon['customerType'].replace([True, False], ['business', 'consumer'], inplace = True)
amazon.head()
amazon.info()
amazon['date'] = pd.to_datetime(amazon['date'])
amazon['month'] = amazon['date'].dt.month
amazon['month'].unique()
amazon['date'].max()
amazon['date'].min()
months = ['march','April', 'May', 'June']
amazon['month'].replace([3,4,5,6],months, inplace = True)
amazon.set_index('orderID', inplace = True)
amazon