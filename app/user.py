import sys
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
import streamlit as st
from datetime import date
from src.utils.functions import *

user_id = st.sidebar.text_input("Entrez votre numéro d'utilisateur :")

if user_id:
    try:
        name, first_name, email = get_user_info(user_id)
        st.title("Journal intime de {} {}".format(first_name, name))
        try:
            st.image(get_image_path(user_id), width=100)
        except:
            pass
        st.write("""
         Aujourd'hui, nous sommes le {0:%d} {0:%B} {0:%Y}.
         """
         .format(date.today()))

        st.text("Entrez un texte : (Analyse d'émotions)")

        text = st.text_input('texte')
        submit = st.button('Envoyer')

        if user_id and text and submit:
            external_data = {}
            external_data['user_id'] = user_id
            external_data['date'] = datetime.today().strftime("%m/%d/%y")
            external_data['content'] = text
            external_data['emotion'], probas = get_emotion(text)
            add_entry(external_data)

        try:
            date_input = st.date_input('''
            Entrez une date pour rechercher le texte correspondant :
            ''', key='1')
            submit_date = st.button('Envoyer', key='submit_date')
        except:
            date_input = None
            date_input = st.date_input('''
            Entrez une date pour rechercher le texte correspondant :
            ''', key='2')
            submit_date = st.button('Envoyer', key='submit_date_2')
        if user_id:
            if submit_date:

                date_input = date_to_datetime(date_input)
                dict_date = {'id': user_id, 'date': date_input}
                print(dict_date)
                entries = get_entries_date(user_id, date_input)
                print(entries)
                if entries == []:
                    st.write("Il n'y a pas de texte à la date sélectionnée.")
                display_entries(entries)
    except:
        st.write("Il n'y a pas d'utilisateur avec l'id {}".format(user_id))

