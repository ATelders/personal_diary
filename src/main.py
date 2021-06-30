import sys

from utils.api import get_entries, update_user
from utils.classes import User
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.utils.functions import *
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


a = st.sidebar.radio('Menu du coach:',[
    'Afficher tous les utilisateurs',
    'Créer un utilisateur',
    'Afficher un utilisateur',
    'Supprimer un utilisateur'
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
            entries_df = pd.DataFrame(entries)
            wheel_labels = pd.DataFrame()
            wheel_labels['emotions'] = entries_df[4].unique()
            wheel_labels['rates'] = entries_df[4].value_counts(normalize=True).values


            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = wheel_labels['emotions']
            sizes = wheel_labels['rates']
            length = len(labels.unique())
            explode = ([0.01 for i in range(length)])  # only "explode" the 2nd slice (i.e. 'Hogs')

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=False, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig1)
        except:
            pass




        for item in range(len(entries)):
            d = datetime.strptime(entries[item][2], '%Y-%m-%dT%H:%M:%S')
            st.write("Date: {0:%d} {0:%B} {0:%Y}".format(d))
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