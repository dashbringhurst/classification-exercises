import env
import os
import pandas as pd
import numpy as np

def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''This function uses credentials from an env file to log into a database'''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    '''The function uses the get_connection function to connect to a database and retrieve the titanic_db dataset'''
    return pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

def get_iris_data():
    return pd.read_sql('SELECT * FROM species JOIN measurements USING(species_id)', get_connection('iris_db'))

def new_telco_data():
    '''
    This function reads the telco data from the Codeup db into a df.
    '''
    sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, acquire.get_connection('telco_churn'))
    
    return df

def get_telco_data():
    '''
    This function reads in telco data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('telco.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('telco.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_telco_data()
        
        # Cache data
        df.to_csv('telco.csv')
        
    return df

def csv_titanic_data():
    filename = "titanic.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = get_titanic_data()
        df.to_csv(filename, index=False)
        return df  

def csv_iris_data():
    filename = "iris.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = get_iris_data()
        df.to_csv(filename, index=False)
        return df  


def get_tidy_data_attendance():
    return pd.read_sql('SELECT * FROM attendance', get_connection('tidy_data'))

def csv_tidy_data():
    filename = "tidy_data.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = get_tidy_data()
        df.to_csv(filename, index=False)
        return df  

def get_tidy_data_coffee():
    return pd.read_sql('SELECT * FROM coffee_levels', get_connection('tidy_data'))

def get_tidy_data_cake():
    return pd.read_sql('SELECT * FROM cake_recipes', get_connection('tidy_data'))

def get_tidy_data_gap1():
    return pd.read_sql('SELECT * FROM gapminder1', get_connection('tidy_data'))
