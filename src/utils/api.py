from os import name
from fastapi import FastAPI
import uvicorn
import sys
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.config import USER, PASSWORD
from src.utils.sql_requests import request_select_user, request_add_user, request_add_entry, request_entries_from_user
import mysql.connector
from mysql.connector import errorcode
import pickle5 as pickle
import datetime

# Instanciate the API
app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8080)

# NLP model
filename = '/home/apprenant/simplon_projects/personal_diary/models/lr_kaggle_tfidf.sav'
classifier = pickle.load(open(filename, 'rb'))
tf = pickle.load(open('/home/apprenant/simplon_projects/personal_diary/models/tfidf.sav', 'rb'))

# Connect to SQL

DB_NAME = 'personal_diary'

def get_connection():
    db_connection = mysql.connector.connect(
        user=USER,
        database=DB_NAME,
        password=PASSWORD)
    return db_connection


# GET

@app.get("/")
async def root():
    return {"message": "happiness"}

@app.get("/user_id/{user_id}")
def get_user(user_id):
    '''
    Get the user from his id. Returns a JSON
    '''
    db_connection = get_connection()
    cursor = db_connection.cursor()
    user_id = int(user_id)
    cursor.execute(request_select_user, (user_id, ))
    user = cursor.fetchall()
    cursor.close()
    db_connection.close()
    return {'user_id': user }

@app.get("user_id/entries/{user_id}")
def get_entries(user_id):
    db_connection = get_connection()
    cursor = db_connection.cursor()
    user_id = int(user_id)
    cursor.execute(request_entries_from_user, (user_id, ))
    entries = cursor.fetchall()
    cursor.close()
    db_connection.close()
    return {'entries': entries }  

@app.get("/emotion/{sentence}")
def predict_emotion(sentence):
    '''
    Predict the emotion in a text
    '''
    matrix = tf.transform([sentence])
    predictions = classifier.predict(matrix)
    labels = ["happy", "sadness", "love", "anger", "fear", "surprise"]
    labels.sort()
    return {'label': labels[int(predictions)]}

# POST

@app.post("/add_user")
def add_user(user_data: dict):
    db_connection = get_connection()
    cursor = db_connection.cursor()
    cursor.execute(request_add_user, ([user_data['name'], user_data['first_name'], user_data['email']]))
    cursor.close()
    db_connection.commit()
    db_connection.close()

@app.post("/add_entry")
def add_entry(entry_data: dict):
    db_connection = get_connection()
    cursor = db_connection.cursor()
    cursor.execute(request_add_entry, ([
        entry_data['user_id'],
        datetime.datetime.strptime(entry_data["date"], "%m/%d/%y").date(),
        entry_data["content"],
        entry_data["emotion"],
        ])
    )
    cursor.close()
    db_connection.commit()
    db_connection.close()

