from fastapi import FastAPI
import uvicorn
import sys
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.config import USER, PASSWORD
from src.utils.edit_users import select_user
import mysql.connector
from mysql.connector import errorcode

# MySQL Connector
DB_NAME = 'personal_diary'

app = FastAPI()

def get_connection():
    db_connection = mysql.connector.connect(
        user=USER,
        database=DB_NAME,
        password=PASSWORD)
    return db_connection

@app.get("/")
async def root():
    return {"message": "happiness"}


@app.get("/{user_id}")
def get_user(user_id):
    db_connection = get_connection()
    cursor = db_connection.cursor()
    user_id = int(user_id)
    cursor.execute(select_user, (user_id, ))
    user = cursor.fetchall()
    cursor.close()
    db_connection.close()
    return {'user_id': user }




if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8080)