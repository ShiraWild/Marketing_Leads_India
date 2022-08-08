#imports
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker
import psycopg2
import pandas as pd

#Load leads_predictions - the predictions of the test dataset

leads_predictions = pd.read_csv("C:\\Users\\Shir\\Desktop\\nativs\\interviews\\buzzer-ai\\leads_predictions.csv")

#Create list containing data rows
leads_predictions_lst = []
for index, rows in leads_predictions.iterrows():
    # Create list for the current row
    row_lst = (rows.LeadNumber, rows.Score)
    leads_predictions_lst.append(row_lst)


#Local connection to the db
Base = declarative_base()
path_url = 'postgresql+psycopg2://postgres:postgres@localhost/postgres'
engine = create_engine(path_url)
Base.metadata.create_all(engine)


try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="Leads")
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO "Predictions" (lead_id, score) VALUES (%s,%s)"""

    #add predictions to the db
    for row in leads_predictions_lst:
        cursor.execute(postgres_insert_query, row)
        connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

