from fastapi import FastAPI
import sys
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.config import USER, PASSWORD
from src.utils.edit_users import select_user
import mysql.connector
from mysql.connector import errorcode

# MySQL Connector
DB_NAME = 'personal_diary'
db_connection = mysql.connector.connect(user=USER, database=DB_NAME, password=PASSWORD)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "happiness"}


@app.get("/{user_id}")
def get_user(user_id):
    cursor = db_connection.cursor()
    user_id = int(user_id)
    cursor.execute(select_user, (user_id, ))
    user = cursor.fetchall()
    print(user)
    cursor.close()
    return {'user_id': user }


db_connection.close()

