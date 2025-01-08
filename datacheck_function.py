import pandas as pd
import numpy as np
import json
from app_store_scraper import AppStore

#load data from app store
balance = AppStore(country='us', app_name='balance-meditation-sleep', app_id = '1361356590')
balance.review(how_many=2000)
balance.reviews

#convert to dataframe
balance_df = pd.DataFrame(balance.reviews)
balance_df.head()

#check data quality function and load into postgres table.
def data_qual_checks(df):
    """
    preloading checks
    """
    check_results = {
        'missing_reviews_count': len(df[df['review'].isnull()]),
        'missing_ratings_count': len(df[df['rating'].isnull()]),
        'invalid_ratings_count': len(df[(df['rating'] < 1) | (df['rating'] > 5)])
    }

    return check_results

def load_data_postgres(df, table_name, conn_string):
    """
    load data into PostgresSQL table
    conn_string = connection string
    """
    engine = create_engine(conn_string)
    df.to_sql(table_name, engine, if_exists='fail', index=False)
    print(f'Data successfully loaded into {table_name}')

#run data quality checks
data_qual_checks(balance_df)