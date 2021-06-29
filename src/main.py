import sys

from utils.api import get_entries
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.utils.functions import add_user, get_user_info, delete_user
import streamlit as st

a = st.sidebar.radio('Menu du coach:',[
    'Créer un utilisateur',
    'Afficher un utilisateur',
    'Supprimer un utilisateur'])

st.title('La page du coach')


# Insert user
if a == 'Créer un utilisateur':
    st.subheader('Créer un nouvel utilisateur')
    user = {}
    user['name'] = st.text_input('nom')
    user['first_name'] = st.text_input('prenom')
    user['email'] = st.text_input('email')

    submit = st.button('Submit')
    if submit:
        try :
            add_user(user)
            print("Utilisateur créé : {}".format(user))
        except :
            print("L'utilisateur'{} existe déjà".format(user))


# Find user from id
elif a == 'Afficher un utilisateur':
    st.subheader("Afficher les info d'un utilisateur")
    st.text('Chercher un utilisateur avec son id')
    id = st.text_input('id')


    if id:
        name, first_name, email = get_user_info(id)
        st.write("Le nom de l'utilisateur avec l'id {} est {} {}".format(id, first_name, name))
        st.write("Son email est : {}".format(email))
        st.markdown("<hr />", unsafe_allow_html=True)

        entries = get_entries(id)['entries']
        for item in range(len(entries)):
            st.write("Phrase: ", entries[item][3])
            st.write("Émotion: ", entries[item][4])
            st.markdown("<hr />", unsafe_allow_html=True)


elif a == 'Supprimer un utilisateur':
    st.subheader("Supprimer un utilisateur")
    id = st.text_input('id')
    if id:
        try:
            delete_user(int(id))
            print("Utilisateur supprimé : {}".format(id))
        except :
            print("L'utilisateur'{} n'a pas pu être supprimé".format(id))