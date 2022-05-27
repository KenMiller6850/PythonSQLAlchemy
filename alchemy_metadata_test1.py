# To insert data frame into MS SQL database without iterate the data-frame
import pandas
from pathlib import Path
from os import chdir
from pyrsistent import v
from sqlalchemy import create_engine, MetaData, Table, select,text
from ReadConfig2 import getSQLCONFIG


#filePath = Path(__file__).resolve().parent / "FlagstaffWeatherData.csv"
configFilePath = Path(__file__).resolve().parent / "config.ini"

c = getSQLCONFIG(configFilePath)

#params = ("DRIVER={SQL Server};SERVER=dev_151.sql.caresource.corp\dev_151;DATABASE=InternalAudit;Trusted_Connection=yes")

params = ("DRIVER={SQL Server};SERVER=" + c[1] + ";DATABASE=" + c[0] +";Trusted_Connection=yes")


try:
  engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params) 
  conn = engine.connect() 
  print('Connected to database')
  metadata = MetaData()
  mytable = Table('SubscriberIDMaster',metadata,autoload=True,autoload_with=engine)
  
  # Print the column names
  print(mytable.columns.keys())

  # Print full table metadata
  print(repr(metadata.tables['SubscriberIDMaster']))


  #metadata = MetaData(conn)
  #metadata.reflect()
  #mytable = metadata.tables['SubscriberIDMaster']

  #print(mytable.columns.keys())








  #print(metadata.tables)


  #print(result)

  #mytable = MetaData.tables['SubscriberIDMaster']


  conn.close
  engine.dispose

except:
  print('Database connection error')  