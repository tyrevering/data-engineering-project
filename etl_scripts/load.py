# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 20:57:21 2023

@author: tyler
"""

from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Exporting data to a BigQuery warehouse.
    Specified configuration settings in 'io_config.yaml'.
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    for key, value in data.items():
        ID = 'intricate-tempo-390717.grocery_data_engineering.{}'.format(key)
        BigQuery.with_config(ConfigFileLoader(config_path,
                                              config_profile)).export(
            DataFrame(value),
            ID,
            if_exists='replace')
