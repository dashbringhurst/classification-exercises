import os
import numpy as np
import pandas as pd


def prep_iris():
    '''This function takes the iris dataframe from the acquire.py function csv_iris_data() and cleans it.'''
    df_iris = acquire.csv_iris_data()
    df_iris = df_iris.drop(columns=['species_id', 'measurement_id'])
    df_iris = df_iris.rename(columns={'species_name':'species'})
    dummy_iris = pd.get_dummies(df_iris[['species']], dummy_na=False)
    df_iris = pd.concat([df_iris, dummy_iris], axis=1)
    return df_iris

def prep_titanic():
    titanic_db = acquire.csv_titanic_data()
    titanic_db = titanic_db.drop(columns=['class', 'embarked','age','deck'])
    dummy_titanic = pd.get_dummies(titanic_db[['sex', 'embark_town']], dummy_na=False, drop_first=True)
    titanic_db = pd.concat([titanic_db, dummy_titanic], axis=1)
    titanic_db['embark_town'] = titanic_db.embark_town.fillna(value='Southampton')
    return titanic_db

def prep_telco():
    telco = acquire.csv_telco_data()
    telco = telco.drop(columns=['internet_service_type_id','contract_type_id.1','payment_type_id.1','paperless_billing.1','monthly_charges.1','total_charges.1'])
    telco['customer_id'] = telco.customer_id.str.slice(stop=4).astype(int)
    telco['total_charges'] = telco.total_charges.str.replace('$','').str.replace(',','').str.replace(' ','').fillna(0)
    telco['total_charges'] = pd.to_numeric(telco.total_charges)
    dummy_telco = pd.get_dummies(telco[['gender','partner','dependents','phone_service','multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies','paperless_billing','churn','internet_service_type']], drop_first=True)
    telco = pd.concat([telco, dummy_telco], axis=1)
    telco = telco.drop(columns=['gender','partner','dependents','phone_service','multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies','paperless_billing','churn','internet_service_type'])
    return telco

def split_data(df, column):
    '''This function takes in two arguments, a dataframe and a string. The string argument is the name of the
        column that will be used to stratify the train_test_split. The function returns three dataframes, a 
        training dataframe with 60 percent of the data, a validate dataframe with 20 percent of the data and test
        dataframe with 20 percent of the data.'''
    train, test = train_test_split(df, test_size=.2, random_state=217, stratify=df[column])
    train, validate = train_test_split(train, test_size=.25, random_state=217, stratify=train[column])
    return train, validate, test