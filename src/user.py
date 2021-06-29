import sys

from utils.classes import Diary_entry
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.utils.functions import get_emotion, get_today, add_entry, get_entries_date, date_to_datetime
import streamlit as st

st.title('Journal intime')

d = get_today()


st.write("Aujourd'hui, nous sommes le {0:%d} {0:%B} {0:%Y}.".format(d))

st.text("Entrez votre numéro d'utilisateur :")
user_id = st.text_input('id')

st.text("Entrez un texte : (Analyse d'émotions)")

text = st.text_input('texte')
submit = st.button('Envoyer')

if submit:
    emotion = get_emotion(text)
    print(emotion)
    today_entry = Diary_entry(user_id, d.strftime("%m/%d/%y"), text, emotion)
    print(today_entry.entry_data())
    add_entry(today_entry.entry_data())
    st.text(today_entry.get_text())


# date_input = st.date_input('Entrez une date pour rechercher le texte correspondant :')
# submit_date = st.button('Envoyer', key='submit_date')
# if submit_date and user_id:
#     date_input = str(date_to_datetime(date_input))
#     dict_date = {'id': user_id, 'date': date_input}
#     entries = get_entries_date(dict_date)
#     entries
