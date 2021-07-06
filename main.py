import numpy as np
import pandas as pd
import streamlit as st
import sqlalchemy
import pyodbc
import urllib
from cryptography.fernet import Fernet


uploaded_file = st.file_uploader("UPLOAD DATA")  # Input data


if uploaded_file is not None:  # Checking if data has been uploaded
    flag = False
    try:  # CSV type check
        data = pd.read_csv(uploaded_file)
        st.success('File Uploaded Successfully')
        flag = True
    except:  # Invalid type error
        st.error('Upload CSV File Only')

    if flag:
        print('Uploading data')
        quoted = urllib.parse.quote_plus("Driver={SQL Server Native Client 11.0};"  # SQL connection details
                                         "Server=LAPTOP-A0QM0AR0;"
                                         "Database=Task;"
                                         "Trusted_Connection=yes;")
        engine = sqlalchemy.create_engine(
            'mssql+pyodbc:///?odbc_connect={}'.format(quoted))  # Connecting to SQL server
        data.to_sql('data', schema='dbo', con=engine, chunksize=200,
                    method='multi', index=False, if_exists='replace')  # Uploading CSV as table
        print('Uploaded')
