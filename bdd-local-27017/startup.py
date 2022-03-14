#!/usr/bin/env python
import sys 
import pandas as pd
import os
import pymongo
import json

MOVIE_CY_HOME = '/home/eisti/movie_cy'


def import_content(filepath):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['MOVIE_DB'] 
    collection_name = 'MOVIE' 
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)
    data = pd.read_csv(file_res, encoding= 'unicode_escape')
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

if __name__ == "__main__":
  filepath = 'Sample-Spreadsheet-10-rows.csv' 
  database = 'MOVIE_DB'
  collection_name = 'MOVIE'
  name_file = os.path.join(MOVIE_CY_HOME, 'local', 'data.tsv')
  test = f"string"
  com = f"mongoimport --db {database} --collection {collection_name} --type tsv --file {name_file} --headerline --port=27017"
  os.system(com)
  # import_content(filepath)