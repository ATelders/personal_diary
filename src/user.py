import sys
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.utils.functions import *
import streamlit as st

st.text("Entrez votre numéro d'utilisateur :")
user_id = st.text_input('id')
if user_id:
    name, first_name, email = get_user_info(user_id)
    st.title("Journal intime de {} {}".format(first_name, name))

st.write("Aujourd'hui, nous sommes le {0:%d} {0:%B} {0:%Y}.".format(date.today()))

st.text("Entrez un texte : (Analyse d'émotions)")

text = st.text_input('texte')
submit = st.button('Envoyer')

if user_id and text and submit:
    external_data = {}
    external_data['user_id'] = user_id
    external_data['date'] = datetime.today().strftime("%m/%d/%y")
    external_data['content'] = text
    external_data['emotion'] = get_emotion(text)
    print(external_data)
    add_entry(external_data)



date_input = st.date_input('Entrez une date pour rechercher le texte correspondant :')
submit_date = st.button('Envoyer', key='submit_date')
if submit_date and user_id:
    date_input = str(date_to_datetime(date_input))
    dict_date = {'id': user_id, 'date': date_input}
    entries = get_entries_date(dict_date)
    entries
