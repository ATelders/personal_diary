import requests
from datetime import date
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

def get_emotion(text):
    '''
    Get the emotion in the text
    '''
    res = requests.get(f"http://0.0.0.0:8080/emotion/{text}")
    path = res.json()
    emotion = path['label']
    return emotion

def get_user_info(id):
    '''
    Get the name, first name and email adress from the user id
    '''
    res = requests.get(f"http://0.0.0.0:8080/user_id/{id}")
    path = res.json()
    user = path['user_id'][0]
    name = user[1]
    first_name = user[2]
    email = user[3]
    return name, first_name, email

def add_user(user):
    '''
    Add a new user
    '''
    requests.post("http://0.0.0.0:8080/add_user", json=user)

def get_today():
    '''
    Get today's date
    '''
    return date.today()

def add_entry(diary_entry):
    '''
    Add a new diary entry
    '''
    requests.post("http://0.0.0.0:8080/add_entry", json=diary_entry)

def get_entries(user_id):
    '''
    Get all the entries from a user's id
    '''
    res = requests.get("http://0.0.0.0:8080/user_id/entries/{user_id}")
    entries = res.json()['entries']
    return entries


#def get_user_texts(name):