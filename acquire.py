import env
import os
import pandas as pd
import numpy as np

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    return pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

def get_iris_data():
    return pd.read_sql('SELECT * FROM species JOIN measurements USING(species_id)', get_connection('iris_db'))

def get_telco_data():
    return pd.read_sql('''SELECT * FROM customers join customer_contracts using(customer_id) 
                        join customer_payments using(customer_id) 
                        join internet_service_types using(internet_service_type_id);''', get_connection('telco_churn'))

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

def csv_telco_data():
    filename = "telco_churn.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = get_telco_data()
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

