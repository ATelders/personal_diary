import sys

from utils.classes import Diary_entry
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.utils.functions import get_emotion, get_today, add_entry
import streamlit as st

st.title('Journal intime')

d = get_today()

st.write("Aujourd'hui, nous sommes le {0:%d} {0:%B} {0:%Y}.".format(d))

st.text("Entrer votre numéro d'utilisateur :")
user_id = st.text_input('id')

st.text("Entrer un texte : (Analyse d'émotions)")

text = st.text_input('texte')
submit = st.button('Envoyer')

if submit:
    emotion = get_emotion(text)
    print(emotion)
    today_entry = Diary_entry(user_id, d.strftime("%m/%d/%y"), text, emotion)
    print(today_entry.entry_data())
    add_entry(today_entry.entry_data())
    st.text(today_entry.get_text())

