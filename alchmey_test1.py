# To insert data frame into MS SQL database without iterate the data-frame
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select,text
#from six.moves import urllib
params = ("DRIVER={SQL Server};SERVER=dev_75.sql.caresource.corp\dev_75;DATABASE=CARL_POC;Trusted_Connection=yes")
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params) 
#engine.connect() 

with engine.connect() as connection:
    result = connection.execute(text("SELECT [ReceiverIEN],[PlanID] FROM [CARL_POC].[dbo].[Receiver]"))
    for row in result:
        print("ReceiverIEN:", row['ReceiverIEN'])

