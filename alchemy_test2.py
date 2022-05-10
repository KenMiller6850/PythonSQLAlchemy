# To insert data frame into MS SQL database without iterate the data-frame
import pandas
from pathlib import Path
from os import chdir
from sqlalchemy import create_engine, MetaData, Table, select,text

print(Path.cwd())
filePath = Path(__file__).resolve().parent / "FlagstaffWeatherData.csv"

print(filePath)
df = pandas.read_csv(filePath,parse_dates=['DATE'])

df2 = df.fillna(-999)

print(df2)


params = ("DRIVER={SQL Server};SERVER=dev_151.sql.caresource.corp\dev_151;DATABASE=InternalAudit;Trusted_Connection=yes")
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params) 
engine.connect() 

df2.to_sql(name='WeatherData',con=engine, index=False, if_exists='append')

#with engine.connect() as connection:
#    result = connection.execute(text("SELECT [ReceiverIEN],[PlanID] FROM [CARL_POC].[dbo].[Receiver]"))
#    for row in result:
#        print("ReceiverIEN:", row['ReceiverIEN'])

