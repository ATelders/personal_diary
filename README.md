# personal_diary

### User
The user can write a text everyday in the app and search for the texts he wrote at any given date.

### Coach
The coach can add and edit users and get the texts for any users and the emotions associated to those texts.
He can visualize a chart of emotions for any users or for all the users.

## File Structure

```bash
personal_diary/
┣ app/
┃ ┣ main.py         # The coach's backoffice
┃ ┗ user.py         # The user app
┣ avatars/          # Users profile pictures
┣ models/           # ML models for emotion recognition
┣ src/
┃ ┣ api/            # API
┃ ┣ database/       # Create classes and tables
┃ ┣ utils/          # Functions and API requests
┃ ┗ config.py       # DB username and password
┣ test/
┣ .gitignore
┣ LICENSE
┣ README.md
┣ MPD.png           # Physical Data Model and Class Diagram
┗ environment.yml   # Conda environment
```