import json
import requests
from datetime import date, datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

def get_entries_date(user_id, date):
    '''
    Get all the entries from a user's id
    '''
    res = requests.get(f"http://0.0.0.0:8080/user_id/entries/{user_id}/{date}")
    print('get entries')
    print(date)
    path = res.json()
    entries = path['entries']
    return entries

def get_all_entries_dates(date_1, date_2):
    '''
    Get all the entries between 2 dates
    '''
    res = requests.get(f"http://0.0.0.0:8080/entries/{date_1}/{date_2}")
    print('get entries')
    print(date_1)
    print(date_2)
    path = res.json()
    print(path)
    entries = path['entries']
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


def display_entries(entries):
    for item in range(len(entries)):
        d = datetime.strptime(entries[item][2], '%Y-%m-%dT%H:%M:%S')
        st.write("Date: {0:%d} {0:%B} {0:%Y}".format(d))
        st.write("Phrase: ", entries[item][3])
        st.write("Émotion: ", entries[item][4])
        st.markdown("<hr />", unsafe_allow_html=True)

def display_pie_chart(entries):
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