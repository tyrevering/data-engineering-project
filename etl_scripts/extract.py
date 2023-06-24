# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 20:49:30 2023

@author: tyler
"""

import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Extracting data from API
    """
    url = (
        'https://storage.googleapis.com/grocery-sales-data-engineering/'
        'Supermart%20Grocery%20Sales%20-%20Retail%20Analytics%20Dataset.csv'
        )
    response = requests.get(url)

    return pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output, *args) -> None:
    """
    Testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
