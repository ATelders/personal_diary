import sys
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.config import USER, PASSWORD
from src.utils.edit_users import add_user
import requests
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


# Find user from id

st.text('Chercher un utilisateur avec son id')
id = st.text_input('id')

def get_user(id):
    res = requests.get(f"http://0.0.0.0:8080/{id}")
    path = res.json()
    user = path['user_id'][0]
    name = user[1]
    first_name = user[2]
    email = user[3]
    return name, first_name, email

if id:
    name, first_name, email = get_user(id)
    st.write("Le nom de l'utilisateur avec l'id {} est {} {}".format(id, first_name, name))
    st.write("Son email est : {}".format(email))


db_connection.commit()