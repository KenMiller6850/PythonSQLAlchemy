# To insert data frame into MS SQL database without iterate the data-frame
import pandas
from pathlib import Path
from os import chdir
from sqlalchemy import create_engine, MetaData, Table, select,text
from ReadConfig2 import getSQLCONFIG


filePath = Path(__file__).resolve().parent / "FlagstaffWeatherData.csv"
configFilePath = Path(__file__).resolve().parent / "config.ini"

c = getSQLCONFIG(configFilePath)

#params = ("DRIVER={SQL Server};SERVER=dev_151.sql.caresource.corp\dev_151;DATABASE=InternalAudit;Trusted_Connection=yes")

params = ("DRIVER={SQL Server};SERVER=" + c[1] + ";DATABASE=" + c[0] +";Trusted_Connection=yes")

df = pandas.read_csv(filePath,parse_dates=['DATE'])

df2 = df.fillna(-999)

try:
  engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params) 
  engine.connect() 
  df2.to_sql(name='WeatherData',con=engine, index=False, if_exists='replace')
  print('CSV file transferred')  
except:
  print('Database connection error')  


#with engine.connect() as connection:
#    result = connection.execute(text("SELECT [ReceiverIEN],[PlanID] FROM [CARL_POC].[dbo].[Receiver]"))
#    for row in result:
#        print("ReceiverIEN:", row['ReceiverIEN'])

