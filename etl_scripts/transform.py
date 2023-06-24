# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 20:53:12 2023

@author: tyler
"""

import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    df.rename(columns={'ï»¿Order ID': 'Order ID'}, inplace=True)
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

    datetime_dim = df[['Order Date']].drop_duplicates().reset_index(drop=True)
    datetime_dim['datetime_id'] = datetime_dim.index
    datetime_dim['Order_Year'] = datetime_dim['Order Date'].dt.year
    datetime_dim['Order_Month'] = datetime_dim['Order Date'].dt.month
    datetime_dim['Order_Day'] = datetime_dim['Order Date'].dt.day
    datetime_dim[['datetime_id', 'Order Date',
                  'Order_Day', 'Order_Month', 'Order_Year']]

    customer_dim = df[['Customer Name']].drop_duplicates(). \
        reset_index(drop=True)
    customer_dim['Customer_ID'] = customer_dim.index
    customer_dim[['Customer_ID', 'Customer Name']]

    location_dim = df[['Region', 'City',
                       'State']].drop_duplicates().reset_index(drop=True)
    location_dim['location_id'] = location_dim.index

    location_dim[['location_id', 'Region', 'City', 'State']]

    item_dim = df[['Category',
                   'Sub Category']].drop_duplicates().reset_index(drop=True)
    item_dim['Item_ID'] = item_dim.index

    item_dim[['Item_ID', 'Category', 'Sub Category']]

    fact_table = df.merge(datetime_dim, on='Order Date') \
        .merge(customer_dim, on='Customer Name') \
        .merge(location_dim, on=['Region', 'City', 'State']) \
        .merge(item_dim, on=['Category', 'Sub Category']) \
        [['Order ID', 'datetime_id', 'Customer_ID', 'location_id',
          'Item_ID', 'Sales', 'Discount', 'Profit']] \
        .drop_duplicates() \
        .reset_index(drop=True)

    return {'datetime_dim': datetime_dim.to_dict(orient='dict'),
            'customer_dim': customer_dim.to_dict(orient='dict'),
            'location_dim': location_dim.to_dict(orient='dict'),
            'item_dim': item_dim.to_dict(orient='dict'),
            'fact_table': fact_table.to_dict(orient='dict')}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
