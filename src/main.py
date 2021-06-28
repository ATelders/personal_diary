import sys
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.utils.functions import add_user, get_user_info
import streamlit as st

st.title('La page du coach')

user = {}

user['name'] = st.text_input('nom')
user['first_name'] = st.text_input('prenom')
user['email'] = st.text_input('email')


submit = st.button('Submit')

# Insert user

if submit:
    try :
        add_user(user)
        print("Utilisateur créé : {}".format(user))
    except :
        print("L'utilisateur'{} existe déjà".format(user))


# Find user from id

st.text('Chercher un utilisateur avec son id')
id = st.text_input('id')


if id:
    name, first_name, email = get_user_info(id)
    st.write("Le nom de l'utilisateur avec l'id {} est {} {}".format(id, first_name, name))
    st.write("Son email est : {}".format(email))
