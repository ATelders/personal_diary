import sys
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.config import USER, PASSWORD
from src.utils.edit_users import add_client
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

client_data = [name, prenom, email]

submit = st.button('Submit')

# Insert user

if submit:
    try :
        cursor.execute(add_client, client_data)
        print("Client créé : {}".format(client_data))
    except :
        print("Le client{} existe déjà".format(client_data))


db_connection.commit()