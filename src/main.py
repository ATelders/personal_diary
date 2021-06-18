import sys
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.config import USER, PASSWORD
from src.utils.edit_users import add_user
import streamlit as st
import mysql.connector
from mysql.connector import errorcode

# MySQL Connector
DB_NAME = 'personal_diary'
db_connection = mysql.connector.connect(user=USER, database=DB_NAME, password=PASSWORD)
cursor = db_connection.cursor()



st.title('Personal Diary')


name = st.text_input('nom')
prenom = st.text_input('prenom')
email = st.text_input('email')

user_data = [name, prenom, email]

submit = st.button('Submit')

# Insert user

if submit:
    try :
        cursor.execute(add_user, user_data)
        print("Utilisateur créé : {}".format(user_data))
    except :
        print("L'utilisateur'{} existe déjà".format(user_data))


db_connection.commit()