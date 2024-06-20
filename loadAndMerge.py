# Download the Data files from the IMDB Datasets page at https://datasets.imdbws.com/ and save to same folder as this python file.
# title.ratings.tsv.gz
# title.akas.tsv.gz
# title.basics.tsv.gz

# You will then need to extract the data. Go to a terminal, and use the following for each data file
# MAKE SURE YOU'RE IN THE SAME FOLDER THE FILES ARE SAVED IN
# gzip -d title.basics.tsv.gz
# gzip -d title.ratings.tsv.gz
# gzip -d title.akas.tsv.gz

# BE AWARE - THE LOADING SECTION OF THE BELOW TOOK AROUND 15 - 20 MINUTES


import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['imdb']

# Function to load title.basics.tsv into MongoDB with startYear greater than 2000
def load_title_basics(file_path, collection_name):
    df = pd.read_csv(file_path, delimiter='\t', na_values='\\N', dtype={'startYear': 'str'}, low_memory=False)
    df['startYear'] = pd.to_numeric(df['startYear'], errors='coerce')
    df = df[df['startYear'] >= 2000]
    df.fillna("", inplace=True)
    records = df.to_dict(orient='records')
    db[collection_name].insert_many(records)
    return df

# Function to load title.ratings.tsv into MongoDB
def load_title_ratings(file_path, collection_name):
    df = pd.read_csv(file_path, delimiter='\t', na_values='\\N', low_memory=False)
    df.fillna("", inplace=True)
    records = df.to_dict(orient='records')
    db[collection_name].insert_many(records)
    return df

# Function to load title.akas.tsv into MongoDB with region equal to US
def load_title_akas(file_path, collection_name):
    df = pd.read_csv(file_path, delimiter='\t', na_values='\\N', low_memory=False)
    df.rename(columns={'titleId': 'tconst'}, inplace=True)  # Rename titleId to tconst to be able to merge later
    df = df[df['region'] == 'US']
    df.fillna("", inplace=True)
    records = df.to_dict(orient='records')
    db[collection_name].insert_many(records)
    return df

# Load 3 Dataframes to MongoDB
basics_df = load_title_basics('title.basics.tsv', 'title_basics')
ratings_df = load_title_ratings('title.ratings.tsv', 'title_ratings')
akas_df = load_title_akas('title.akas.tsv', 'title_akas')


# Function to Merge DataFrames
def merge_dataframes(basics_df, ratings_df, akas_df):
    # Merge title.akas with title.basics
    merged_df = pd.merge(akas_df, basics_df, on='tconst', how='inner')
    # Merge the result with title.ratings
    merged_df = pd.merge(merged_df, ratings_df, on='tconst', how='inner')
    return merged_df

# Merge the DataFrames
merged_df = merge_dataframes(basics_df, ratings_df, akas_df)
# merged_df = merged_df[merged_df['region'] == 'US']

# Function to load merged DataFrame into MongoDB
def load_merged_data(df, collection_name):
    records = df.to_dict(orient='records')
    db[collection_name].insert_many(records)

# Load the merged DataFrame into MongoDB
load_merged_data(merged_df, 'all_imdb_data')