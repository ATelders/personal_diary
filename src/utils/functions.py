import requests
from datetime import date
import locale

from utils.classes import Diary_entry
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

def get_emotion(text):
    res = requests.get(f"http://0.0.0.0:8080/emotion/{text}")
    path = res.json()
    emotion = path['label']
    return emotion

def get_user_info(id):
    res = requests.get(f"http://0.0.0.0:8080/user_id/{id}")
    path = res.json()
    user = path['user_id'][0]
    name = user[1]
    first_name = user[2]
    email = user[3]
    return name, first_name, email

def add_user(user):
    requests.post("http://0.0.0.0:8080/add_user", json=user)

def get_today():
    return date.today()

def add_entry(diary_entry):
    requests.post("http://0.0.0.0:8080/add_entry", json=diary_entry)