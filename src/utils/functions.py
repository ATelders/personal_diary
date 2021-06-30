import json
import requests
from datetime import date, datetime
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

def get_users():
    res = requests.get(f"http://0.0.0.0:8080/users")
    path = res.json()
    print(path)

    return path    

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
    response = requests.post("http://0.0.0.0:8080/add_user", json=user)
    return response

def update_user(user_id, user):
    '''
    Update a user
    '''
    response = requests.put(f"http://0.0.0.0:8080/update_user/{user_id}", json=user)
    return response


def add_entry(diary_entry):
    '''
    Add a new diary entry
    '''
    requests.post("http://0.0.0.0:8080/add_entry", json=diary_entry)

def get_entries(user_id):
    '''
    Get all the entries from a user's id
    '''
    res = requests.get(f"http://0.0.0.0:8080/user_id/entries/{user_id}")
    path = res.json()
    entries = path['entries']
    return entries

def get_entries_date(dict_date):
    '''
    Get all the entries from a user's id
    '''
    res = requests.get(f"http://0.0.0.0:8080/user_id/entries_date", json=dict_date)
    entries = res.json()
    return entries

def delete_user(id):
    requests.delete(f"http://0.0.0.0:8080/delete_user/{id}")

def date_to_datetime(date):
    return datetime.combine(date ,datetime.min.time())

def save_img(user_id):
    response = requests.get("https://thispersondoesnotexist.com/image")
    file = open("/home/apprenant/simplon_projects/personal_diary/avatars/{}.png".format(user_id), "wb")
    file.write(response.content)
    file.close()

def get_image_path(user_id):
    return "/home/apprenant/simplon_projects/personal_diary/avatars/{}.png".format(user_id)