from pathlib import Path
from os import chdir
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData,inspect
from ReadConfig2 import getSQLCONFIG

meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

configFilePath = Path(__file__).resolve().parent / "config.ini"

c = getSQLCONFIG(configFilePath)

params = ("DRIVER={SQL Server};SERVER=" + c[1] + ";DATABASE=" + c[0] +";Trusted_Connection=yes")


try:
  engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params) 
  
  
  conn = engine.connect() 


  print('Connected to database')

  insp = inspect(engine)
  
  if insp.has_table("students", schema="dbo"):  # True (or False, as the case may be)
     print('Table Exists')
  else:
     print('Table does not exist')    
     try:
       meta.create_all(engine)
       print('Table has been created') 
     except:     
       print('Error creating table')  

  conn.close
  engine.dispose

except:
  print('Database connection error')  
