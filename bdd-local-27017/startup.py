#!/usr/bin/env python
import sys 
import pandas as pd
import os
import pymongo
import json


MOVIE_CY_TMP = './tmp'
DATABASE = 'MOVIE_DB'
PORT = '27017'
TSV_LINK = 'https://datasets.imdbws.com'

# COLLECTION_NAME = 'MOVIE'
# AKAS_TSV_GZ = 'https://datasets.imdbws.com/title.akas.tsv.gz'
# AKAS_TSV = 'title.akas.tsv.gz'
# MOVIE_CY_HOME = '/home/eisti/movie_cy'

def importCSV(database, port, collection, fileName):
  filePath = f"{MOVIE_CY_TMP}/{fileName}.tsv"
  fileLink = f"{TSV_LINK}/{fileName}.tsv.gz"
  dl = f"wget -P {MOVIE_CY_TMP} {fileLink}"
  os.system(dl)
  gzFile = f"{fileName}.tsv.gz"
  extract = f"gzip -d {MOVIE_CY_TMP}/{gzFile}"
  os.system(extract)
  com = f"mongoimport --db {database} --collection {collection} --type tsv --file {filePath} --headerline --port={port}"
  os.system(com)

def cleanTMP():
  delete = f"rm -R {MOVIE_CY_TMP}"
  os.system(delete)

def initDB():
  importCSV(DATABASE,PORT,'PERSONS','name.basics')
  importCSV(DATABASE,PORT,'MOVIES','title.basics')
  importCSV(DATABASE,PORT,'CREWS','title.crew')
  importCSV(DATABASE,PORT,'PRINCIPALS','title.principals')
  importCSV(DATABASE,PORT,'RATINGS','title.ratings')
  cleanTMP()



if __name__ == "__main__":
  initDB()
  
  # name_file = os.path.join(MOVIE_CY_TMP, 'title.akas.tsv')
  # dl = f"wget -P {MOVIE_CY_TMP} {AKAS_TSV_GZ}"
  # extract = f"gzip -d {MOVIE_CY_TMP}/{AKAS_TSV}"
  # com = f"mongoimport --db {DATABASE} --collection {COLLECTION_NAME} --type tsv --file {name_file} --headerline --port={PORT}"
  # delete = f"rm -R {MOVIE_CY_TMP}"
  
  # os.system(dl)
  # os.system(extract)
  # os.system(com)
  # os.system(delete)
  # import_content(filepath)
