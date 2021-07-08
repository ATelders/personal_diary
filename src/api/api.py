import sys
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from typing import Optional
from os import name
import requests
from fastapi import Body, FastAPI
from src.database.classes import Diary_entry, User
import uvicorn
from src.utils.sql_requests import *

import pickle5 as pickle
import datetime
from src.utils.functions import date_to_datetime, save_img, call_connector
import pandas as pd

# Instanciate the API
app = FastAPI()

# NLP model
filename = '/home/apprenant/simplon_projects/personal_diary/models/lr_kaggle_tfidf.sav'
classifier = pickle.load(open(filename, 'rb'))
tf = pickle.load(open('/home/apprenant/simplon_projects/personal_diary/models/tfidf.sav', 'rb'))



# Connect to SQL

DB_NAME = 'personal_diary'


@app.get("/")
async def root():
    return {"message": "happiness"}

### POST

# Request to add a new user

@app.post("/user")
def add_user(user_data: User): #The parameter User is a class
    db_connection, db_cursor = call_connector(db=DB_NAME) #connection with db
    
    # Define and execute the query
    query = """ INSERT INTO user (
                name, first_name, email)
                VALUES (%s, %s, %s)
            """
    values = ([user_data.name, user_data.first_name, user_data.email])
    db_cursor.execute(query, values)
    id = db_cursor.lastrowid
    save_img(id)
    # Save changes into the database
    db_connection.commit()
    return {'id': id}


# Request to add a new entry

@app.post("/entry")
def add_entry(entry_data: Diary_entry): #The parameter User is a class
    db_connection, db_cursor = call_connector(db=DB_NAME) #connection with db
    
    # Define and execute the query
    query = """ INSERT INTO diary_entry (
                user_id, date, content, emotion)
                VALUES (%s, %s, %s, %s)
            """
    values = ([
        entry_data.user_id,
        datetime.datetime.strptime(entry_data.date, "%m/%d/%y").date(),
        entry_data.content,
        entry_data.emotion,
        ])
    db_cursor.executemany(query, values)
    # Save changes into the database
    db_connection.commit()
    return {"entry_date" : entry_data.date, "text_content" : entry_data.content}


# GET


@app.get("/users")
async def get_all_users():
    '''
    Get the users list
    '''
    db_connection, db_cursor = call_connector(db=DB_NAME) #connection with db

    db_cursor.execute(request_display_all_users)
    users = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return {'users': users}


@app.get("/user_id/{user_id}")
async def get_user(user_id):
    '''
    Get the user from his id. Returns a JSON
    '''
    db_connection, db_cursor = call_connector(db=DB_NAME) #connection with db

    user_id = int(user_id)
    db_cursor.execute(request_select_user, (user_id, ))
    user = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return {'user_id': user }

@app.get("/user_id/entries/{user_id}")
async def get_entries(user_id):
    db_connection, db_cursor = call_connector(db=DB_NAME) #connection with db

    user_id = int(user_id)
    db_cursor.execute(request_entries_from_user, (user_id, ))
    entries = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return {'entries': entries }

@app.get("/user_id/entries/{user_id}/{date}")
async def get_entries_date(
    user_id: int,
    date: Optional[datetime.datetime]
    ):
    db_connection, db_cursor = call_connector(db=DB_NAME) #connection with db

    user_id = int(user_id)
    db_cursor.execute(request_entries_from_user_and_date, (user_id, date))
    entries = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return {'entries': entries }

@app.get("/entries/{date_1}/{date_2}")
async def get_all_entries_dates(
    date_1: datetime.datetime,
    date_2: datetime.datetime
    ):
    db_connection, db_cursor = call_connector(db=DB_NAME) #connection with db

    db_cursor.execute(request_all_entries_between_dates, (date_1, date_2))
    entries = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return {'entries': entries }


@app.get("/emotion/{sentence}")
def predict_emotion(sentence):
    '''
    Predict the emotion in a text
    '''
    matrix = tf.transform([sentence])
    predictions = classifier.predict(matrix)
    predictions_proba = classifier.predict_proba(matrix)
    print(predictions_proba)
    labels = ["happy", "sadness", "love", "anger", "fear", "surprise"]
    labels.sort()
    data = {'Labels':labels,
            'Probabilities':predictions_proba[0]}
    proba_df = pd.DataFrame(data, columns=['Labels', 'Probabilities'])
    
    return {'label': labels[int(predictions)], 'probas': proba_df}

#list(predictions_proba[0]

# PUT

@app.put("/update_user/{user_id}")
def update_user(user_id, user_data: User):
    db_connection, db_cursor = call_connector(db=DB_NAME) #connection with db

    db_cursor.execute(request_update_user, ([user_data.name, user_data.first_name, user_data.email, user_id]))
    db_cursor.close()
    db_connection.commit()
    db_connection.close()


# DELETE

@app.delete("/delete_user/{user_id}")
def delete_user(user_id: int):
    db_connection, db_cursor = call_connector(db=DB_NAME) #connection with db

    db_cursor.execute(request_delete_user, (user_id, ))
    db_cursor.close()
    db_connection.commit()
    db_connection.close()


# When this file is called from the terminal, the API is launched

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True, host="0.0.0.0", port=8080)
