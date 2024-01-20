import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from all_flights import settings


settings_data = settings.DATABASES['default'].items()
hostname = 'localhost'
database = list((value for key, value in settings_data if key == 'NAME'))[0]
username = list((value for key, value in settings_data if key == 'USER'))[0]
pwd = list((value for key, value in settings_data if key == 'PASSWORD'))[0]
port_id = list((value for key, value in settings_data if key == 'PORT'))[0]

engine = create_engine("postgresql+psycopg2://postgres:Shoosh3434@localhost:5432/jb_flights")
with pd.ExcelFile(r'C:\\Users\\Josh\\flights_202401182213.xlsx') as xlsx_file:
    df = pd.read_excel(xlsx_file)
    df.to_sql(name='flights', con=engine, if_exists='append', index=False)




