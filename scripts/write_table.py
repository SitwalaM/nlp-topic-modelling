import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine



#credentials
user = 'root'
passw = 'jesuswalks'  #insert your password here
host =  'localhost'
port = 3306
database = 'nlp'

database_connection = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(user, passw,
                                                      host, database), pool_recycle=1, pool_timeout=57600).connect()



def update_db_with_data(database_connection, dataframe, table_name, dtypes_dictionary):
    ''' function used to connect to update tables in the sql database
    inputs
    ------
    database_connection : connection object using sqlalchemy "create engine"
    dataframe: pandas datarame to be added to the database
    table_name: string name of table in database
    dtypes_dictionary: dictionary of datatypes for columns in the dataframe

    outputs
    -------
    None
    '''

    dataframe.to_sql(con=database_connection,
                     name=table_name,
                     if_exists='append',
                     index = False,
                     dtype = dtypes_dictionary,
                     chunksize=1000)
    return None


dtypes_dictionary = {"id": sqlalchemy.types.BigInteger,
                   "retweet_count": sqlalchemy.types.Numeric,
                    "date_created": sqlalchemy.types.DateTime(),
                    "tweet": sqlalchemy.types.Text,
                    "clean_tweet": sqlalchemy.types.Text,
                    "topic": sqlalchemy.types.Numeric
                    }


