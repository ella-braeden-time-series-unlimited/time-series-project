# Imports
import numpy as np
import pandas as pd
import os

from datetime import datetime

import env
from env import user, password, host



def wrangle_superstore():
    '''
    
    '''
    
    filename = 'superstore.csv'
    
    if os.path.exists(filename):
        print('Reading cleaned data from csv file...')
        return pd.read_csv(filename)
    
    # Pull from SQL
    query = '''
        SELECT orders.*, products.`Product Name`, categories.Category, categories.`Sub-Category`, regions.`Region Name`
        FROM orders
        LEFT JOIN products ON orders.`Product ID` = products.`Product ID`
        LEFT JOIN categories ON orders.`Category ID` = categories.`Category ID`
        LEFT JOIN regions ON orders.`Region ID` = regions.`Region ID`;
        '''

    url = f"mysql+pymysql://{env.user}:{env.password}@{env.host}/superstore_db"

    df = pd.read_sql(query, url)
    
    # Rename columns
    df = df.rename(columns={
                    'Order ID': 'order_id',
                    'Order Date': 'order_date',
                    'Ship Date': 'ship_date',
                    'Customer ID': 'customer_id',
                    'Postal Code': 'zip_code',
                    'Category ID': 'category_id',
                    'Region ID': 'region_id',
                    'Region Name': 'region_name',
                    'Ship Mode': 'shipping_method'})
    
    df.columns= df.columns.str.lower()
    
    # Set order_date to index
    df['order_date'] = pd.to_datetime(df['order_date'])

    df = df.set_index('order_date').sort_index()
    
    # Download cleaned data to a .csv
    df.to_csv(filename, index=False)
    
    print('Downloading data from SQL...')
    print('Saving to .csv')
    return df