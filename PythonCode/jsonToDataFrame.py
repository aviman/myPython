"""
Python Programme to read a json output from elasticsearch api call to index and load to DataFrame
"""

import pandas as pd
import json

with open('InputFiles\hits.json','r') as f:
    data = json.loads(f.read())
df_nested_list = pd.json_normalize(data)
df_nested_list_hits = pd.json_normalize(df_nested_list['hits.hits'][0])
df_nested_list_hits.drop(columns=['_source.@version', '_source.@timestamp'],inplace=True)
df_nested_list_hits_source = df_nested_list_hits.filter(regex='_source.*')
df_nested_list_hits_source.columns = df_nested_list_hits_source.columns.str.replace('_source.', '')
