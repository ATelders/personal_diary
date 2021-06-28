import sys

from utils.classes import Diary_entry
sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.utils.functions import get_emotion, get_today, add_entry
import streamlit as st

st.title('Journal intime')

# NLP

d = get_today()
user_id = 1


st.write("Aujourd'hui, nous sommes le {0:%d} {0:%B} {0:%Y}.".format(d))

st.text("Entrer un texte : (Analyse d'émotions)")

text = st.text_input('texte')
if text:
    emotion = get_emotion(text)
    today_entry = Diary_entry(id, user_id, str(d), text, emotion)
    today_entry.content = text
    add_entry(today_entry.entry_data())
    st.text(today_entry.get_text())
    st.write(get_emotion(today_entry))
