import os
import numpy as np
import pandas as pd
import acquire
from sklearn.model_selection import train_test_split


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
    telco = acquire.get_telco_data()
    telco['gender'] = telco.gender.map({'Female': 0, 'Male': 1})
    telco['partner'] = telco.partner.map({'Yes': 1, 'No': 0})
    telco['dependents'] = telco.dependents.map({'Yes': 1, 'No': 0})
    telco['phone_service'] = telco.phone_service.map({'Yes': 1, 'No': 0})
    telco['paperless_billing'] = telco.paperless_billing.map({'Yes': 1, 'No': 0})
    telco['churn'] = telco.churn.map({'Yes': 1, 'No': 0})
    telco['multiple_lines'] = telco.multiple_lines.str.replace('No phone service', 'No')
    telco['payment_type'] = telco.payment_type.str.replace('Electronic check','manual').str.replace('Mailed check','manual')
    telco['payment_type'] = telco.payment_type.str.replace('(','').str.replace(')', '').str.replace('Bank transfer automatic', 'auto').str.replace('Credit card automatic', 'auto')
    telco['streaming_tv'] = telco.streaming_tv.str.replace('No internet service','No')
    telco['streaming_movies'] = telco.streaming_movies.str.replace('No internet service', 'No')
    telco['online_security'] = telco.online_security.str.replace('No internet service', 'No')
    telco['online_backup'] = telco.online_backup.str.replace('No internet service', 'No')
    telco['device_protection'] = telco.device_protection.str.replace('No internet service', 'No')
    telco['tech_support'] = telco.tech_support.str.replace('No internet service', 'No')
    telco['total_charges'] = telco.total_charges.str.replace('$','').str.replace(',','').str.replace(' ','').fillna(0)
    telco['total_charges'] = pd.to_numeric(telco.total_charges)
    return telco

def split_data(df, column):
    '''This function takes in two arguments, a dataframe and a string. The string argument is the name of the
        column that will be used to stratify the train_test_split. The function returns three dataframes, a 
        training dataframe with 60 percent of the data, a validate dataframe with 20 percent of the data and test
        dataframe with 20 percent of the data.'''
    train, test = train_test_split(df, test_size=.2, random_state=217, stratify=df[column])
    train, validate = train_test_split(train, test_size=.25, random_state=217, stratify=train[column])
    return train, validate, test