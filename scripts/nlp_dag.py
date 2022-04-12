from pull_tweets import extract
from twitter_preprocessing import process_tweets
from write_table import update_db_with_data
import datetime as dt
from model_predict import get_inference
import pickle
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from datetime import timedelta
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import os


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 4, 8),
    'email': ['sitwala.mundia@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=15)
}



dag = DAG(
    'nlp_twitter',
    default_args=default_args,
    description='DAG for twitter monitor',
    schedule_interval = "0 */8 * * *",
)


def extract_clean():
    filename = "clean_"+str(dt.date.today()) + ".csv"
    df = extract()
    cleaned_df = process_tweets(df)
    df.to_csv(filename)

    return cleaned_df


def modelling():
    # function to run model in the pipeline
    # returns dataframe with predictions in column topic

    with open("lda_model.pk","rb") as f:
        lda_model = pickle.load(f)
    
    # vectorizer  
    vectorizer = pickle.load(open("vectorizer.pickle", 'rb'))

    # topics
    topics = list(np.arange(0,10))
    

    #cleaned_df = extract_clean()    
    cleaned_df = pd.read_csv("clean_"+str(dt.date.today()) + ".csv")
    cleaned_df["topic"] = cleaned_df.clean_tweet.apply(lambda x: get_inference(lda_model,vectorizer,topics,np.str_(x),0))
    cleaned_df.to_csv("predict_"+"clean_"+str(dt.date.today()) + ".csv")

    return cleaned_df



def update_db():
    # function that upates dataset in MySQL database in the pipeline
    user = 'root'
    passw = '****'  #insert your password here
    host =  'localhost'
    port = 3306
    database = 'nlp'

    database_connection = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                format(user, passw,
                                                        host, database), pool_recycle=1, pool_timeout=57600).connect()
    dtypes_dictionary = {"id": sqlalchemy.types.BigInteger,
                    "retweet_count": sqlalchemy.types.Numeric,
                        "date_created": sqlalchemy.types.DateTime(),
                        "tweet": sqlalchemy.types.Text,
                        "clean_tweet": sqlalchemy.types.Text,
                        "topic": sqlalchemy.types.Numeric
                        }
    dataframe = pd.read_csv("predict_"+"clean_"+str(dt.date.today()) + ".csv")
    datframe = dataframe.loc[dataframe.id != "id"]
    update_db_with_data(database_connection, dataframe, "topics", dtypes_dictionary)
    os.remove("clean_"+str(dt.date.today()) + ".csv")
    os.remove("predict_"+"clean_"+str(dt.date.today()) + ".csv")
    return None

# python operators for the pipeline are defined below
extract_tweets = PythonOperator(
    task_id='extract_clean',
    python_callable=extract_clean,
    dag=dag,
)

model = PythonOperator(
    task_id='predictions',
    python_callable=modelling,
    dag=dag,
)

update_db = PythonOperator(
    task_id='update_database',
    python_callable=update_db,
    dag=dag,
)

# define pipeline and dependencies here
extract_tweets >> model >> update_db
