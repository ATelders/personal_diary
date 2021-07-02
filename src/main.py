import sys


from utils.api import get_entries, update_user
from utils.classes import User
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.utils.functions import *
import streamlit as st
import time


a = st.sidebar.radio('Menu du coach:',[
    'Afficher tous les utilisateurs',
    'Créer un utilisateur',
    'Afficher un utilisateur',
    'Ambiance générale'
    ])

st.title('La page du coach')

# Display all users
if a == 'Afficher tous les utilisateurs':
    users = get_users()['users']
    for item in range(len(users)):
        st.markdown("<hr />", unsafe_allow_html=True)
        st.write("n° client: ", users[item][0])
        st.write("Nom: ", users[item][2], users[item][1])
        st.write("E-mail: ", users[item][3])
        action = st.radio('Radio', ['Afficher', 'Modifier','Supprimer'], key=users[item][0])
        if action == 'Supprimer':
            if st.button('Confirmer la suppression'):
                delete_user(int(users[item][0]))
                #users.pop(item)
        
        elif action == 'Modifier':
            data = {}
            data['name'] = st.text_input('Nom', users[item][1])
            data['first_name'] = st.text_input('Prénom', users[item][2])
            data['email'] = st.text_input('E-mail', users[item][3])
            submit = st.button('Valider')
            if submit:
                update_user(int(users[item][0]), data)


# Insert user
elif a == 'Créer un utilisateur':
    st.subheader('Créer un nouvel utilisateur')
    name = st.text_input('Nom')
    first_name = st.text_input('Prénom')
    email = st.text_input('E-mail')
    st.write(first_name, name, email)
    submit = st.button('Valider')

    if name and first_name and email and submit:
        external_data = {}
        external_data['name'] = name
        external_data['first_name'] = first_name
        external_data['email'] = email
        add_user(external_data)

# Find user from id
elif a == 'Afficher un utilisateur':
    st.subheader("Afficher les info d'un utilisateur")
    st.text('Chercher un utilisateur avec son id')
    id = st.text_input('id')


    if id:
        try:
            st.image(get_image_path(id), width=100)
        except:
            pass

        name, first_name, email = get_user_info(id)
        st.write("Le nom de l'utilisateur avec l'id {} est {} {}".format(id, first_name, name))
        st.write("Son email est : {}".format(email))
        st.markdown("<hr />", unsafe_allow_html=True)
        try:
            entries = get_entries(id)
            with st.spinner(text='Construction de la roue des émotions...'):
                time.sleep(3)
                display_pie_chart(entries)
        except:
            pass

        display_entries(entries)

elif a == 'Ambiance générale':
    st.header('Ambiance générale')
    st.write("Choisissez la période: ")
    date_1 = st.date_input('Entre le: ', key='date_1')
    date_2 = st.date_input('et le :', key='date_2')
    date_1 = date_to_datetime(date_1)
    date_2 = date_to_datetime(date_2)

    if date_1 and date_2:
        entries = get_all_entries_dates(date_1, date_2)
        st.write('Il y a {} textes sur cette période.'.format(len(entries)))

        display_pie_chart(entries)
